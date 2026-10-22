# 7B - 30B (Senior Engineering Co-Pilots)

- **Category**: `08-Code-Generation`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `12GB - 24GB VRAM`

---

## 🤖 Registered Models

### 🔹 Qwen2.5-Coder-14B / 32B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `14.7B / 32.5B (128k context)`
- **Official Hugging Face / Source**: [Qwen2.5-Coder-14B / 32B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: State-of-the-art coding intelligence beating proprietary models (GPT-4o level) on EvalPlus & SWE-bench.

---
### 🔹 StarCoder2-15B
- **Organization / Creator**: BigCode
- **Parameter Count**: `15B`
- **Official Hugging Face / Source**: [StarCoder2-15B on Hub](https://huggingface.co/bigcode/starcoder2-15b)
- **License**: `OpenRAIL-M v1`
- **AOMe Use Case**: Enterprise code base maintenance, refactoring, and multi-file code understanding.

---
### 🔹 CodeLlama-34B-Instruct
- **Organization / Creator**: Meta
- **Parameter Count**: `34B`
- **Official Hugging Face / Source**: [CodeLlama-34B-Instruct on Hub](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf)
- **License**: `Llama 2 Community License`
- **AOMe Use Case**: Infill fill-in-the-middle support and Python / C++ deep reasoning.

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
