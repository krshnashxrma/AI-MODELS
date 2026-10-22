# Model Card: Nomic-Embed-Text-v1.5

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: Nomic AI
- **Parameter Count**: 137M (Matryoshka Embeddings)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/nomic-ai/nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)

## 🎯 AOMe Implementation & Use Case
Dynamic embedding truncation (flexible 64 to 768 dimensions) with 8k context.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Lightweight & High-Throughput Embeddings)
- **Estimated Requirements**: CPU or 1GB VRAM (Millions of tokens/sec)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
