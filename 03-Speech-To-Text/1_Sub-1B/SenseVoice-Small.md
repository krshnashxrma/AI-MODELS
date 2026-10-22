# Model Card: SenseVoice-Small

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: FunAudioLLM / Alibaba
- **Parameter Count**: 230M
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/FunAudioLLM/SenseVoiceSmall](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)

## 🎯 AOMe Implementation & Use Case
Ultra-fast multi-lingual ASR with emotion recognition and audio event detection.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Real-Time & Edge Transcription)
- **Estimated Requirements**: 500MB - 3GB RAM / CPU capable
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
