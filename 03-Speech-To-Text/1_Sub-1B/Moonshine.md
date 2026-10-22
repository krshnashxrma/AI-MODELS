# Model Card: Moonshine

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: Useful Sensors
- **Parameter Count**: 27M (Tiny) / 62M (Base)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/UsefulSensors/moonshine](https://huggingface.co/UsefulSensors/moonshine)

## 🎯 AOMe Implementation & Use Case
Optimized sub-second speech-to-text on resource-constrained micro-devices.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Real-Time & Edge Transcription)
- **Estimated Requirements**: 500MB - 3GB RAM / CPU capable
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/UsefulSensors/moonshine)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
