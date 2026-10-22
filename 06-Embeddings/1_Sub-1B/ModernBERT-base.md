# Model Card: ModernBERT-base / large

## 📋 Specifications
- **Category**: Text & Multimodal Embeddings (RAG & Semantic Search)
- **Organization**: Answer.AI & LightOn
- **Parameter Count**: 149M / 395M (8k native context)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)

## 🎯 AOMe Implementation & Use Case
Modern drop-in BERT replacement with Rotary Embeddings and 8192 token context.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Lightweight & High-Throughput Embeddings)
- **Estimated Requirements**: CPU or 1GB VRAM (Millions of tokens/sec)
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, AWS Bedrock/SageMaker) or run locally using 4-bit / 8-bit quantized GGUF via Ollama/llama.cpp when needed.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/answerdotai/ModernBERT-large)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
