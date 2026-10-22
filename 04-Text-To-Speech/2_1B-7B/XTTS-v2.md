# Model Card: XTTS-v2

## 📋 Specifications
- **Category**: Text-to-Speech (TTS & Voice Generation)
- **Organization**: Coqui AI
- **Parameter Count**: 1.2B
- **License**: Coqui Public Model License
- **Repository / Weights Link**: [https://huggingface.co/coqui/XTTS-v2](https://huggingface.co/coqui/XTTS-v2)

## 🎯 AOMe Implementation & Use Case
Real-time voice cloning in 17 languages with single audio snippet.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Studio Quality & Expressive Voice)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/coqui/XTTS-v2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
