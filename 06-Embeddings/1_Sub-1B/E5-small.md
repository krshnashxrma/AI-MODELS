# Model Card: E5-small / base / large-v2

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: Microsoft
- **Parameter Count**: 33M - 335M
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/intfloat/e5-large-v2](https://huggingface.co/intfloat/e5-large-v2)

## 🎯 AOMe Implementation & Use Case
High-accuracy asymmetric search (query vs document retrieval).

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Lightweight & High-Throughput Embeddings)
- **Estimated Requirements**: CPU or 1GB VRAM (Millions of tokens/sec)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/intfloat/e5-large-v2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
