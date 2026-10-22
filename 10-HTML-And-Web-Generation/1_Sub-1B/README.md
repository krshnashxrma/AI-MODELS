# Sub-1B (DOM & Layout Parsers)

- **Category**: `10-HTML-And-Web-Generation`
- **Parameter Window**: `< 1 Billion Parameters`
- **Hardware Footprint**: `1GB - 2GB RAM / CPU`

---

## 🤖 Registered Models

### 🔹 LayoutLMv3
- **Organization / Creator**: Microsoft
- **Parameter Count**: `133M - 368M`
- **Official Hugging Face / Source**: [LayoutLMv3 on Hub](https://huggingface.co/microsoft/layoutlmv3-base)
- **License**: `CC-BY-NC-SA 4.0`
- **AOMe Use Case**: Multi-modal layout understanding: links visual bounding boxes with HTML/DOM coordinate trees.

---
### 🔹 Pix2Code
- **Organization / Creator**: tonybeltramelli
- **Parameter Count**: `150M`
- **Official Hugging Face / Source**: [Pix2Code on Hub](https://github.com/tonybeltramelli/pix2code)
- **License**: `Apache 2.0`
- **AOMe Use Case**: Translates graphical user interface screenshots directly into valid HTML/CSS code.

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
