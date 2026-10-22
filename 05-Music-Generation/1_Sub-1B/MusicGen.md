# Model Card: MusicGen Small

## 📋 Specifications
- **Category**: Music & Audio Generation
- **Organization**: Meta FAIR (AudioCraft)
- **Parameter Count**: 300M
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/facebook/musicgen-small](https://huggingface.co/facebook/musicgen-small)

## 🎯 AOMe Implementation & Use Case
Fast local instrumental and beat generation from short text prompts.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Rapid Music & Beat Sketches)
- **Estimated Requirements**: 2GB - 4GB VRAM / CPU
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/facebook/musicgen-small)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
