# Model Card: PixArt-Sigma

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: PixArt-alpha team
- **Parameter Count**: 600M - 2B (DiT)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS](https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS)

## 🎯 AOMe Implementation & Use Case
4K diffusion transformer with high photorealism and efficient compute.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (High-Quality Consumer Diffusion)
- **Estimated Requirements**: 6GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
