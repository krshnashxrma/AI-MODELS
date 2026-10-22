# Model Card: Moondream2

## 📋 Specifications
- **Category**: Vision-Language Models (VLM & Multimodal Understanding)
- **Organization**: vikhyatk
- **Parameter Count**: 1.86B
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/vikhyatk/moondream2](https://huggingface.co/vikhyatk/moondream2)

## 🎯 AOMe Implementation & Use Case
High-speed tiny vision model for image captioning, QA, and object bounding boxes.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Multimodal Assistants)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/vikhyatk/moondream2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
