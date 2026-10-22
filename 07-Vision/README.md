# Vision-Language Models (VLM & Multimodal Understanding)

## 📌 Niche Overview
- **AOMe Role**: Document OCR, UI/UX diagram reading, visual QA, screenshot analysis, object identification, and robotics vision.
- **Organization Strategy**: Arranged strictly from low parameter counts (sub-1B) up to billions and trillions of parameters.

---

## 📊 Parameter Tiers in this Niche

| Tier Directory | Parameter Range | Typical Target Hardware |
|---|---|---|
| [`1_Sub-1B`](./1_Sub-1B/README.md) | **< 1 Billion Parameters (256M - 900M)** | 1GB - 2GB RAM / Edge NPU |
| [`2_1B-7B`](./2_1B-7B/README.md) | **1B to 7B Parameters** | 4GB - 12GB VRAM |
| [`3_7B-30B`](./3_7B-30B/README.md) | **7B to 30B Parameters** | 16GB - 24GB VRAM |
| [`4_30B-100B+`](./4_30B-100B+/README.md) | **30B to 90B Parameters** | Multi-GPU Cluster (48GB - 80GB+) |
| [`5_MoE-Trillion+`](./5_MoE-Trillion+/README.md) | **Sparse Mixture-of-Experts Vision Models** | Distributed Cloud Infrastructure |

---

## 🔍 Quick Navigation
- **[Sub-1B (On-Device Vision Assistants)](./1_Sub-1B/README.md)**: Includes SmolVLM-256M / 500M
- **[1B - 7B (Lightweight Multimodal Assistants)](./2_1B-7B/README.md)**: Includes SmolVLM-Instruct (2.2B), Moondream2, Qwen2-VL-2B / 7B-Instruct, PaliGemma-2-3B / 10B, MiniCPM-V 2.6
- **[7B - 30B (Advanced Document & UI Parsing)](./3_7B-30B/README.md)**: Includes Llama-3.2-11B-Vision-Instruct, Pixtral-12B, InternVL2-26B / 40B
- **[30B - 100B+ (Frontier Multimodal Foundations)](./4_30B-100B+/README.md)**: Includes Qwen2-VL-72B-Instruct, Llama-3.2-90B-Vision-Instruct
- **[MoE Multimodal Architectures](./5_MoE-Trillion+/README.md)**: Includes DeepSeek-VL2
