# Model Card: Qwen2-7B-Embedding

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: Alibaba
- **Parameter Count**: 7.6B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/Alibaba-NLP/bge-multilingual-gemma2](https://huggingface.co/Alibaba-NLP/bge-multilingual-gemma2)

## 🎯 AOMe Implementation & Use Case
High-capacity multilingual and long-document dense semantic indexing.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (State-of-the-Art Dense & Multilingual Embeddings)
- **Estimated Requirements**: 4GB - 16GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/Alibaba-NLP/bge-multilingual-gemma2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
