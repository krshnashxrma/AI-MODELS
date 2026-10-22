# Model Card: SALMONN / Qwen2-Audio-7B-Instruct

## 📋 Specifications
- **Category**: Speech-to-Text (ASR & Transcription)
- **Organization**: Alibaba / Tsinghua
- **Parameter Count**: 7.6B - 13B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct)

## 🎯 AOMe Implementation & Use Case
End-to-end audio understanding: listens, transcribes, parses tone, and speaks back directly.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Multimodal Audio-LLM Unified Interpreters)
- **Estimated Requirements**: 16GB - 32GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
