# Sub-1B (Tagging, OCR & Colorization)

- **Category**: `09-Anime-And-Manga-AI`
- **Parameter Window**: `< 1 Billion Parameters`
- **Hardware Footprint**: `1GB - 3GB VRAM / CPU`

---

## 🤖 Registered Models

### 🔹 MangaOCR
- **Organization / Creator**: kha-white
- **Parameter Count**: `100M`
- **Official Hugging Face / Source**: [MangaOCR on Hub](https://huggingface.co/kha-white/manga-ocr-base)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Zero-shot optical character recognition for Japanese manga text bubbles and handwritten dialogue.

---
### 🔹 WD14-Danbooru-Tagger
- **Organization / Creator**: SmilingWolf
- **Parameter Count**: `80M - 150M (ConvNeXt / SwinV2)`
- **Official Hugging Face / Source**: [WD14-Danbooru-Tagger on Hub](https://huggingface.co/SmilingWolf/wd-v1-4-convnextv2-tagger-v2)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Precise anime tag extraction (hair style, costume, pose, camera angle, character identity).

---
### 🔹 Anything V5 / Waifu-Diffusion-1.4
- **Organization / Creator**: CagliostroLab / Hakurei
- **Parameter Count**: `~860M`
- **Official Hugging Face / Source**: [Anything V5 / Waifu-Diffusion-1.4 on Hub](https://huggingface.co/stablediffusionapi/anything-v5)
- **License**: `CreativeML OpenRAIL-M`
- **AOMe Use Case**: Classic lightweight 2D anime stylized image rendering on standard consumer GPUs.

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
