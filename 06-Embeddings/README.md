# Text & Multimodal Embeddings (RAG & Semantic Search)

## 📌 Niche Overview
- **AOMe Role**: Retrieval-Augmented Generation (RAG), vector databases, semantic search, clustering, and deduplication.
- **Organization Strategy**: Arranged strictly from low parameter counts (sub-1B) up to billions and trillions of parameters.

---

## 📊 Parameter Tiers in this Niche

| Tier Directory | Parameter Range | Typical Target Hardware |
|---|---|---|
| [`1_Sub-1B`](./1_Sub-1B/README.md) | **< 1 Billion Parameters (22M - 335M)** | CPU or 1GB VRAM (Millions of tokens/sec) |
| [`2_1B-7B`](./2_1B-7B/README.md) | **1B to 7B Parameters** | 4GB - 16GB VRAM |

---

## 🔍 Quick Navigation
- **[Sub-1B (Lightweight & High-Throughput Embeddings)](./1_Sub-1B/README.md)**: Includes all-MiniLM-L6-v2, BGE-small / base / large-en-v1.5, E5-small / base / large-v2, ModernBERT-base / large, Nomic-Embed-Text-v1.5
- **[1B - 7B (State-of-the-Art Dense & Multilingual Embeddings)](./2_1B-7B/README.md)**: Includes BGE-M3, E5-Mistral-7B-Instruct, NV-Embed-v2, Qwen2-7B-Embedding
