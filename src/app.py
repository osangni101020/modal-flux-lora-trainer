import subprocess
import os
from modal import (App, Image, web_server, Secret)

image = (
    Image.debian_slim(python_version="3.11")
    .apt_install("libgl1", "libglib2.0-0", "git")
    .run_commands("git clone https://github.com/ostris/ai-toolkit.git /root/ai-toolkit")
    .run_commands("cd /root/ai-toolkit && git submodule update --init --recursive")
    .run_commands("pip install -r /root/ai-toolkit/requirements.txt")
    .copy_local_file("src/flux_train_lora_ui_wrapper.py", "/root/ai-toolkit/flux_train_lora_ui_wrapper.py")

)

app = App(
    "train-flux-lora",
    image=image,
    secrets=[Secret.from_name("huggingface-secret")]
)


@app.cls(
    gpu="A100",
    image=image,
    concurrency_limit=1,
    timeout=7200,  # Default is 2 hrs,change it based on your needs
    allow_concurrent_inputs=100,
)
class App:
    def run_gradio(self, port):
        os.chdir("/root/ai-toolkit")
        cmd = f"python flux_train_lora_ui_wrapper.py --host 0.0.0.0 --port {port}"
        subprocess.Popen(cmd, shell=True)

    @web_server(8000, startup_timeout=120)
    def ui(self):
        self.run_gradio(8000)
