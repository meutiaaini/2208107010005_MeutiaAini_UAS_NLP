from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import traceback
import uvicorn

# Import fungsi dari modul lain
from app.stt import transcribe_speech_to_text
from app.llm import generate_response
from app.tts import transcribe_text_to_speech

app = FastAPI()

# Mengizinkan akses dari frontend (contoh: Gradio) ke backend ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bebas diakses dari domain mana pun
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/voice-chat")
async def voice_chat(file: UploadFile = File(...)):
    """
    Endpoint utama untuk menerima file audio dari pengguna,
    mengubah audio menjadi teks (STT), memprosesnya melalui LLM,
    dan mengembalikan hasil respons dalam bentuk audio (TTS).
    """
    try:
        print(f"[INFO] File diterima: {file.filename}")

        # Membaca data audio dari file yang diunggah
        audio_bytes = await file.read()
        ext = os.path.splitext(file.filename)[-1].lower()

        # Validasi format file audio yang didukung
        if ext not in ['.wav', '.mp3', '.m4a']:
            raise HTTPException(status_code=400, detail="Jenis file tidak didukung.")

        # Proses Speech-to-Text (STT)
        text = transcribe_speech_to_text(audio_bytes, file_ext=ext)
        if text.startswith("[ERROR]"):
            raise HTTPException(status_code=500, detail=text)

        print(f"[INFO] Hasil transkripsi: {text.strip()}")

        # Kirim teks ke LLM untuk menghasilkan respons
        response = generate_response(text.strip())
        if response.startswith("[ERROR]"):
            raise HTTPException(status_code=500, detail=response)

        print(f"[INFO] Respons dari model: {response.strip()}")

        # Ubah teks respons menjadi audio melalui TTS
        audio_path = transcribe_text_to_speech(response.strip())
        if audio_path.startswith("[ERROR]"):
            raise HTTPException(status_code=500, detail=audio_path)

        # Kirimkan file audio hasil sebagai respons ke frontend
        return FileResponse(audio_path, media_type="audio/wav", filename="response.wav")

    except Exception as e:
        print("[EXCEPTION]", traceback.format_exc())
        raise HTTPException(status_code=500, detail="Terjadi kesalahan di server.")

# Menjalankan server jika file ini dijalankan langsung
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)