# 30B - 70B (High-Performance Enterprise)

- **Category**: `01-Chat-LLM`
- **Parameter Window**: `30B to 70B Parameters`
- **Hardware Footprint**: `32GB - 80GB VRAM (Dual 3090/4090 or A100/H100 / Mac Studio)`

---

## 🤖 Registered Models

### 🔹 Llama-3.3-70B-Instruct
- **Organization / Creator**: Meta
- **Parameter Count**: `70.6B`
- **Official Hugging Face / Source**: [Llama-3.3-70B-Instruct on Hub](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)
- **License**: `Llama 3.3 Community License`
- **AOMe Use Case**: State-of-the-art open-source general reasoning and autonomous agent brain.

---
### 🔹 Qwen2.5-72B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `72.7B`
- **Official Hugging Face / Source**: [Qwen2.5-72B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- **License**: `Qwen Research License`
- **AOMe Use Case**: Top open-weight LLM for complex STEM, multi-turn dialog, and coding.

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
