import csv
from pathlib import Path
from typing import List, Dict, Any, Optional
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import config

def export_to_csv(records: List[Dict[str, Any]], export_path: Optional[Path] = None) -> Path:
    target_path = Path(export_path) if export_path is not None else config.CSV_EXPORT_PATH

    fieldnames = [
        "image_name",
        "predicted_species",
        "confidence",
        "analysis_date",
        "description",
        "scientific_name",
        "family",
        "audio_name",
        "audio_predicted_species",
        "audio_confidence"
    ]

    with open(target_path, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";", extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({
                "image_name": record.get("image_name") or "",
                "predicted_species": record.get("predicted_species") or "",
                "confidence": record.get("confidence") or 0.0,
                "analysis_date": record.get("analysis_date") or "",
                "description": record.get("description") or "",
                "scientific_name": record.get("scientific_name") or "",
                "family": record.get("family") or "",
                "audio_name": record.get("audio_name") or "",
                "audio_predicted_species": record.get("audio_predicted_species") or "",
                "audio_confidence": record.get("audio_confidence") or 0.0
            })

    return target_path

def compute_statistics(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not records:
        return {
            "total_analyzed": 0,
            "most_frequent_species": [],
            "highest_confidence": None,
            "lowest_confidence": None,
            "species_counts": {}
        }

    species_counts: Dict[str, int] = {}
    valid_conf_records = []

    for r in records:
        species = r.get("predicted_species")
        if species:
            species_counts[species] = species_counts.get(species, 0) + 1

        conf = r.get("confidence")
        if conf is not None:
            try:
                valid_conf_records.append((float(conf), r))
            except (ValueError, TypeError):
                pass

    sorted_species = sorted(species_counts.items(), key=lambda item: item[1], reverse=True)
    valid_conf_records.sort(key=lambda item: item[0], reverse=True)

    highest = valid_conf_records[0][1] if valid_conf_records else None
    lowest = valid_conf_records[-1][1] if valid_conf_records else None

    return {
        "total_analyzed": len(records),
        "most_frequent_species": sorted_species[:5],
        "highest_confidence": highest,
        "lowest_confidence": lowest,
        "species_counts": species_counts
    }

def generate_distribution_chart(records: List[Dict[str, Any]], output_path: Optional[Path] = None) -> Path:
    target_path = Path(output_path) if output_path is not None else config.STATS_PLOT_PATH

    stats = compute_statistics(records)
    species_counts = stats["species_counts"]

    if not species_counts:
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.text(0.5, 0.5, "Немає даних для побудови графіка", ha="center", va="center")
        ax.axis("off")
        plt.tight_layout()
        fig.savefig(target_path, dpi=120)
        plt.close(fig)
        return target_path

    top_items = sorted(species_counts.items(), key=lambda x: x[1], reverse=True)[:8]
    names = [item[0] for item in top_items]
    counts = [item[1] for item in top_items]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(names, counts, color="steelblue", edgecolor="midnightblue")
    ax.invert_yaxis()
    ax.set_xlabel("Кількість виявлень")
    ax.set_title("Розподіл найчастіше визначених видів птахів")
    ax.grid(axis="x", linestyle="--", alpha=0.7)

    for bar in bars:
        width = bar.get_width()
        ax.annotate(f"{int(width)}",
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha="left", va="center")

    plt.tight_layout()
    fig.savefig(target_path, dpi=150)
    plt.close(fig)
    return target_path
