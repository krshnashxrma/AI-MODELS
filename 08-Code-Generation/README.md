# Code Generation & Programming Assistants

## 📌 Niche Overview
- **AOMe Role**: Autocompletion, code generation, refactoring, unit test synthesis, debugging, and terminal agent control.
- **Organization Strategy**: Arranged strictly from low parameter counts (sub-1B) up to billions and trillions of parameters.

---

## 📊 Parameter Tiers in this Niche

| Tier Directory | Parameter Range | Typical Target Hardware |
|---|---|---|
| [`1_Sub-1B`](./1_Sub-1B/README.md) | **< 1 Billion Parameters (500M)** | 1GB - 2GB RAM / CPU (Zero latency fill-in-the-middle) |
| [`2_1B-7B`](./2_1B-7B/README.md) | **1B to 7B Parameters** | 4GB - 8GB VRAM |
| [`3_7B-30B`](./3_7B-30B/README.md) | **7B to 30B Parameters** | 12GB - 24GB VRAM |
| [`4_MoE-Trillion+`](./4_MoE-Trillion+/README.md) | **Sparse Mixture-of-Experts (236B+ Parameters)** | Distributed Server (Dual/Quad 80GB VRAM) or Cloud Endpoints |

---

## 🔍 Quick Navigation
- **[Sub-1B (Real-Time In-Editor Autocomplete)](./1_Sub-1B/README.md)**: Includes Qwen2.5-Coder-0.5B-Instruct, StarCoderBase-1B / SmolLM2-Coder
- **[1B - 7B (Lightweight Developer Workstation)](./2_1B-7B/README.md)**: Includes Qwen2.5-Coder-1.5B / 3B / 7B-Instruct, StarCoder2-3B / 7B, DeepSeek-Coder-6.7B-Instruct
- **[7B - 30B (Senior Engineering Co-Pilots)](./3_7B-30B/README.md)**: Includes Qwen2.5-Coder-14B / 32B-Instruct, StarCoder2-15B, CodeLlama-34B-Instruct
- **[MoE & Frontier Coding Giants](./4_MoE-Trillion+/README.md)**: Includes DeepSeek-Coder-V2-Instruct, DeepSeek-V3 / R1 (Coding & Algorithmic Specialization)
