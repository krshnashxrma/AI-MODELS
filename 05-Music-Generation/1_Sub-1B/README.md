# Sub-1B (Rapid Music & Beat Sketches)

- **Category**: `05-Music-Generation`
- **Parameter Window**: `< 1 Billion Parameters (300M)`
- **Hardware Footprint**: `2GB - 4GB VRAM / CPU`

---

## 🤖 Registered Models

### 🔹 MusicGen Small
- **Organization / Creator**: Meta FAIR (AudioCraft)
- **Parameter Count**: `300M`
- **Official Hugging Face / Source**: [MusicGen Small on Hub](https://huggingface.co/facebook/musicgen-small)
- **License**: `MIT`
- **AOMe Use Case**: Fast local instrumental and beat generation from short text prompts.

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
