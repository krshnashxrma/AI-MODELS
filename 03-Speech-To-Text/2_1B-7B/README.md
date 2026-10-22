# 1B - 7B (Enterprise High-Accuracy ASR)

- **Category**: `03-Speech-To-Text`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 12GB VRAM`

---

## 🤖 Registered Models

### 🔹 Whisper Large-v3 & Large-v3-Turbo
- **Organization / Creator**: OpenAI
- **Parameter Count**: `1.55B (Large-v3) / 809M (Turbo)`
- **Official Hugging Face / Source**: [Whisper Large-v3 & Large-v3-Turbo on Hub](https://huggingface.co/openai/whisper-large-v3-turbo)
- **License**: `MIT`
- **AOMe Use Case**: Industry-standard accuracy for 100+ languages, timestamping, and translation.

---
### 🔹 SeamlessM4T-Medium
- **Organization / Creator**: Meta
- **Parameter Count**: `1.2B`
- **Official Hugging Face / Source**: [SeamlessM4T-Medium on Hub](https://huggingface.co/facebook/seamless-m4t-v2-large)
- **License**: `CC-BY-NC 4.0`
- **AOMe Use Case**: Unified speech-to-speech and speech-to-text translation across 100 languages.

---
### 🔹 NVIDIA Canary-1B
- **Organization / Creator**: NVIDIA
- **Parameter Count**: `1B`
- **Official Hugging Face / Source**: [NVIDIA Canary-1B on Hub](https://huggingface.co/nvidia/canary-1b)
- **License**: `CC-BY-4.0`
- **AOMe Use Case**: Top-ranked Hugging Face Open ASR leaderboard model for multi-accent English and European languages.

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
