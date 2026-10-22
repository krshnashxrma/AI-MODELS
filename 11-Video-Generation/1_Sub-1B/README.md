# Sub-1B (Fast Motion Modules)

- **Category**: `11-Video-Generation`
- **Parameter Window**: `< 1 Billion Parameters`
- **Hardware Footprint**: `4GB - 6GB VRAM`

---

## 🤖 Registered Models

### 🔹 AnimateDiff-SD1.5
- **Organization / Creator**: AnimateDiff
- **Parameter Count**: `400M motion adapter`
- **Official Hugging Face / Source**: [AnimateDiff-SD1.5 on Hub](https://huggingface.co/guoyww/animatediff-motion-adapter-v1-5-2)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Fast lightweight camera motion and dynamic video generation on consumer PCs.

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
