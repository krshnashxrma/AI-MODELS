# Model Card: Tiny-SD / SD-Turbo

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: Segmind / Stability AI
- **Parameter Count**: 200M - 800M (1-step inference)
- **License**: OpenRAIL-M
- **Repository / Weights Link**: [https://huggingface.co/stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo)

## 🎯 AOMe Implementation & Use Case
Real-time generation in canvas and responsive UI editing.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Fast / Lightweight Generators)
- **Estimated Requirements**: 2GB - 4GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/stabilityai/sd-turbo)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
