# Model Card: DeepSeek-Coder-V2-Instruct

## 📋 Specifications
- **Category**: Code Generation & Programming Assistants
- **Organization**: DeepSeek AI
- **Parameter Count**: 236B Total (21B Active per token) / Lite 16B (2.4B Active)
- **License**: DeepSeek Open Model License (Commercial allowed)
- **Repository / Weights Link**: [https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct)

## 🎯 AOMe Implementation & Use Case
World's most capable open-source MoE coder, supporting 338 programming languages with 128k context.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: MoE & Frontier Coding Giants
- **Estimated Requirements**: Distributed Server (Dual/Quad 80GB VRAM) or Cloud Endpoints
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
