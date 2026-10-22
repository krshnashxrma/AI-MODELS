# MoE Multimodal Architectures

- **Category**: `07-Vision`
- **Parameter Window**: `Sparse Mixture-of-Experts Vision Models`
- **Hardware Footprint**: `Distributed Cloud Infrastructure`

---

## 🤖 Registered Models

### 🔹 DeepSeek-VL2
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `MoE Vision-Language (Dynamic Sparse Experts)`
- **Official Hugging Face / Source**: [DeepSeek-VL2 on Hub](https://huggingface.co/deepseek-ai/deepseek-vl2)
- **License**: `MIT`
- **AOMe Use Case**: High-throughput sparse multimodal understanding for massive document batches.

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
