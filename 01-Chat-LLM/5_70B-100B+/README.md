# 70B - 100B+ (Data Center Dense Models)

- **Category**: `01-Chat-LLM`
- **Parameter Window**: `70B to 405B Parameters (Dense)`
- **Hardware Footprint**: `Multi-GPU Cluster (4x-8x H100 80GB)`

---

## 🤖 Registered Models

### 🔹 Llama-3.1-405B-Instruct
- **Organization / Creator**: Meta
- **Parameter Count**: `405B (Dense)`
- **Official Hugging Face / Source**: [Llama-3.1-405B-Instruct on Hub](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct)
- **License**: `Llama 3.1 Community License`
- **AOMe Use Case**: Frontier flagship dense model for synthetic data generation and distillation.

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
