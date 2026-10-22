# Sub-1B (Ultra-Fast & Edge Voice Synthesizers)

- **Category**: `04-Text-To-Speech`
- **Parameter Window**: `< 1 Billion Parameters (15M - 380M)`
- **Hardware Footprint**: `CPU / Mobile / 1GB VRAM`

---

## 🤖 Registered Models

### 🔹 Piper TTS
- **Organization / Creator**: Rhasspy
- **Parameter Count**: `15M - 30M`
- **Official Hugging Face / Source**: [Piper TTS on Hub](https://github.com/rhasspy/piper)
- **License**: `MIT`
- **AOMe Use Case**: Instant, zero-latency local speech on Raspberry Pi and low-end laptops.

---
### 🔹 Kokoro-82M
- **Organization / Creator**: Hexgrad
- **Parameter Count**: `82M`
- **Official Hugging Face / Source**: [Kokoro-82M on Hub](https://huggingface.co/hexgrad/Kokoro-82M)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Unbelievable natural human inflection and audio fidelity under 100M parameters.

---
### 🔹 F5-TTS
- **Organization / Creator**: SWivid / F5 Team
- **Parameter Count**: `380M (Flow Matching)`
- **Official Hugging Face / Source**: [F5-TTS on Hub](https://huggingface.co/SWivid/F5-TTS)
- **License**: `MIT`
- **AOMe Use Case**: High-fidelity non-autoregressive voice cloning with a short 3-second reference audio.

---
### 🔹 MeloTTS
- **Organization / Creator**: MyShell.ai
- **Parameter Count**: `100M`
- **Official Hugging Face / Source**: [MeloTTS on Hub](https://huggingface.co/myshell-ai/MeloTTS-English)
- **License**: `MIT`
- **AOMe Use Case**: Real-time multilingual text-to-speech with precise accent control.

---
## 💡 Deployment Quickstart (No local file storage)

```python
# Streaming inference via Hugging Face Hub (zero disk bloat)
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "MODEL_ID_FROM_ABOVE"
# When ready to run on cloud server or high-memory instance:
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")
```
