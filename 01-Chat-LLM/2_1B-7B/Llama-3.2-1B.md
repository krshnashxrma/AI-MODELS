# Model Card: Llama-3.2-1B / 3B-Instruct

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: Meta
- **Parameter Count**: 1.23B / 3.21B
- **License**: Llama 3.2 Community License
- **Repository / Weights Link**: [https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)

## 🎯 AOMe Implementation & Use Case
Multilingual edge dialogue, tool calling, and summarization.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Consumer GPU)
- **Estimated Requirements**: 4GB - 8GB VRAM (or 8GB-16GB Unified RAM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
