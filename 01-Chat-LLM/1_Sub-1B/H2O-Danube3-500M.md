# Model Card: H2O-Danube3-500M

## 📋 Specifications
- **Category**: Chat & Large Language Models (LLMs)
- **Organization**: H2O.ai
- **Parameter Count**: 500M
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/h2oai/h2o-danube3-500m-chat](https://huggingface.co/h2oai/h2o-danube3-500m-chat)

## 🎯 AOMe Implementation & Use Case
On-device private chat and offline document queries.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Edge & Mobile)
- **Estimated Requirements**: 1GB - 2GB RAM / CPU or Mobile NPU
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/h2oai/h2o-danube3-500m-chat)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
