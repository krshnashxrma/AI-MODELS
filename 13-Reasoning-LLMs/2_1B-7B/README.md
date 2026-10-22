# 1B - 7B (Lightweight Thinking Models)

- **Category**: `13-Reasoning-LLMs`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 8GB VRAM`

---

## 🤖 Registered Models

### 🔹 DeepSeek-R1-Distill-Qwen-1.5B / 7B
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `1.5B / 7.6B`
- **Official Hugging Face / Source**: [DeepSeek-R1-Distill-Qwen-1.5B / 7B on Hub](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)
- **License**: `MIT`
- **AOMe Use Case**: Reinforcement-learning-driven step-by-step reasoning beating OpenAI o1-mini on MATH-500.

---
### 🔹 Marco-o1-7B
- **Organization / Creator**: Alibaba
- **Parameter Count**: `7B (MCTS + Fine-Grained CoT)`
- **Official Hugging Face / Source**: [Marco-o1-7B on Hub](https://huggingface.co/AIDC-AI/Marco-o1)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Monte Carlo Tree Search driven deep reasoning for complex decision making.

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
