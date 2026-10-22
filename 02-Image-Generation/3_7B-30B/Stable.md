# Model Card: Stable Diffusion 3.5 Large

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: Stability AI
- **Parameter Count**: 8.1B
- **License**: Stability Community License
- **Repository / Weights Link**: [https://huggingface.co/stabilityai/stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)

## 🎯 AOMe Implementation & Use Case
Flagship multimodal diffusion for commercial grade creative assets.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (State-of-the-Art Flow Matching & Large DiT)
- **Estimated Requirements**: 16GB - 24GB+ VRAM (or quantized FP8/GGUF on 12GB)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
