# 7B - 30B (State-of-the-Art Video DiT)

- **Category**: `11-Video-Generation`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `24GB - 80GB VRAM`

---

## 🤖 Registered Models

### 🔹 HunyuanVideo
- **Organization / Creator**: Tencent
- **Parameter Count**: `13B (Open-Source Video SOTA)`
- **Official Hugging Face / Source**: [HunyuanVideo on Hub](https://huggingface.co/tencent/HunyuanVideo)
- **License**: `Tencent Hunyuan Community License`
- **AOMe Use Case**: High-definition 1080p photorealistic text-to-video matching proprietary models like Runway Gen-3.

---
### 🔹 Mochi-1
- **Organization / Creator**: Genmo
- **Parameter Count**: `10B (Asymmetric Diffusion Transformer)`
- **Official Hugging Face / Source**: [Mochi-1 on Hub](https://huggingface.co/genmo/mochi-1-preview)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High prompt adherence and physical motion realism at 30 fps.

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
