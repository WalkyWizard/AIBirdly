import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

class BirdDatabase:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS analyses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    analysis_type TEXT NOT NULL,
                    image_name TEXT,
                    predicted_species TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    analysis_date TEXT NOT NULL,
                    description TEXT,
                    scientific_name TEXT,
                    family TEXT,
                    habitat TEXT,
                    region TEXT,
                    diet TEXT,
                    audio_name TEXT,
                    audio_predicted_species TEXT,
                    audio_confidence REAL,
                    top3_json TEXT,
                    additional_info TEXT
                )
            """)
            conn.commit()

    def add_record(
        self,
        analysis_type: str,
        predicted_species: str,
        confidence: float,
        image_name: Optional[str] = None,
        description: Optional[str] = None,
        scientific_name: Optional[str] = None,
        family: Optional[str] = None,
        habitat: Optional[str] = None,
        region: Optional[str] = None,
        diet: Optional[str] = None,
        audio_name: Optional[str] = None,
        audio_predicted_species: Optional[str] = None,
        audio_confidence: Optional[float] = None,
        top3_list: Optional[List[Dict[str, Any]]] = None,
        additional_info: Optional[str] = None,
        analysis_date: Optional[str] = None
    ) -> int:
        if analysis_date is None:
            analysis_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        top3_json = json.dumps(top3_list) if top3_list is not None else "[]"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO analyses (
                    analysis_type,
                    image_name,
                    predicted_species,
                    confidence,
                    analysis_date,
                    description,
                    scientific_name,
                    family,
                    habitat,
                    region,
                    diet,
                    audio_name,
                    audio_predicted_species,
                    audio_confidence,
                    top3_json,
                    additional_info
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                analysis_type,
                image_name,
                predicted_species,
                confidence,
                analysis_date,
                description,
                scientific_name,
                family,
                habitat,
                region,
                diet,
                audio_name,
                audio_predicted_species,
                audio_confidence,
                top3_json,
                additional_info
            ))
            conn.commit()
            return cursor.lastrowid

    def get_all_records(self) -> List[Dict[str, Any]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM analyses ORDER BY id DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def search_by_name(self, query: str) -> List[Dict[str, Any]]:
        search_pattern = f"%{query.strip()}%"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM analyses
                WHERE predicted_species LIKE ?
                   OR description LIKE ?
                   OR scientific_name LIKE ?
                   OR audio_predicted_species LIKE ?
                ORDER BY id DESC
            """, (search_pattern, search_pattern, search_pattern, search_pattern))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def delete_record(self, record_id: int) -> bool:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM analyses WHERE id = ?", (record_id,))
            conn.commit()
            return cursor.rowcount > 0

    def filter_records(
        self,
        family: Optional[str] = None,
        habitat: Optional[str] = None,
        diet: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        query = "SELECT * FROM analyses WHERE 1=1"
        params = []
        if family:
            query += " AND family = ?"
            params.append(family)
        if habitat:
            query += " AND habitat LIKE ?"
            params.append(f"%{habitat}%")
        if diet:
            query += " AND diet LIKE ?"
            params.append(f"%{diet}%")
        query += " ORDER BY id DESC"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, tuple(params))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def get_statistics(self) -> Dict[str, Any]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM analyses")
            total_count = cursor.fetchone()[0]

            if total_count == 0:
                return {
                    "total_count": 0,
                    "most_frequent": [],
                    "highest_confidence": None,
                    "lowest_confidence": None,
                    "species_distribution": {}
                }

            cursor.execute("""
                SELECT predicted_species, COUNT(*) as freq
                FROM analyses
                GROUP BY predicted_species
                ORDER BY freq DESC
            """)
            species_freq = cursor.fetchall()
            most_frequent = [(row[0], row[1]) for row in species_freq[:5]]
            species_distribution = {row[0]: row[1] for row in species_freq}

            cursor.execute("SELECT * FROM analyses ORDER BY confidence DESC LIMIT 1")
            highest_row = cursor.fetchone()
            highest_confidence = dict(highest_row) if highest_row else None

            cursor.execute("SELECT * FROM analyses ORDER BY confidence ASC LIMIT 1")
            lowest_row = cursor.fetchone()
            lowest_confidence = dict(lowest_row) if lowest_row else None

            return {
                "total_count": total_count,
                "most_frequent": most_frequent,
                "highest_confidence": highest_confidence,
                "lowest_confidence": lowest_confidence,
                "species_distribution": species_distribution
            }
