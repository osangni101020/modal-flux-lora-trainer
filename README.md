# Train Flux LoRA on Modal

Use [ai-toolkit](https://github.com/ostris/ai-toolkit) to train your Flux LoRA on [Modal](https://modal.com/) with Gradio UI.
No need to setup anything. Just deploy the app and train your LoRA from the UI.

It is useful for training on GPUs with large VRAM like A10G, A100, H100 etc. You can checkout the GPU pricing [here](https://modal.com/pricing).

## How to deploy

1. Signup for Modal Labs
2. Create HF_TOKEN with write access to HuggingFace
3. Add it to Modal secrets under `huggingface-secret`
4. Deploy the app

```sh
# create virtual env (Optional)
python -m venv .venv
source .venv/bin/activate

# install modal
pip install modal

# setup modal - one time setup
modal setup

# run the app
modal deploy src/app.py
```

## Training

1. Open the app URL in the browser
2. Upload your dataset, add keywords, configure training parameters and train your LoRA
3. Once training is complete, your LoRA will be saved to HuggingFace repo
