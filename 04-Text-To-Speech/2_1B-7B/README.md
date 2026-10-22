# 1B - 7B (Studio Quality & Expressive Voice)

- **Category**: `04-Text-To-Speech`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 12GB VRAM`

---

## 🤖 Registered Models

### 🔹 CosyVoice / CosyVoice-2
- **Organization / Creator**: FunAudioLLM / Alibaba
- **Parameter Count**: `1B - 3B`
- **Official Hugging Face / Source**: [CosyVoice / CosyVoice-2 on Hub](https://huggingface.co/FunAudioLLM/CosyVoice-300M)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Multi-lingual emotional voice synthesis with fine-grained control over laughter, breaths, and pitch.

---
### 🔹 XTTS-v2
- **Organization / Creator**: Coqui AI
- **Parameter Count**: `1.2B`
- **Official Hugging Face / Source**: [XTTS-v2 on Hub](https://huggingface.co/coqui/XTTS-v2)
- **License**: `Coqui Public Model License`
- **AOMe Use Case**: Real-time voice cloning in 17 languages with single audio snippet.

---
### 🔹 ChatTTS
- **Organization / Creator**: 2noise
- **Parameter Count**: `~1B`
- **Official Hugging Face / Source**: [ChatTTS on Hub](https://huggingface.co/2noise/ChatTTS)
- **License**: `CC-BY-NC-4.0`
- **AOMe Use Case**: Conversational TTS designed explicitly for chatbot dialogue with natural interjections.

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
