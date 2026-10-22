# Sub-1B (Real-Time In-Editor Autocomplete)

- **Category**: `08-Code-Generation`
- **Parameter Window**: `< 1 Billion Parameters (500M)`
- **Hardware Footprint**: `1GB - 2GB RAM / CPU (Zero latency fill-in-the-middle)`

---

## 🤖 Registered Models

### 🔹 Qwen2.5-Coder-0.5B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `490M`
- **Official Hugging Face / Source**: [Qwen2.5-Coder-0.5B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2.5-Coder-0.5B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Instant keystroke-by-keystroke tab autocompletion and syntax fixes.

---
### 🔹 StarCoderBase-1B / SmolLM2-Coder
- **Organization / Creator**: BigCode / Hugging Face
- **Parameter Count**: `1B / 360M`
- **Official Hugging Face / Source**: [StarCoderBase-1B / SmolLM2-Coder on Hub](https://huggingface.co/bigcode/starcoderbase-1b)
- **License**: `OpenRAIL-M v1`
- **AOMe Use Case**: Sub-second code completion for constrained editor extensions.

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
