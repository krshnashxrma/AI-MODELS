# 1B - 7B (Full Arrangement & High Fidelity Music)

- **Category**: `05-Music-Generation`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `8GB - 16GB VRAM`

---

## 🤖 Registered Models

### 🔹 MusicGen Medium & Melody
- **Organization / Creator**: Meta FAIR
- **Parameter Count**: `1.5B`
- **Official Hugging Face / Source**: [MusicGen Medium & Melody on Hub](https://huggingface.co/facebook/musicgen-melody)
- **License**: `MIT`
- **AOMe Use Case**: Conditioned music generation driven by humming, melody stems, and text prompts.

---
### 🔹 MusicGen Large
- **Organization / Creator**: Meta FAIR
- **Parameter Count**: `3.3B`
- **Official Hugging Face / Source**: [MusicGen Large on Hub](https://huggingface.co/facebook/musicgen-large)
- **License**: `MIT`
- **AOMe Use Case**: Studio quality complex harmonic structures, orchestral music, and electronic beats.

---
### 🔹 Stable Audio Open 1.0
- **Organization / Creator**: Stability AI
- **Parameter Count**: `1.2B (Diffusion Architecture)`
- **Official Hugging Face / Source**: [Stable Audio Open 1.0 on Hub](https://huggingface.co/stabilityai/stable-audio-open-1.0)
- **License**: `Stability Community License`
- **AOMe Use Case**: Variable-length high-fidelity sound effects, foley, and instrumental transitions.

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
