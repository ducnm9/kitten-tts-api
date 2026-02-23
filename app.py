
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
import uuid
import os
import threading
import time


from kittentts import KittenTTS


app = FastAPI()

# List of available voices
AVAILABLE_VOICES = ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']


class Req(BaseModel):
    text: str
    voice: str = "Bella"

model = KittenTTS("KittenML/kitten-tts-nano-0.8-int8")  # tiny model


@app.post("/synthesize")
async def synthesize(req: Req):
    if not req.text:
        raise HTTPException(status_code=400, detail="Text is required")
    if req.voice not in AVAILABLE_VOICES:
        raise HTTPException(status_code=400, detail=f"Invalid voice. Please choose one of: {AVAILABLE_VOICES}")

    audio = model.generate(req.text, voice=req.voice)

    out_file = f"/tmp/{uuid.uuid4()}.wav"
    import soundfile as sf
    sf.write(out_file, audio, 24000)

    # Cleanup function to delete file after 15 minutes
    def cleanup_file(path):
        time.sleep(900)  # 15 minutes
        try:
            if os.path.exists(path):
                os.remove(path)
        except Exception:
            pass

    threading.Thread(target=cleanup_file, args=(out_file,), daemon=True).start()

    # Use uuid from filename for returned file
    file_uuid = os.path.basename(out_file).replace('.wav', '')
    return FileResponse(out_file, media_type="audio/wav", filename=f"output_{file_uuid}.wav")


# Endpoint to get available voices
@app.get("/voices")
async def get_voices():
    return {"available_voices": AVAILABLE_VOICES}