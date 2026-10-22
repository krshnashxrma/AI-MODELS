# Model Card: Stable Diffusion 3.5 Medium

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: Stability AI
- **Parameter Count**: 2.5B (MMDiT Architecture)
- **License**: Stability Community License
- **Repository / Weights Link**: [https://huggingface.co/stabilityai/stable-diffusion-3.5-medium](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)

## 🎯 AOMe Implementation & Use Case
Typography rendering, prompt fidelity, and balance of speed and realism.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (High-Quality Consumer Diffusion)
- **Estimated Requirements**: 6GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
