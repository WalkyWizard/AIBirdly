import asyncio
import uvicorn
import config
from services.vision_service import app as vision_app
from services.audio_service import app as audio_app
from services.info_service import app as info_app

app = vision_app

async def serve_all():
    c_vision = uvicorn.Config(vision_app, host=config.AI_VISION_HOST, port=config.AI_VISION_PORT, log_level="info")
    s_vision = uvicorn.Server(c_vision)

    c_audio = uvicorn.Config(audio_app, host=config.AI_AUDIO_HOST, port=config.AI_AUDIO_PORT, log_level="info")
    s_audio = uvicorn.Server(c_audio)

    c_info = uvicorn.Config(info_app, host=config.AI_INFO_HOST, port=config.AI_INFO_PORT, log_level="info")
    s_info = uvicorn.Server(c_info)

    await asyncio.gather(
        s_vision.serve(),
        s_audio.serve(),
        s_info.serve()
    )

if __name__ == "__main__":
    asyncio.run(serve_all())
