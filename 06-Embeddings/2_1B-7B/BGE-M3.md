# Model Card: BGE-M3

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: BAAI
- **Parameter Count**: 568M
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)

## 🎯 AOMe Implementation & Use Case
Multi-functionality (dense, sparse lexical, and multi-vector colBERT in one model) across 100+ languages.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (State-of-the-Art Dense & Multilingual Embeddings)
- **Estimated Requirements**: 4GB - 16GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/BAAI/bge-m3)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
