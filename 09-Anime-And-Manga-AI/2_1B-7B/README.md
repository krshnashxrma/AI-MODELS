# 1B - 7B (Premier Anime XL & 2D Animation)

- **Category**: `09-Anime-And-Manga-AI`
- **Parameter Window**: `1B to 7B Parameters`
- **Hardware Footprint**: `6GB - 12GB VRAM`

---

## 🤖 Registered Models

### 🔹 Animagine-XL-3.1
- **Organization / Creator**: CagliostroLab / Linaqruf
- **Parameter Count**: `3.5B (SDXL DiT backbone)`
- **Official Hugging Face / Source**: [Animagine-XL-3.1 on Hub](https://huggingface.co/cagliostrolab/animagine-xl-3.1)
- **License**: `Animagine OpenRAIL-M`
- **AOMe Use Case**: The undisputed gold standard for high-resolution 1024x1024 anime art, Danbooru tag fidelity, and artist styles.

---
### 🔹 Pony-Diffusion-V6-XL
- **Organization / Creator**: AstraliteHeart
- **Parameter Count**: `3.5B`
- **Official Hugging Face / Source**: [Pony-Diffusion-V6-XL on Hub](https://huggingface.co/Linaqruf/animagine-xl-3.1)
- **License**: `Fair AI Public License`
- **AOMe Use Case**: Exceptional anatomical coherence, dynamic posing, and character design for cartoons and anime.

---
### 🔹 AnimateDiff-Anime (Motion Module v3)
- **Organization / Creator**: guoyww / AnimateDiff team
- **Parameter Count**: `1.5B (SDXL + Motion LoRA)`
- **Official Hugging Face / Source**: [AnimateDiff-Anime (Motion Module v3) on Hub](https://huggingface.co/guoyww/animatediff-motion-adapter-v1-5-3)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Converts 2D anime illustrations into fluid, looping anime animation clips and GIFs.

---
### 🔹 LivePortrait Anime
- **Organization / Creator**: Kuaishou / KwaiVGI
- **Parameter Count**: `1.2B`
- **Official Hugging Face / Source**: [LivePortrait Anime on Hub](https://huggingface.co/KwaiVGI/LivePortrait)
- **License**: `MIT`
- **AOMe Use Case**: Drives 2D anime character portraits with webcam face tracking and voice lip-sync.

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
