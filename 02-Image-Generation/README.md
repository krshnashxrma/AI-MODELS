# Image Generation (Diffusion & Flow Matching)

## 📌 Niche Overview
- **AOMe Role**: Text-to-image synthesis, visual asset creation, UI mockups, and stylistic transformation.
- **Organization Strategy**: Arranged strictly from low parameter counts (sub-1B) up to billions and trillions of parameters.

---

## 📊 Parameter Tiers in this Niche

| Tier Directory | Parameter Range | Typical Target Hardware |
|---|---|---|
| [`1_Sub-1B`](./1_Sub-1B/README.md) | **< 1 Billion Parameters** | 2GB - 4GB VRAM |
| [`2_1B-7B`](./2_1B-7B/README.md) | **1B to 7B Parameters** | 6GB - 12GB VRAM |
| [`3_7B-30B`](./3_7B-30B/README.md) | **7B to 30B Parameters** | 16GB - 24GB+ VRAM (or quantized FP8/GGUF on 12GB) |
| [`4_30B-100B+`](./4_30B-100B+/README.md) | **30B+ Parameters** | Multi-GPU Server (48GB - 80GB+) |

---

## 🔍 Quick Navigation
- **[Sub-1B (Fast / Lightweight Generators)](./1_Sub-1B/README.md)**: Includes Stable Diffusion v1.5, Tiny-SD / SD-Turbo
- **[1B - 7B (High-Quality Consumer Diffusion)](./2_1B-7B/README.md)**: Includes Stable Diffusion XL (SDXL 1.0), Stable Diffusion 3.5 Medium, PixArt-Sigma
- **[7B - 30B (State-of-the-Art Flow Matching & Large DiT)](./3_7B-30B/README.md)**: Includes FLUX.1-schnell / FLUX.1-dev, Stable Diffusion 3.5 Large, AuraFlow v0.3
- **[30B - 100B+ (Unified Multimodal Generation)](./4_30B-100B+/README.md)**: Includes OmniGen-v1
