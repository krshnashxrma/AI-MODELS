# Sub-1B (Instant Mesh & 3D Sketches)

- **Category**: `12-3D-And-Spatial-AI`
- **Parameter Window**: `< 1 Billion Parameters`
- **Hardware Footprint**: `2GB - 4GB VRAM / CPU`

---

## 🤖 Registered Models

### 🔹 TripoSR
- **Organization / Creator**: Tripo AI & Stability AI
- **Parameter Count**: `300M - 400M (Feedforward LRM)`
- **Official Hugging Face / Source**: [TripoSR on Hub](https://huggingface.co/stabilityai/TripoSR)
- **License**: `MIT`
- **AOMe Use Case**: Generates textured 3D mesh files (.obj, .gltf) from a single 2D image in under 0.5 seconds.

---
### 🔹 Shap-E
- **Organization / Creator**: OpenAI
- **Parameter Count**: `300M`
- **Official Hugging Face / Source**: [Shap-E on Hub](https://huggingface.co/openai/shap-e)
- **License**: `MIT`
- **AOMe Use Case**: Direct text/image conditioning to 3D implicit functions and NeRF renders.

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
