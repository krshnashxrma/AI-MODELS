# 30B - 100B+ (Unified Multimodal Generation)

- **Category**: `02-Image-Generation`
- **Parameter Window**: `30B+ Parameters`
- **Hardware Footprint**: `Multi-GPU Server (48GB - 80GB+)`

---

## 🤖 Registered Models

### 🔹 OmniGen-v1
- **Organization / Creator**: VectorSpaceLab
- **Parameter Count**: `Unified Transformer (3.8B - scalable multimodal backbone)`
- **Official Hugging Face / Source**: [OmniGen-v1 on Hub](https://huggingface.co/Shitao/OmniGen-v1)
- **License**: `MIT`
- **AOMe Use Case**: All-in-one image generation, inpainting, style transfer, and subject-driven generation.

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
