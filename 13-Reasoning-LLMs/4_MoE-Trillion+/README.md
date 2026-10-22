# MoE Frontier Thinking Titans

- **Category**: `13-Reasoning-LLMs`
- **Parameter Window**: `671B MoE Parameters`
- **Hardware Footprint**: `Distributed Cloud Cluster`

---

## 🤖 Registered Models

### 🔹 DeepSeek-R1 (Full 671B MoE)
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `671B MoE (37B active)`
- **Official Hugging Face / Source**: [DeepSeek-R1 (Full 671B MoE) on Hub](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- **License**: `MIT`
- **AOMe Use Case**: World-leading open-source reasoning model, rivaling OpenAI o1 on Olympiad math, SWE-bench, and reasoning.

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
