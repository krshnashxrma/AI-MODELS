# 30B - 100B+ (Frontier Multimodal Foundations)

- **Category**: `07-Vision`
- **Parameter Window**: `30B to 90B Parameters`
- **Hardware Footprint**: `Multi-GPU Cluster (48GB - 80GB+)`

---

## 🤖 Registered Models

### 🔹 Qwen2-VL-72B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `72.1B`
- **Official Hugging Face / Source**: [Qwen2-VL-72B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2-VL-72B-Instruct)
- **License**: `Qwen Research License`
- **AOMe Use Case**: Open-weight multimodal frontier model rivaling proprietary GPT-4o on vision benchmarks.

---
### 🔹 Llama-3.2-90B-Vision-Instruct
- **Organization / Creator**: Meta
- **Parameter Count**: `89.2B`
- **Official Hugging Face / Source**: [Llama-3.2-90B-Vision-Instruct on Hub](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct)
- **License**: `Llama 3.2 Community License`
- **AOMe Use Case**: Enterprise grade multimodal reasoning, table extraction, and visual workflow automation.

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
