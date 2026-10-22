# MoE & Trillion-Scale Architectures

- **Category**: `01-Chat-LLM`
- **Parameter Window**: `Sparse Mixture-of-Experts (Hundreds of Billions to Trillions)`
- **Hardware Footprint**: `Distributed Cloud Inference (vLLM / SGLang / TensorRT-LLM)`

---

## 🤖 Registered Models

### 🔹 DeepSeek-V3
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `671B Total (37B Active per token)`
- **Official Hugging Face / Source**: [DeepSeek-V3 on Hub](https://huggingface.co/deepseek-ai/DeepSeek-V3)
- **License**: `DeepSeek Open Model License (commercial allowed)`
- **AOMe Use Case**: Unmatched cost-to-performance frontier reasoning MoE with Multi-head Latent Attention.

---
### 🔹 DeepSeek-R1
- **Organization / Creator**: DeepSeek AI
- **Parameter Count**: `671B Total (37B Active) + Distilled Variants (1.5B - 70B)`
- **Official Hugging Face / Source**: [DeepSeek-R1 on Hub](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- **License**: `MIT`
- **AOMe Use Case**: Frontier chain-of-thought reasoning rivaling OpenAI o1.

---
### 🔹 Grok-1
- **Organization / Creator**: xAI
- **Parameter Count**: `314B MoE (86B Active per token)`
- **Official Hugging Face / Source**: [Grok-1 on Hub](https://huggingface.co/xai-org/grok-1)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Open base weights for massive scale conversational research.

---
### 🔹 Switch Transformers (Switch-C 1.6T)
- **Organization / Creator**: Google Research
- **Parameter Count**: `1.6 Trillion Parameters (Sparse MoE)`
- **Official Hugging Face / Source**: [Switch Transformers (Switch-C 1.6T) on Hub](https://huggingface.co/google/switch-c-2048)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Pioneering trillion-parameter sparse MoE research model.

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
