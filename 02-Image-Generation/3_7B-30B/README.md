# 7B - 30B (State-of-the-Art Flow Matching & Large DiT)

- **Category**: `02-Image-Generation`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `16GB - 24GB+ VRAM (or quantized FP8/GGUF on 12GB)`

---

## 🤖 Registered Models

### 🔹 FLUX.1-schnell / FLUX.1-dev
- **Organization / Creator**: Black Forest Labs
- **Parameter Count**: `12B (Flow Matching Transformer)`
- **Official Hugging Face / Source**: [FLUX.1-schnell / FLUX.1-dev on Hub](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- **License**: `FLUX.1-dev Non-Commercial / schnell Apache 2.0`
- **AOMe Use Case**: Highest fidelity text rendering, complex spatial compositions, and photorealism.

---
### 🔹 Stable Diffusion 3.5 Large
- **Organization / Creator**: Stability AI
- **Parameter Count**: `8.1B`
- **Official Hugging Face / Source**: [Stable Diffusion 3.5 Large on Hub](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
- **License**: `Stability Community License`
- **AOMe Use Case**: Flagship multimodal diffusion for commercial grade creative assets.

---
### 🔹 AuraFlow v0.3
- **Organization / Creator**: fal.ai
- **Parameter Count**: `6.8B (Open Flow-based DiT)`
- **Official Hugging Face / Source**: [AuraFlow v0.3 on Hub](https://huggingface.co/fal/AuraFlow-v0.3)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Fully open Apache-licensed high-parameter flow transformer.

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
