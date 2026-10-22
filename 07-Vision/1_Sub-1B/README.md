# Sub-1B (On-Device Vision Assistants)

- **Category**: `07-Vision`
- **Parameter Window**: `< 1 Billion Parameters (256M - 900M)`
- **Hardware Footprint**: `1GB - 2GB RAM / Edge NPU`

---

## 🤖 Registered Models

### 🔹 SmolVLM-256M / 500M
- **Organization / Creator**: Hugging Face
- **Parameter Count**: `256M / 500M`
- **Official Hugging Face / Source**: [SmolVLM-256M / 500M on Hub](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Ultra-lightweight edge visual description, video frame inspection, and mobile camera analysis.

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
