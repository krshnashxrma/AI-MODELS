# Sub-1B (Fast / Lightweight Generators)

- **Category**: `02-Image-Generation`
- **Parameter Window**: `< 1 Billion Parameters`
- **Hardware Footprint**: `2GB - 4GB VRAM`

---

## 🤖 Registered Models

### 🔹 Stable Diffusion v1.5
- **Organization / Creator**: RunwayML / Stability AI
- **Parameter Count**: `~860M (UNet + Text Encoder)`
- **Official Hugging Face / Source**: [Stable Diffusion v1.5 on Hub](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- **License**: `CreativeML OpenRAIL-M`
- **AOMe Use Case**: Instant low-latency generation, massive ecosystem of LoRAs and ControlNets.

---
### 🔹 Tiny-SD / SD-Turbo
- **Organization / Creator**: Segmind / Stability AI
- **Parameter Count**: `200M - 800M (1-step inference)`
- **Official Hugging Face / Source**: [Tiny-SD / SD-Turbo on Hub](https://huggingface.co/stabilityai/sd-turbo)
- **License**: `OpenRAIL-M`
- **AOMe Use Case**: Real-time generation in canvas and responsive UI editing.

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
