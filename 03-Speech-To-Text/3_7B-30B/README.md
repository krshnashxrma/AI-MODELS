# 7B - 30B (Multimodal Audio-LLM Unified Interpreters)

- **Category**: `03-Speech-To-Text`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `16GB - 32GB VRAM`

---

## 🤖 Registered Models

### 🔹 SALMONN / Qwen2-Audio-7B-Instruct
- **Organization / Creator**: Alibaba / Tsinghua
- **Parameter Count**: `7.6B - 13B`
- **Official Hugging Face / Source**: [SALMONN / Qwen2-Audio-7B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: End-to-end audio understanding: listens, transcribes, parses tone, and speaks back directly.

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
