# Sub-1B (Real-Time & Edge Transcription)

- **Category**: `03-Speech-To-Text`
- **Parameter Window**: `< 1 Billion Parameters (39M - 769M)`
- **Hardware Footprint**: `500MB - 3GB RAM / CPU capable`

---

## 🤖 Registered Models

### 🔹 Whisper Tiny / Base / Small / Medium
- **Organization / Creator**: OpenAI
- **Parameter Count**: `39M (Tiny), 74M (Base), 244M (Small), 769M (Medium)`
- **Official Hugging Face / Source**: [Whisper Tiny / Base / Small / Medium on Hub](https://huggingface.co/openai/whisper-small)
- **License**: `MIT`
- **AOMe Use Case**: Fast edge voice commands and low-latency whisper.cpp transcription.

---
### 🔹 Moonshine
- **Organization / Creator**: Useful Sensors
- **Parameter Count**: `27M (Tiny) / 62M (Base)`
- **Official Hugging Face / Source**: [Moonshine on Hub](https://huggingface.co/UsefulSensors/moonshine)
- **License**: `MIT`
- **AOMe Use Case**: Optimized sub-second speech-to-text on resource-constrained micro-devices.

---
### 🔹 SenseVoice-Small
- **Organization / Creator**: FunAudioLLM / Alibaba
- **Parameter Count**: `230M`
- **Official Hugging Face / Source**: [SenseVoice-Small on Hub](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)
- **License**: `MIT`
- **AOMe Use Case**: Ultra-fast multi-lingual ASR with emotion recognition and audio event detection.

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
