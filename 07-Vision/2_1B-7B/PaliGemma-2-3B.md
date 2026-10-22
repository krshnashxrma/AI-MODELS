# Model Card: PaliGemma-2-3B / 10B

## 📋 Specifications
- **Category**: Vision-Language Models (VLM & Multimodal Understanding)
- **Organization**: Google DeepMind
- **Parameter Count**: 3B / 10B
- **License**: Gemma Terms of Use
- **Repository / Weights Link**: [https://huggingface.co/google/paligemma-2-3b-pt-448](https://huggingface.co/google/paligemma-2-3b-pt-448)

## 🎯 AOMe Implementation & Use Case
Specialized OCR, document QA, bounding box detection, and fine-tuning base.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Multimodal Assistants)
- **Estimated Requirements**: 4GB - 12GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/google/paligemma-2-3b-pt-448)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
