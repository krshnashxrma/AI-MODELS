# 7B - 30B (Next-Gen Flow Matching Anime)

- **Category**: `09-Anime-And-Manga-AI`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `16GB - 24GB VRAM`

---

## 🤖 Registered Models

### 🔹 Illustrious-XL / Flux-Anime-LoRA
- **Organization / Creator**: OnomaAI / Black Forest Labs
- **Parameter Count**: `12B (FLUX.1 backbone with anime distillation)`
- **Official Hugging Face / Source**: [Illustrious-XL / Flux-Anime-LoRA on Hub](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- **License**: `Non-commercial / Research`
- **AOMe Use Case**: Photorealistic 2D anime scenes with complex perspective, detailed hand gestures, and fine lines.

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
