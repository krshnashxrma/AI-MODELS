# Model Card: AuraFlow v0.3

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: fal.ai
- **Parameter Count**: 6.8B (Open Flow-based DiT)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/fal/AuraFlow-v0.3](https://huggingface.co/fal/AuraFlow-v0.3)

## 🎯 AOMe Implementation & Use Case
Fully open Apache-licensed high-parameter flow transformer.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (State-of-the-Art Flow Matching & Large DiT)
- **Estimated Requirements**: 16GB - 24GB+ VRAM (or quantized FP8/GGUF on 12GB)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/fal/AuraFlow-v0.3)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
