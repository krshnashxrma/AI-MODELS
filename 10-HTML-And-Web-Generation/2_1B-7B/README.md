# 1B - 7B (Interactive Frontend & Tailwind Coders)

- **Category**: `10-HTML-And-Web-Generation`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 8GB VRAM`

---

## 🤖 Registered Models

### 🔹 Design2Code-1.5B / 7B
- **Organization / Creator**: SALT Lab (Stanford)
- **Parameter Count**: `1.5B / 7B`
- **Official Hugging Face / Source**: [Design2Code-1.5B / 7B on Hub](https://huggingface.co/SALT-NLP/Design2Code-hf)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Benchmark leader for converting visual webpage screenshots into production-ready responsive HTML/CSS.

---
### 🔹 Qwen2.5-Coder-7B (Frontend Web Specialization)
- **Organization / Creator**: Qwen team
- **Parameter Count**: `7.6B`
- **Official Hugging Face / Source**: [Qwen2.5-Coder-7B (Frontend Web Specialization) on Hub](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Generates complete single-file HTML apps with modern CSS Grid, Flexbox, Canvas animations, and JS logic.

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
