# Model Card: CosyVoice / CosyVoice-2

## 📋 Specifications
- **Category**: Text-to-Speech (TTS & Voice Generation)
- **Organization**: FunAudioLLM / Alibaba
- **Parameter Count**: 1B - 3B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/FunAudioLLM/CosyVoice-300M](https://huggingface.co/FunAudioLLM/CosyVoice-300M)

## 🎯 AOMe Implementation & Use Case
Multi-lingual emotional voice synthesis with fine-grained control over laughter, breaths, and pitch.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Studio Quality & Expressive Voice)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/FunAudioLLM/CosyVoice-300M)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
