# 1B - 7B (High-Poly Textured 3D Assets)

- **Category**: `12-3D-And-Spatial-AI`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `8GB - 16GB VRAM`

---

## 🤖 Registered Models

### 🔹 Stable Fast 3D (SF3D)
- **Organization / Creator**: Stability AI
- **Parameter Count**: `1.2B`
- **Official Hugging Face / Source**: [Stable Fast 3D (SF3D) on Hub](https://huggingface.co/stabilityai/stable-fast-3d)
- **License**: `Stability Community License`
- **AOMe Use Case**: Generates UV-unwrapped 3D meshes with PBR materials (normal and roughness maps) in 0.5s.

---
### 🔹 InstantMesh
- **Organization / Creator**: TencentARC
- **Parameter Count**: `1.5B (Multi-view DiT + Sparse Reconstruction)`
- **Official Hugging Face / Source**: [InstantMesh on Hub](https://huggingface.co/TencentARC/InstantMesh)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High-fidelity topological meshes from single product shots and character renders.

---
## 💡 Deployment Quickstart (No local file storage)

```python
# Streaming inference via Hugging Face Hub (zero disk bloat)
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "MODEL_ID_FROM_ABOVE"
# When ready to run on cloud server or high-memory instance:
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")
```
