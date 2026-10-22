# Model Card: F5-TTS

## 📋 Specifications
- **Category**: Text-to-Speech (TTS & Voice Generation)
- **Organization**: SWivid / F5 Team
- **Parameter Count**: 380M (Flow Matching)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/SWivid/F5-TTS](https://huggingface.co/SWivid/F5-TTS)

## 🎯 AOMe Implementation & Use Case
High-fidelity non-autoregressive voice cloning with a short 3-second reference audio.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Ultra-Fast & Edge Voice Synthesizers)
- **Estimated Requirements**: CPU / Mobile / 1GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/SWivid/F5-TTS)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
