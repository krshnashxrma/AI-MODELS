# Sub-1B (Lightweight & High-Throughput Embeddings)

- **Category**: `06-Embeddings`
- **Parameter Window**: `< 1 Billion Parameters (22M - 335M)`
- **Hardware Footprint**: `CPU or 1GB VRAM (Millions of tokens/sec)`

---

## 🤖 Registered Models

### 🔹 all-MiniLM-L6-v2
- **Organization / Creator**: Sentence Transformers
- **Parameter Count**: `22.7M (384 dims)`
- **Official Hugging Face / Source**: [all-MiniLM-L6-v2 on Hub](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Ultra-lightweight vector embedding for mobile apps and instant offline lookup.

---
### 🔹 BGE-small / base / large-en-v1.5
- **Organization / Creator**: BAAI
- **Parameter Count**: `33M (Small), 109M (Base), 335M (Large)`
- **Official Hugging Face / Source**: [BGE-small / base / large-en-v1.5 on Hub](https://huggingface.co/BAAI/bge-large-en-v1.5)
- **License**: `MIT`
- **AOMe Use Case**: Proven standard for production RAG pipelines on standard consumer hardware.

---
### 🔹 E5-small / base / large-v2
- **Organization / Creator**: Microsoft
- **Parameter Count**: `33M - 335M`
- **Official Hugging Face / Source**: [E5-small / base / large-v2 on Hub](https://huggingface.co/intfloat/e5-large-v2)
- **License**: `MIT`
- **AOMe Use Case**: High-accuracy asymmetric search (query vs document retrieval).

---
### 🔹 ModernBERT-base / large
- **Organization / Creator**: Answer.AI & LightOn
- **Parameter Count**: `149M / 395M (8k native context)`
- **Official Hugging Face / Source**: [ModernBERT-base / large on Hub](https://huggingface.co/answerdotai/ModernBERT-large)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Modern drop-in BERT replacement with Rotary Embeddings and 8192 token context.

---
### 🔹 Nomic-Embed-Text-v1.5
- **Organization / Creator**: Nomic AI
- **Parameter Count**: `137M (Matryoshka Embeddings)`
- **Official Hugging Face / Source**: [Nomic-Embed-Text-v1.5 on Hub](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Dynamic embedding truncation (flexible 64 to 768 dimensions) with 8k context.

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
