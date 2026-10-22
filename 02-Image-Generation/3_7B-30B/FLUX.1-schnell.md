# Model Card: FLUX.1-schnell / FLUX.1-dev

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: Black Forest Labs
- **Parameter Count**: 12B (Flow Matching Transformer)
- **License**: FLUX.1-dev Non-Commercial / schnell Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)

## 🎯 AOMe Implementation & Use Case
Highest fidelity text rendering, complex spatial compositions, and photorealism.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (State-of-the-Art Flow Matching & Large DiT)
- **Estimated Requirements**: 16GB - 24GB+ VRAM (or quantized FP8/GGUF on 12GB)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
