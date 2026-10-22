# AOMe AI Models Catalog & Registry

Welcome to the **AOMe Open-Source AI Model Knowledge Base and Architecture Registry**.

> [!IMPORTANT]
> **Zero Local Storage Footprint Guarantee**: This repository contains **specifications, model cards, architectural parameters, Hugging Face endpoints, and deployment configs only**.
> **No heavy binary model weights (.safetensors, .bin, .gguf) are stored locally or committed to GitHub.**
> Models are downloaded directly on-demand into cloud instances (RunPod, Lambda, Modal, Google Colab) or streamed via Hugging Face Hub / Ollama without overloading local disk space.

---

## 📂 Architecture & Niche Hierarchy

Every niche is organized into its own folder, structured systematically **from the smallest parameter footprint (<1B) up to massive billions and trillions of parameters (MoE)**:

| # | Category | Core Examples | AOMe Primary Use Case |
|---|---|---|---|
| **01** | [**Chat-LLM**](./01-Chat-LLM/README.md) | Qwen 2.5, Mistral, Gemma 2, Llama 3.3, DeepSeek-V3 | Conversational AI, chatbots, cognitive reasoning |
| **02** | [**Image-Generation**](./02-Image-Generation/README.md) | Stable Diffusion (1.5, XL, 3.5), FLUX.1, PixArt | Visual asset generation, UI styling, art design |
| **03** | [**Speech-To-Text**](./03-Speech-To-Text/README.md) | Whisper (Tiny to Large-v3), Moonshine, Canary | Real-time transcription, meeting notes, voice input |
| **04** | [**Text-To-Speech**](./04-Text-To-Speech/README.md) | Piper, Kokoro-82M, CosyVoice, F5-TTS | Ultra-low latency voice synthesis & voice agents |
| **05** | [**Music-Generation**](./05-Music-Generation/README.md) | MusicGen (Small to Large), Stable Audio Open | Instrumental beats, background tracks, foley audio |
| **06** | [**Embeddings**](./06-Embeddings/README.md) | BGE-M3, ModernBERT, E5-Mistral-7B, NV-Embed-v2 | RAG retrieval, vector search, semantic clustering |
| **07** | [**Vision**](./07-Vision/README.md) | SmolVLM, Qwen2-VL, PaliGemma 2, Pixtral | UI/UX diagram reading, OCR, multimodal reasoning |
| **08** | [**Code-Generation**](./08-Code-Generation/README.md) | Qwen2.5-Coder (0.5B-32B), DeepSeek-Coder-V2 | Real-time autocompletion, coding agents, unit tests |

---

## 📈 Parameter Tiers Progression

Across every niche, models are classified into intuitive sizing tiers:
1. `1_Sub-1B`: Under 1 Billion (15M - 999M) &rarr; Zero-latency, edge, mobile NPU, CPU-capable.
2. `2_1B-7B`: 1 to 7 Billion &rarr; Ideal for consumer laptops and single GPUs (4GB-8GB VRAM).
3. `3_7B-30B`: 7 to 30 Billion &rarr; Workstation class (12GB-24GB VRAM like RTX 3060/4070/4090 or Apple Silicon).
4. `4_30B-70B`: 30 to 70 Billion &rarr; Dual GPU / High-end workstation (32GB-80GB VRAM).
5. `5_70B-100B+`: 70 to 100B+ Dense Flagships &rarr; Enterprise multi-GPU setups.
6. `6_MoE-Trillion+`: Sparse Mixture-of-Experts (671B DeepSeek, 314B Grok, 1.6T Switch) &rarr; Distributed cloud clusters.

---

## 🚀 How to Run Models Remotely or On-Demand

### 1. Using Ollama (Streamed to Local GPU/CPU without storing Git weights)
```bash
# Run lightweight Qwen 2.5
ollama run qwen2.5:7b

# Run DeepSeek-R1 reasoning distilled
ollama run deepseek-r1:8b

# Run state-of-the-art coding model
ollama run qwen2.5-coder:7b
```

### 2. Using vLLM in Cloud (RunPod / Modal / GCP)
```bash
pip install vllm
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-Coder-32B-Instruct \
    --tensor-parallel-size 2
```

### 3. Using Hugging Face Inference API / Serverless
```python
import requests

API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
```
