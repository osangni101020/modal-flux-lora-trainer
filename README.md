# Train Flux LoRA on Modal

Use [ai-toolkit](https://github.com/ostris/ai-toolkit) to train your Flux LoRA on [Modal](https://modal.com/) with Gradio UI.
No need to setup anything. Just deploy the app and train your LoRA from the UI.

It is useful for training on GPUs with large VRAM like A10G, A100, H100 etc. You can checkout the GPU pricing [here](https://modal.com/pricing).

## Demo

[![Video](./youtube-video.gif)](https://www.youtube.com/watch?v=qAXAkSniSKs)

## How to deploy

1. Signup for Modal Labs
2. Create hugging face token with **write** access to HuggingFace
3. Add token to env variable under the name `HF_TOKEN` to Modal secrets. Use the name `huggingface-secret` for secret
4. Deploy the app using below commands

```sh
# 1. create virtual env (Optional)
python -m venv .venv
source .venv/bin/activate

# 2. install modal
pip install modal

# 3. setup modal - one time setup
modal setup

# 4. deploy the app
modal deploy src/app.py
```

## Training

1. Open the app URL in the browser
2. Name your LoRA, add trigger keyword, upload your dataset, configure training parameters and start training
3. Once training is complete, your LoRA will be saved to HuggingFace repo

## Training config

If you want to use advanced options during the training, you can refer to this [config](https://github.com/ostris/ai-toolkit/blob/main/config/examples/train_lora_flux_24gb.yaml) on ai-toolkit
