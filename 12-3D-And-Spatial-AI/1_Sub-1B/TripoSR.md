# Model Card: TripoSR

## 📋 Specifications
- **Category**: 3D Generation & Spatial Intelligence
- **Organization**: Tripo AI & Stability AI
- **Parameter Count**: 300M - 400M (Feedforward LRM)
- **License**: MIT
- **Repository / Weights Link**: [https://huggingface.co/stabilityai/TripoSR](https://huggingface.co/stabilityai/TripoSR)

## 🎯 AOMe Implementation & Use Case
Generates textured 3D mesh files (.obj, .gltf) from a single 2D image in under 0.5 seconds.

## ⚙️ Hardware & Deployment Requirements
- **Tier**: Sub-1B (Instant Mesh & 3D Sketches)
- **Estimated Requirements**: 2GB - 4GB VRAM / CPU
- **Recommendation**: Deploy as an API service on cloud GPUs (RunPod, Lambda Labs, Modal) or stream via Ollama.

## 🔗 Quick Links
- [Hugging Face Repository](https://huggingface.co/stabilityai/TripoSR)
- [Tier Index](./README.md)
- [Niche Index](../README.md)
