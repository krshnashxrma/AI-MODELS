# 1B - 7B (Cinematic Text-to-Video)

- **Category**: `11-Video-Generation`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `8GB - 16GB VRAM`

---

## 🤖 Registered Models

### 🔹 Stable Video Diffusion (SVD-XT)
- **Organization / Creator**: Stability AI
- **Parameter Count**: `1.5B`
- **Official Hugging Face / Source**: [Stable Video Diffusion (SVD-XT) on Hub](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt-1-1)
- **License**: `Stability Community License`
- **AOMe Use Case**: Image-to-video motion generation with 25 dynamic frames at 1024x576.

---
### 🔹 CogVideoX-2B / 5B
- **Organization / Creator**: THUDM / Zhipu AI
- **Parameter Count**: `2B / 5B (3D VAE + Expert Transformer)`
- **Official Hugging Face / Source**: [CogVideoX-2B / 5B on Hub](https://huggingface.co/THUDM/CogVideoX-5b)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Full text-to-video generation with exceptional temporal consistency and fluid motion.

---
### 🔹 LTX-Video
- **Organization / Creator**: Lightricks
- **Parameter Count**: `2B (Real-time 24fps DiT)`
- **Official Hugging Face / Source**: [LTX-Video on Hub](https://huggingface.co/Lightricks/LTX-Video)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Ultra-fast high-resolution video generation optimized for local workstation execution.

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
