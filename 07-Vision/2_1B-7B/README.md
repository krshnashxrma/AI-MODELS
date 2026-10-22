# 1B - 7B (Lightweight Multimodal Assistants)

- **Category**: `07-Vision`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `4GB - 12GB VRAM`

---

## 🤖 Registered Models

### 🔹 SmolVLM-Instruct (2.2B)
- **Organization / Creator**: Hugging Face
- **Parameter Count**: `2.2B`
- **Official Hugging Face / Source**: [SmolVLM-Instruct (2.2B) on Hub](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High efficiency edge multimodal model for document parsing and screen understanding.

---
### 🔹 Moondream2
- **Organization / Creator**: vikhyatk
- **Parameter Count**: `1.86B`
- **Official Hugging Face / Source**: [Moondream2 on Hub](https://huggingface.co/vikhyatk/moondream2)
- **License**: `Apache 2.0`
- **AOMe Use Case**: High-speed tiny vision model for image captioning, QA, and object bounding boxes.

---
### 🔹 Qwen2-VL-2B / 7B-Instruct
- **Organization / Creator**: Qwen team
- **Parameter Count**: `2.2B / 7.6B (Dynamic Resolution)`
- **Official Hugging Face / Source**: [Qwen2-VL-2B / 7B-Instruct on Hub](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)
- **License**: `Apache 2.0`
- **AOMe Use Case**: World-class visual grounding, multi-page PDF processing, video timeline analysis.

---
### 🔹 PaliGemma-2-3B / 10B
- **Organization / Creator**: Google DeepMind
- **Parameter Count**: `3B / 10B`
- **Official Hugging Face / Source**: [PaliGemma-2-3B / 10B on Hub](https://huggingface.co/google/paligemma-2-3b-pt-448)
- **License**: `Gemma Terms of Use`
- **AOMe Use Case**: Specialized OCR, document QA, bounding box detection, and fine-tuning base.

---
### 🔹 MiniCPM-V 2.6
- **Organization / Creator**: OpenBMB
- **Parameter Count**: `8B`
- **Official Hugging Face / Source**: [MiniCPM-V 2.6 on Hub](https://huggingface.co/openbmb/MiniCPM-V-2_6)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Single-GPU multimodal model matching GPT-4V on OCR and spatial reasoning.

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
