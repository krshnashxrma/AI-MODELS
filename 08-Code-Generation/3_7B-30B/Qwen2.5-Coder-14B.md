# Model Card: Qwen2.5-Coder-14B / 32B-Instruct

## 📋 Specifications
- **Category**: Code Generation & Programming Assistants
- **Organization**: Qwen team
- **Parameter Count**: 14.7B / 32.5B (128k context)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)

## 🎯 AOMe Implementation & Use Case
State-of-the-art coding intelligence beating proprietary models (GPT-4o level) on EvalPlus & SWE-bench.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 7B - 30B (Senior Engineering Co-Pilots)
- **Estimated Requirements**: 12GB - 24GB VRAM
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
