# Model Card: all-MiniLM-L6-v2

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: Sentence Transformers
- **Parameter Count**: 22.7M (384 dims)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

## 🎯 AOMe Implementation & Use Case
Ultra-lightweight vector embedding for mobile apps and instant offline lookup.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Lightweight & High-Throughput Embeddings)
- **Estimated Requirements**: CPU or 1GB VRAM (Millions of tokens/sec)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
