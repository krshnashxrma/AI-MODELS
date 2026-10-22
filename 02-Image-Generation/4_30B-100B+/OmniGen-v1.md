# Model Card: OmniGen-v1

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: VectorSpaceLab
- **Parameter Count**: Unified Transformer (3.8B - scalable multimodal backbone)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/Shitao/OmniGen-v1](https://huggingface.co/Shitao/OmniGen-v1)

## 🎯 AOMe Implementation & Use Case
All-in-one image generation, inpainting, style transfer, and subject-driven generation.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 30B - 100B+ (Unified Multimodal Generation)
- **Estimated Requirements**: Multi-GPU Server (48GB - 80GB+)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/Shitao/OmniGen-v1)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
