# 1B - 7B (High-Quality Consumer Diffusion)

- **Category**: `02-Image-Generation`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `6GB - 12GB VRAM`

---

## 🤖 Registered Models

### 🔹 Stable Diffusion XL (SDXL 1.0)
- **Organization / Creator**: Stability AI
- **Parameter Count**: `3.5B (Base) + 6.6B (Refiner pipeline)`
- **Official Hugging Face / Source**: [Stable Diffusion XL (SDXL 1.0) on Hub](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- **License**: `OpenRAIL++-M`
- **AOMe Use Case**: Standard high-resolution 1024x1024 artistic and photorealistic creation.

---
### 🔹 Stable Diffusion 3.5 Medium
- **Organization / Creator**: Stability AI
- **Parameter Count**: `2.5B (MMDiT Architecture)`
- **Official Hugging Face / Source**: [Stable Diffusion 3.5 Medium on Hub](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)
- **License**: `Stability Community License`
- **AOMe Use Case**: Typography rendering, prompt fidelity, and balance of speed and realism.

---
### 🔹 PixArt-Sigma
- **Organization / Creator**: PixArt-alpha team
- **Parameter Count**: `600M - 2B (DiT)`
- **Official Hugging Face / Source**: [PixArt-Sigma on Hub](https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS)
- **License**: `Apache 2.0`
- **AOMe Use Case**: 4K diffusion transformer with high photorealism and efficient compute.

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
