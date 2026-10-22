# 1B - 7B (Lightweight Developer Workstation)

- **Category**: `08-Code-Generation`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 8GB VRAM`

---

## 🤖 Registered Models

### 🔹 Qwen2.5-Coder-1.5B / 3B / 7B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `1.5B, 3.1B, 7.6B`
- **Official Hugging Face / Source**: [Qwen2.5-Coder-1.5B / 3B / 7B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Benchmark champion for open-source code generation, repository awareness, and unit testing.

---
### 🔹 StarCoder2-3B / 7B
- **Organization / Creator**: BigCode / ServiceNow / Hugging Face
- **Parameter Count**: `3B / 7B`
- **Official Hugging Face / Source**: [StarCoder2-3B / 7B on Hub](https://huggingface.co/bigcode/starcoder2-7b)
- **License**: `OpenRAIL-M v1`
- **AOMe Use Case**: Permissively licensed code generation trained on 600+ programming languages.

---
### 🔹 DeepSeek-Coder-6.7B-Instruct
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `6.7B`
- **Official Hugging Face / Source**: [DeepSeek-Coder-6.7B-Instruct on Hub](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct)
- **License**: `DeepSeek Model License`
- **AOMe Use Case**: Proven workhorse for project-level coding, debugging, and git commits.

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
