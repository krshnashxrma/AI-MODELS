# 7B - 30B (Full-Stack Component Architectures)

- **Category**: `10-HTML-And-Web-Generation`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `12GB - 24GB VRAM`

---

## 🤖 Registered Models

### 🔹 Qwen2.5-Coder-32B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `32.5B`
- **Official Hugging Face / Source**: [Qwen2.5-Coder-32B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Generates complex responsive web applications, multi-component React/Next.js/Tailwind suites, and WebSockets.

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
