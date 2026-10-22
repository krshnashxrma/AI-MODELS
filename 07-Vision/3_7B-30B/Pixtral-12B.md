# Model Card: Pixtral-12B

## 📋 Specifications
- **Category**: Vision-Language Models (VLM & Multimodal Understanding)
- **Organization**: Mistral AI
- **Parameter Count**: 12.4B (Native multimodal 128k context)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/mistralai/Pixtral-12B-2409](https://huggingface.co/mistralai/Pixtral-12B-2409)

## 🎯 AOMe Implementation & Use Case
Arbitrary aspect ratio, multi-image sequences, and code generation from diagrams.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Advanced Document & UI Parsing)
- **Estimated Requirements**: 16GB - 24GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/mistralai/Pixtral-12B-2409)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
