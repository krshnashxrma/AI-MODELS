# Model Card: ChatTTS

## 📋 Specifications
- **Category**: Text-to-Speech (TTS & Voice Generation)
- **Organization**: 2noise
- **Parameter Count**: ~1B
- **License**: CC-BY-NC-4.0
- **Repository / Weights Link**: [https://huggingface.co/2noise/ChatTTS](https://huggingface.co/2noise/ChatTTS)

## 🎯 AOMe Implementation & Use Case
Conversational TTS designed explicitly for chatbot dialogue with natural interjections.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Studio Quality & Expressive Voice)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/2noise/ChatTTS)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
