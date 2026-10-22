# Chat & Large Language Models (LLMs)

## 📌 Niche Overview
- **AOMe Role**: Conversational AI, chatbots, cognitive reasoning, interactive assistants.
- **Organization Strategy**: Arranged strictly from low parameter counts (sub-1B) up to billions and trillions of parameters.

---

## 📊 Parameter Tiers in this Niche

| Tier Directory | Parameter Range | Typical Target Hardware |
|---|---|---|
| [`1_Sub-1B`](./1_Sub-1B/README.md) | **< 1 Billion Parameters (100M - 999M)** | 1GB - 2GB RAM / CPU or Mobile NPU |
| [`2_1B-7B`](./2_1B-7B/README.md) | **1B to 7B Parameters** | 4GB - 8GB VRAM (or 8GB-16GB Unified RAM) |
| [`3_7B-30B`](./3_7B-30B/README.md) | **7B to 30B Parameters** | 12GB - 24GB VRAM (RTX 3060/4070/4090 or Apple M-series) |
| [`4_30B-70B`](./4_30B-70B/README.md) | **30B to 70B Parameters** | 32GB - 80GB VRAM (Dual 3090/4090 or A100/H100 / Mac Studio) |
| [`5_70B-100B+`](./5_70B-100B+/README.md) | **70B to 405B Parameters (Dense)** | Multi-GPU Cluster (4x-8x H100 80GB) |
| [`6_MoE-Trillion+`](./6_MoE-Trillion+/README.md) | **Sparse Mixture-of-Experts (Hundreds of Billions to Trillions)** | Distributed Cloud Inference (vLLM / SGLang / TensorRT-LLM) |

---

## 🔍 Quick Navigation
- **[Sub-1B (Edge & Mobile)](./1_Sub-1B/README.md)**: Includes SmolLM2-135M / 360M, Qwen2.5-0.5B-Instruct, H2O-Danube3-500M
- **[1B - 7B (Lightweight Consumer GPU)](./2_1B-7B/README.md)**: Includes SmolLM2-1.7B-Instruct, Llama-3.2-1B / 3B-Instruct, Qwen2.5-1.5B / 3B / 7B-Instruct, Gemma-2-2B-IT, Mistral-7B-Instruct-v0.3
- **[7B - 30B (Workstation & Mid-Range)](./3_7B-30B/README.md)**: Includes Gemma-2-9B-IT / 27B-IT, Mistral-NeMo-Instruct-2407, Qwen2.5-14B / 32B-Instruct
- **[30B - 70B (High-Performance Enterprise)](./4_30B-70B/README.md)**: Includes Llama-3.3-70B-Instruct, Qwen2.5-72B-Instruct
- **[70B - 100B+ (Data Center Dense Models)](./5_70B-100B+/README.md)**: Includes Llama-3.1-405B-Instruct
- **[MoE & Trillion-Scale Architectures](./6_MoE-Trillion+/README.md)**: Includes DeepSeek-V3, DeepSeek-R1, Grok-1, Switch Transformers (Switch-C 1.6T)
