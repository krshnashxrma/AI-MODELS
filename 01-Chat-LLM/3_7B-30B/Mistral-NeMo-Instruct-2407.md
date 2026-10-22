# Model Card: Mistral-NeMo-Instruct-2407

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: Mistral AI & NVIDIA
- **Parameter Count**: 12.2B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)

## 🎯 AOMe Implementation & Use Case
128k context window assistant for long document synthesis.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Workstation & Mid-Range)
- **Estimated Requirements**: 12GB - 24GB VRAM (RTX 3060/4070/4090 or Apple M-series)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
