import os
import tempfile
import requests
import gradio as gr
import scipy.io.wavfile
import gradio.themes.base as base

def voice_chat(audio):
    if audio is None:
        return None

    sr, audio_data = audio

    # Simpan audio sebagai .wav temporer
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        scipy.io.wavfile.write(tmpfile.name, sr, audio_data)
        audio_path = tmpfile.name

    # Kirim audio ke backend FastAPI
    with open(audio_path, "rb") as f:
        files = {"file": ("voice.wav", f, "audio/wav")}
        response = requests.post("http://localhost:8000/voice-chat", files=files)

    # Jika berhasil, simpan dan kembalikan file audio balasan
    if response.status_code == 200:
        output_audio_path = os.path.join(tempfile.gettempdir(), "tts_output.wav")
        with open(output_audio_path, "wb") as f:
            f.write(response.content)
        return output_audio_path
    else:
        return None

# Buat tema custom Gradio
custom_theme = base.Base(
    primary_hue="violet",      
    secondary_hue="purple",
    neutral_hue="slate"
).set(
    body_background_fill="#fdf4ff",              # latar belakang pastel ungu muda
    button_primary_background_fill="#9B7EBD",    # warna tombol submit (ungu pastel)
    button_primary_text_color="#ffffff",         # teks tombol putih
    block_title_text_color="#6b21a8"             # warna judul blok
)

# Buat antarmuka Gradio
with gr.Blocks(theme=custom_theme) as demo:
    gr.Markdown("# 🎙️ Voice Chatbot")
    gr.Markdown("Berbicara langsung ke mikrofon dan dapatkan jawaban suara dari asisten AI.")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources="microphone", type="numpy", label="🎤 Rekam Pertanyaan Anda")
            submit_btn = gr.Button("🔁 Submit")
        with gr.Column():
            audio_output = gr.Audio(type="filepath", label="🔊 Balasan dari Asisten")

    submit_btn.click(
        fn=voice_chat,
        inputs=audio_input,
        outputs=audio_output
    )

demo.launch()

