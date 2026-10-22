# Model Card: Mistral-7B-Instruct-v0.3

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: Mistral AI
- **Parameter Count**: 7.25B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)

## 🎯 AOMe Implementation & Use Case
High-throughput general chatbot with function-calling support.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Consumer GPU)
- **Estimated Requirements**: 4GB - 8GB VRAM (or 8GB-16GB Unified RAM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
