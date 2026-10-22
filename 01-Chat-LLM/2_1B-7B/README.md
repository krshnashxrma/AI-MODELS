# 1B - 7B (Lightweight Consumer GPU)

- **Category**: `01-Chat-LLM`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 8GB VRAM (or 8GB-16GB Unified RAM)`

---

## 🤖 Registered Models

### 🔹 SmolLM2-1.7B-Instruct
- **Organization / Creator**: Hugging Face
- **Parameter Count**: `1.7B`
- **Official Hugging Face / Source**: [SmolLM2-1.7B-Instruct on Hub](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High performance local conversational assistant on entry laptops.

---
### 🔹 Llama-3.2-1B / 3B-Instruct
- **Organization / Creator**: Meta
- **Parameter Count**: `1.23B / 3.21B`
- **Official Hugging Face / Source**: [Llama-3.2-1B / 3B-Instruct on Hub](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- **License**: `Llama 3.2 Community License`
- **AOMe Use Case**: Multilingual edge dialogue, tool calling, and summarization.

---
### 🔹 Qwen2.5-1.5B / 3B / 7B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `1.5B, 3.09B, 7.61B`
- **Official Hugging Face / Source**: [Qwen2.5-1.5B / 3B / 7B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Leading open-weight benchmark leader for conversational intelligence and function calling.

---
### 🔹 Gemma-2-2B-IT
- **Organization / Creator**: Google DeepMind
- **Parameter Count**: `2.61B`
- **Official Hugging Face / Source**: [Gemma-2-2B-IT on Hub](https://huggingface.co/google/gemma-2-2b-it)
- **License**: `Gemma Terms of Use`
- **AOMe Use Case**: Efficient factual reasoning and conversational safety.

---
### 🔹 Mistral-7B-Instruct-v0.3
- **Organization / Creator**: Mistral AI
- **Parameter Count**: `7.25B`
- **Official Hugging Face / Source**: [Mistral-7B-Instruct-v0.3 on Hub](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High-throughput general chatbot with function-calling support.

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
