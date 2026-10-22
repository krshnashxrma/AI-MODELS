# Sub-1B (Micro Reasoning Agents)

- **Category**: `13-Reasoning-LLMs`
- **Parameter Window**: `< 1 Billion Parameters`
- **Hardware Footprint**: `1GB RAM / Mobile`

---

## 🤖 Registered Models

### 🔹 SmolLM2-360M-Reasoning
- **Organization / Creator**: Hugging Face
- **Parameter Count**: `360M`
- **Official Hugging Face / Source**: [SmolLM2-360M-Reasoning on Hub](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Step-by-step logic and classification on edge devices without GPU.

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
