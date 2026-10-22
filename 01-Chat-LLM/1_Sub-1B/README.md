# Sub-1B (Edge & Mobile)

- **Category**: `01-Chat-LLM`
- **Parameter Window**: `< 1 Billion Parameters (100M - 999M)`
- **Hardware Footprint**: `1GB - 2GB RAM / CPU or Mobile NPU`

---

## 🤖 Registered Models

### 🔹 SmolLM2-135M / 360M
- **Organization / Creator**: Hugging Face
- **Parameter Count**: `135M / 360M`
- **Official Hugging Face / Source**: [SmolLM2-135M / 360M on Hub](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Ultra-lightweight mobile assistant and background intent classification.

---
### 🔹 Qwen2.5-0.5B-Instruct
- **Organization / Creator**: Alibaba Cloud / Qwen team
- **Parameter Count**: `490M`
- **Official Hugging Face / Source**: [Qwen2.5-0.5B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Fast edge reasoning, simple QA, and micro-agent routing without GPU.

---
### 🔹 H2O-Danube3-500M
- **Organization / Creator**: H2O.ai
- **Parameter Count**: `500M`
- **Official Hugging Face / Source**: [H2O-Danube3-500M on Hub](https://huggingface.co/h2oai/h2o-danube3-500m-chat)
- **License**: `Apache 2.0`
- **AOMe Use Case**: On-device private chat and offline document queries.

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
