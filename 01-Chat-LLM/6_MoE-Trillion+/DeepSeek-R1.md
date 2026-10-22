# Model Card: DeepSeek-R1

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: DeepSeek AI
- **Parameter Count**: 671B Total (37B Active) + Distilled Variants (1.5B - 70B)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)

## 🎯 AOMe Implementation & Use Case
Frontier chain-of-thought reasoning rivaling OpenAI o1.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: MoE & Trillion-Scale Architectures
- **Estimated Requirements**: Distributed Cloud Inference (vLLM / SGLang / TensorRT-LLM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
