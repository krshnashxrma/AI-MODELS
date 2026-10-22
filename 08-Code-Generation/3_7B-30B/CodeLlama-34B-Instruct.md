# Model Card: CodeLlama-34B-Instruct

## 📋 Specifications
- **Category**: Code Generation & Programming Assistants
- **Organization**: Meta
- **Parameter Count**: 34B
- **License**: Llama 2 Community License
- **Repository / Weights Link**: [https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf)

## 🎯 AOMe Implementation & Use Case
Infill fill-in-the-middle support and Python / C++ deep reasoning.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Senior Engineering Co-Pilots)
- **Estimated Requirements**: 12GB - 24GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
