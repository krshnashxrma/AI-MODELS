# Model Card: Llama-3.2-11B-Vision-Instruct

## 📋 Specifications
- **Category**: Vision-Language Models (VLM & Multimodal Understanding)
- **Organization**: Meta
- **Parameter Count**: 10.6B
- **License**: Llama 3.2 Community License
- **Repository / Weights Link**: [https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)

## 🎯 AOMe Implementation & Use Case
Native image reasoning, visual QA, and chart comprehension integrated into Llama 3.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Advanced Document & UI Parsing)
- **Estimated Requirements**: 16GB - 24GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
