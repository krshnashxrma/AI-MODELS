# MoE & Frontier Coding Giants

- **Category**: `08-Code-Generation`
- **Parameter Window**: `Sparse Mixture-of-Experts (236B+ Parameters)`
- **Hardware Footprint**: `Distributed Server (Dual/Quad 80GB VRAM) or Cloud Endpoints`

---

## 🤖 Registered Models

### 🔹 DeepSeek-Coder-V2-Instruct
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `236B Total (21B Active per token) / Lite 16B (2.4B Active)`
- **Official Hugging Face / Source**: [DeepSeek-Coder-V2-Instruct on Hub](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct)
- **License**: `DeepSeek Open Model License (Commercial allowed)`
- **AOMe Use Case**: World's most capable open-source MoE coder, supporting 338 programming languages with 128k context.

---
### 🔹 DeepSeek-V3 / R1 (Coding & Algorithmic Specialization)
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `671B Total (37B Active per token)`
- **Official Hugging Face / Source**: [DeepSeek-V3 / R1 (Coding & Algorithmic Specialization) on Hub](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- **License**: `MIT`
- **AOMe Use Case**: Elite algorithmic reasoning, complex competitive programming, and automated software engineering.

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
