# Model Card: StarCoderBase-1B / SmolLM2-Coder

## 📋 Specifications
- **Category**: Code Generation & Programming Assistants
- **Organization**: BigCode / Hugging Face
- **Parameter Count**: 1B / 360M
- **License**: OpenRAIL-M v1
- **Repository / Weights Link**: [https://huggingface.co/bigcode/starcoderbase-1b](https://huggingface.co/bigcode/starcoderbase-1b)

## 🎯 AOMe Implementation & Use Case
Sub-second code completion for constrained editor extensions.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Real-Time In-Editor Autocomplete)
- **Estimated Requirements**: 1GB - 2GB RAM / CPU (Zero latency fill-in-the-middle)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/bigcode/starcoderbase-1b)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
