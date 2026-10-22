# Model Card: DeepSeek-VL2

## 📋 Specifications
- **Category**: Vision-Language Models (VLM & Multimodal Understanding)
- **Organization**: DeepSeek AI
- **Parameter Count**: MoE Vision-Language (Dynamic Sparse Experts)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/deepseek-ai/deepseek-vl2](https://huggingface.co/deepseek-ai/deepseek-vl2)

## 🎯 AOMe Implementation & Use Case
High-throughput sparse multimodal understanding for massive document batches.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: MoE Multimodal Architectures
- **Estimated Requirements**: Distributed Cloud Infrastructure
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/deepseek-ai/deepseek-vl2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
