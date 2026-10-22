# Model Card: NVIDIA Canary-1B

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: NVIDIA
- **Parameter Count**: 1B
- **License**: CC-BY-4.0
- **Repository / Weights Link**: [https://huggingface.co/nvidia/canary-1b](https://huggingface.co/nvidia/canary-1b)

## 🎯 AOMe Implementation & Use Case
Top-ranked Hugging Face Open ASR leaderboard model for multi-accent English and European languages.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Enterprise High-Accuracy ASR)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/nvidia/canary-1b)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
