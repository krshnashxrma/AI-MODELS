# 7B - 30B (Workstation & Mid-Range)

- **Category**: `01-Chat-LLM`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `12GB - 24GB VRAM (RTX 3060/4070/4090 or Apple M-series)`

---

## 🤖 Registered Models

### 🔹 Gemma-2-9B-IT / 27B-IT
- **Organization / Creator**: Google DeepMind
- **Parameter Count**: `9.24B / 27.2B`
- **Official Hugging Face / Source**: [Gemma-2-9B-IT / 27B-IT on Hub](https://huggingface.co/google/gemma-2-27b-it)
- **License**: `Gemma Terms of Use`
- **AOMe Use Case**: Near frontier-level logic, nuanced text generation, and deep analysis.

---
### 🔹 Mistral-NeMo-Instruct-2407
- **Organization / Creator**: Mistral AI & NVIDIA
- **Parameter Count**: `12.2B`
- **Official Hugging Face / Source**: [Mistral-NeMo-Instruct-2407 on Hub](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)
- **License**: `Apache 2.0`
- **AOMe Use Case**: 128k context window assistant for long document synthesis.

---
### 🔹 Qwen2.5-14B / 32B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `14.7B / 32.5B`
- **Official Hugging Face / Source**: [Qwen2.5-14B / 32B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Powerful conversational agents rivaling previous 70B generation.

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
