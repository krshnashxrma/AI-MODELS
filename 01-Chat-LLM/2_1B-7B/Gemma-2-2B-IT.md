# Model Card: Gemma-2-2B-IT

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: Google DeepMind
- **Parameter Count**: 2.61B
- **License**: Gemma Terms of Use
- **Repository / Weights Link**: [https://huggingface.co/google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)

## 🎯 AOMe Implementation & Use Case
Efficient factual reasoning and conversational safety.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: 1B - 7B (Lightweight Consumer GPU)
- **Estimated Requirements**: 4GB - 8GB VRAM (or 8GB-16GB Unified RAM)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/google/gemma-2-2b-it)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
