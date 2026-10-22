# Model Card: StarCoder2-3B / 7B

## 📋 Specifications
- **Category**: Code Generation & Programming Assistants
- **Organization**: BigCode / ServiceNow / Hugging Face
- **Parameter Count**: 3B / 7B
- **License**: OpenRAIL-M v1
- **Repository / Weights Link**: [https://huggingface.co/bigcode/starcoder2-7b](https://huggingface.co/bigcode/starcoder2-7b)

## 🎯 AOMe Implementation & Use Case
Permissively licensed code generation trained on 600+ programming languages.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Developer Workstation)
- **Estimated Requirements**: 4GB - 8GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/bigcode/starcoder2-7b)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
