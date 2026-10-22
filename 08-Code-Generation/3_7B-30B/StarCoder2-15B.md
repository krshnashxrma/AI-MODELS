# Model Card: StarCoder2-15B

## 📋 Specifications
- **Category**: Code Generation & Programming Assistants
- **Organization**: BigCode
- **Parameter Count**: 15B
- **License**: OpenRAIL-M v1
- **Repository / Weights Link**: [https://huggingface.co/bigcode/starcoder2-15b](https://huggingface.co/bigcode/starcoder2-15b)

## 🎯 AOMe Implementation & Use Case
Enterprise code base maintenance, refactoring, and multi-file code understanding.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Senior Engineering Co-Pilots)
- **Estimated Requirements**: 12GB - 24GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/bigcode/starcoder2-15b)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
