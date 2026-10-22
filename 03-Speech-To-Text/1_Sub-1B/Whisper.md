# Model Card: Whisper Tiny / Base / Small / Medium

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: OpenAI
- **Parameter Count**: 39M (Tiny), 74M (Base), 244M (Small), 769M (Medium)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/openai/whisper-small](https://huggingface.co/openai/whisper-small)

## 🎯 AOMe Implementation & Use Case
Fast edge voice commands and low-latency whisper.cpp transcription.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Real-Time & Edge Transcription)
- **Estimated Requirements**: 500MB - 3GB RAM / CPU capable
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/openai/whisper-small)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
