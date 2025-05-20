# Voice Chatbot UAS – STT, Gemini LLM, TTS Integration

Proyek UAS ini merupakan aplikasi chatbot berbasis suara yang memungkinkan pengguna berbicara langsung melalui antarmuka web. Sistem akan mengenali suara pengguna, mengubahnya menjadi teks (Speech-to-Text), memprosesnya menggunakan model bahasa besar (Gemini API), lalu mengubah hasil jawabannya kembali menjadi suara (Text-to-Speech).

## 📌 Fitur Utama
- 🎙️ Speech-to-Text (STT) menggunakan `whisper.cpp` dari OpenAI.
- 🧠 LLM Integration menggunakan Google Gemini API untuk menghasilkan respons dalam Bahasa Indonesia.
- 🔊 Text-to-Speech (TTS) menggunakan model Coqui TTS (Indonesian TTS).
- 🧪 Antarmuka pengguna interaktif berbasis `Gradio` untuk pengujian langsung dari browser.

## 🗂️ Struktur Proyek
```
voice_chatbot_project/
│
├── app/
│   ├── main.py            # Endpoint utama FastAPI
│   ├── llm.py             # Integrasi Gemini API
│   ├── stt.py             # Transkripsi suara (whisper.cpp)
│   ├── tts.py             # TTS dengan Coqui
│   └── whisper.cpp/       # Hasil clone whisper.cpp
│   └── coqui_utils/       # Model dan config Coqui TTS
│
├── gradio_app/
│   └── app.py             # Frontend dengan Gradio
│
├── .env                   # Menyimpan Gemini API Key
├── requirements.txt       # Daftar dependensi Python
```

## 📋 Prasyarat
Pastikan Anda telah menginstal komponen berikut sebelum menjalankan proyek:
- Python **versi 3.9** atau lebih baru  
- **Whisper.cpp** (beserta model `ggml-large-v3-turbo.bin`)  
- **Coqui TTS** (beserta model Bahasa Indonesia) 

## 📚 Catatan Penggunaan
- Semua file audio menggunakan format `.wav`.
- Untuk menghasilkan fonem seperti `dəˈnɡan`, teks dari Gemini harus dikonversi ke fonetik.
- Disarankan menggunakan model Whisper: `ggml-large-v3-turbo`.
- Gunakan speaker: `wibowo` dari model Coqui v1.2.

## 🚀 Langkah Instalasi

### 1. Clone Repositori

```bash
git clone https://github.com/meutiaaini/2208107010005_MeutiaAini_UAS_NLP.git
cd 2208107010005_MeutiaAini_UAS_NLP
```

### 2. Instal Dependensi Python
```
pip install -r requirements.txt
```

### 3. Clone dan Kompilasi whisper.cpp
```
cd app
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
make
cd ..
```

### 4. Unduh Model Whisper
```
mkdir -p whisper.cpp/models
cd whisper.cpp/models
wget https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin
cd ../..
```

### 5. Siapkan Model Coqui TTS
```
mkdir -p coqui_utils
```

### 6. Konfigurasi API Key Gemini
```
cp .env.example .env
```

Edit file .env menggunakan editor teks, lalu tambahkan API Key Gemini Anda:
```
GEMINI_API_KEY=your_api_key_here
```

## 🖥️ Menjalankan Aplikasi
### 1. Jalankan Backend FastAPI
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Jalankan Frontend Gradio (di terminal baru)
```
cd gradio_app
python app.py
```

## 🙋‍♀️ Tentang
- Nama: Meutia Aini
- NIM: 2208107010005
- Mata Kuliah: Praktikum Pemrosesan Bahasa Alami

## 👨‍💻 Dibuat Untuk
Proyek UAS mata kuliah *Pemrosesan Bahasa Alami* — Semester Genap 2024/2025.

## Link Video YouTube
https://youtu.be/8qvz9XF8RPQ

## Link Postingan LinkedIn
https://www.linkedin.com/posts/meutia-aini-17121931b_naturallanguageprocessing-speechtotext-texttospeech-activity-7330119314584272896-wAeN?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFEDFqUBVR5cxWTIShRHIwXIgxT3EzSlAWY
