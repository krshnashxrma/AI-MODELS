# Model Card: Whisper Large-v3 & Large-v3-Turbo

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: OpenAI
- **Parameter Count**: 1.55B (Large-v3) / 809M (Turbo)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)

## 🎯 AOMe Implementation & Use Case
Industry-standard accuracy for 100+ languages, timestamping, and translation.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Enterprise High-Accuracy ASR)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/openai/whisper-large-v3-turbo)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
