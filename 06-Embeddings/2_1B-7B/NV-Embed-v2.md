# Model Card: NV-Embed-v2

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: NVIDIA
- **Parameter Count**: 7B
- **License**: CC-BY-NC 4.0
- **Repository / Weights Link**: [https://huggingface.co/nvidia/NV-Embed-v2](https://huggingface.co/nvidia/NV-Embed-v2)

## 🎯 AOMe Implementation & Use Case
#1 ranked general embedding model on Massive Text Embedding Benchmark (MTEB).

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (State-of-the-Art Dense & Multilingual Embeddings)
- **Estimated Requirements**: 4GB - 16GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/nvidia/NV-Embed-v2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
