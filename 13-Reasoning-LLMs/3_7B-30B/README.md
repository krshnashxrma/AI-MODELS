# 7B - 30B (Deep Thinking & STEM Giants)

- **Category**: `13-Reasoning-LLMs`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `16GB - 24GB VRAM`

---

## 🤖 Registered Models

### 🔹 QwQ-32B-Preview
- **Organization / Creator**: Qwen team
- **Parameter Count**: `32.5B`
- **Official Hugging Face / Source**: [QwQ-32B-Preview on Hub](https://huggingface.co/Qwen/QwQ-32B-Preview)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Exceptional mathematical and competitive coding capabilities rivaling frontier models.

---
### 🔹 DeepSeek-R1-Distill-Qwen-32B
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `32.5B`
- **Official Hugging Face / Source**: [DeepSeek-R1-Distill-Qwen-32B on Hub](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)
- **License**: `MIT`
- **AOMe Use Case**: Elite chain-of-thought logic engine suitable for workstation deployment.

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
