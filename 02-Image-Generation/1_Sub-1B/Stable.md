# Model Card: Stable Diffusion v1.5

## 📋 Specifications
- **Category**: Image Generation (Diffusion & Flow Matching)
- **Organization**: RunwayML / Stability AI
- **Parameter Count**: ~860M (UNet + Text Encoder)
- **License**: CreativeML OpenRAIL-M
- **Repository / Weights Link**: [https://huggingface.co/runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

## 🎯 AOMe Implementation & Use Case
Instant low-latency generation, massive ecosystem of LoRAs and ControlNets.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Fast / Lightweight Generators)
- **Estimated Requirements**: 2GB - 4GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
