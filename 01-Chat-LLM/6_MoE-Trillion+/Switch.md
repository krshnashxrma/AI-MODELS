# Model Card: Switch Transformers (Switch-C 1.6T)

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: Google Research
- **Parameter Count**: 1.6 Trillion Parameters (Sparse MoE)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/google/switch-c-2048](https://huggingface.co/google/switch-c-2048)

## 🎯 AOMe Implementation & Use Case
Pioneering trillion-parameter sparse MoE research model.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: MoE & Trillion-Scale Architectures
- **Estimated Requirements**: Distributed Cloud Inference (vLLM / SGLang / TensorRT-LLM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/google/switch-c-2048)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
