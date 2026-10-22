# 7B - 30B (Advanced Document & UI Parsing)

- **Category**: `07-Vision`
- **Parameter Window**: `7B to 30B Parameters`
- **Hardware Footprint**: `16GB - 24GB VRAM`

---

## 🤖 Registered Models

### 🔹 Llama-3.2-11B-Vision-Instruct
- **Organization / Creator**: Meta
- **Parameter Count**: `10.6B`
- **Official Hugging Face / Source**: [Llama-3.2-11B-Vision-Instruct on Hub](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)
- **License**: `Llama 3.2 Community License`
- **AOMe Use Case**: Native image reasoning, visual QA, and chart comprehension integrated into Llama 3.

---
### 🔹 Pixtral-12B
- **Organization / Creator**: Mistral AI
- **Parameter Count**: `12.4B (Native multimodal 128k context)`
- **Official Hugging Face / Source**: [Pixtral-12B on Hub](https://huggingface.co/mistralai/Pixtral-12B-2409)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Arbitrary aspect ratio, multi-image sequences, and code generation from diagrams.

---
### 🔹 InternVL2-26B / 40B
- **Organization / Creator**: OpenGVLab
- **Parameter Count**: `26B / 40B`
- **Official Hugging Face / Source**: [InternVL2-26B / 40B on Hub](https://huggingface.co/OpenGVLab/InternVL2-26B)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Exceptional mathematical diagram reasoning and scientific document parsing.

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
