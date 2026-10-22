# 1B - 7B (State-of-the-Art Dense & Multilingual Embeddings)

- **Category**: `06-Embeddings`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 16GB VRAM`

---

## 🤖 Registered Models

### 🔹 BGE-M3
- **Organization / Creator**: BAAI
- **Parameter Count**: `568M`
- **Official Hugging Face / Source**: [BGE-M3 on Hub](https://huggingface.co/BAAI/bge-m3)
- **License**: `MIT`
- **AOMe Use Case**: Multi-functionality (dense, sparse lexical, and multi-vector colBERT in one model) across 100+ languages.

---
### 🔹 E5-Mistral-7B-Instruct
- **Organization / Creator**: Microsoft
- **Parameter Count**: `7.1B`
- **Official Hugging Face / Source**: [E5-Mistral-7B-Instruct on Hub](https://huggingface.co/intfloat/e5-mistral-7b-instruct)
- **License**: `MIT`
- **AOMe Use Case**: LLM-powered embedding ranking at the very top of MTEB leaderboards.

---
### 🔹 NV-Embed-v2
- **Organization / Creator**: NVIDIA
- **Parameter Count**: `7B`
- **Official Hugging Face / Source**: [NV-Embed-v2 on Hub](https://huggingface.co/nvidia/NV-Embed-v2)
- **License**: `CC-BY-NC 4.0`
- **AOMe Use Case**: #1 ranked general embedding model on Massive Text Embedding Benchmark (MTEB).

---
### 🔹 Qwen2-7B-Embedding
- **Organization / Creator**: Alibaba
- **Parameter Count**: `7.6B`
- **Official Hugging Face / Source**: [Qwen2-7B-Embedding on Hub](https://huggingface.co/Alibaba-NLP/bge-multilingual-gemma2)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High-capacity multilingual and long-document dense semantic indexing.

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
