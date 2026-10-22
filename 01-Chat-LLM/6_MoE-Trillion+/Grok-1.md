# Model Card: Grok-1

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: xAI
- **Parameter Count**: 314B MoE (86B Active per token)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/xai-org/grok-1](https://huggingface.co/xai-org/grok-1)

## 🎯 AOMe Implementation & Use Case
Open base weights for massive scale conversational research.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: MoE & Trillion-Scale Architectures
- **Estimated Requirements**: Distributed Cloud Inference (vLLM / SGLang / TensorRT-LLM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/xai-org/grok-1)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
