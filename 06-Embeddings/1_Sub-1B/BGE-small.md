# Model Card: BGE-small / base / large-en-v1.5

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: BAAI
- **Parameter Count**: 33M (Small), 109M (Base), 335M (Large)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)

## 🎯 AOMe Implementation & Use Case
Proven standard for production RAG pipelines on standard consumer hardware.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Lightweight & High-Throughput Embeddings)
- **Estimated Requirements**: CPU or 1GB VRAM (Millions of tokens/sec)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/BAAI/bge-large-en-v1.5)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
