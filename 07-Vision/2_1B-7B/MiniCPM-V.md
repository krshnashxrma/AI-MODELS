# Model Card: MiniCPM-V 2.6

## 📋 Specifications
- **Category**: Vision-Language Models (VLM & Multimodal Understanding)
- **Organization**: OpenBMB
- **Parameter Count**: 8B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/openbmb/MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6)

## 🎯 AOMe Implementation & Use Case
Single-GPU multimodal model matching GPT-4V on OCR and spatial reasoning.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Multimodal Assistants)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/openbmb/MiniCPM-V-2_6)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
