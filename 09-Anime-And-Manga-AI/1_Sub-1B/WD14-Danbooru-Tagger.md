# Model Card: WD14-Danbooru-Tagger

## 📋 Specifications
- **Category**: Anime, Manga & 2D Illustration AI
- **Organization**: SmilingWolf
- **Parameter Count**: 80M - 150M (ConvNeXt / SwinV2)
- **License**: Apache 2.0
- **Repository / Weights Link**: [https://huggingface.co/SmilingWolf/wd-v1-4-convnextv2-tagger-v2](https://huggingface.co/SmilingWolf/wd-v1-4-convnextv2-tagger-v2)

## 🎯 AOMe Implementation & Use Case
Precise anime tag extraction (hair style, costume, pose, camera angle, character identity).

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Tagging, OCR & Colorization)
- **Estimated Requirements**: 1GB - 3GB VRAM / CPU
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, Modal) or stream via Ollama.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/SmilingWolf/wd-v1-4-convnextv2-tagger-v2)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
