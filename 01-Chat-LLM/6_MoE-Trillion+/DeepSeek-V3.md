# Model Card: DeepSeek-V3

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: DeepSeek AI
- **Parameter Count**: 671B Total (37B Active per token)
- **License**: DeepSeek Open Model License (commercial allowed)
- **Repository / Weights Link**: [https://huggingface.co/deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3)

## 🎯 AOMe Implementation & Use Case
Unmatched cost-to-performance frontier reasoning MoE with Multi-head Latent Attention.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: MoE & Trillion-Scale Architectures
- **Estimated Requirements**: Distributed Cloud Inference (vLLM / SGLang / TensorRT-LLM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/deepseek-ai/DeepSeek-V3)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
