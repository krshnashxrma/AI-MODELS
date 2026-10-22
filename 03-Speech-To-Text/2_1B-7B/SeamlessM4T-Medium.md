# Model Card: SeamlessM4T-Medium

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: Meta
- **Parameter Count**: 1.2B
- **License**: CC-BY-NC 4.0
- **Repository / Weights Link**: [https://huggingface.co/facebook/seamless-m4t-v2-large](https://huggingface.co/facebook/seamless-m4t-v2-large)

## 🎯 AOMe Implementation & Use Case
Unified speech-to-speech and speech-to-text translation across 100 languages.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Enterprise High-Accuracy ASR)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/facebook/seamless-m4t-v2-large)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
