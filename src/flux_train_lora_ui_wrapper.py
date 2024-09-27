# wrapper for running gradio ui which allows changing host and port
from flux_train_ui import demo

demo.queue(max_size=5)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str)
    parser.add_argument("--port", type=int)
    args = parser.parse_args()
    demo.launch(server_name=args.host, server_port=args.port)
