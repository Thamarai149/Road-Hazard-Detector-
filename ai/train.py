import argparse
import importlib

YOLO = None
try:
    mod = importlib.import_module("ultralytics.yolo")
    YOLO = getattr(mod, "YOLO", None)
except Exception:
    try:
        mod = importlib.import_module("ultralytics")
        YOLO = getattr(mod, "YOLO", None)
    except Exception:
        YOLO = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="ai/dataset.yaml", help="Path to dataset YAML")
    parser.add_argument("--model", default="yolov8n.pt", help="Base model to fine-tune")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch", type=int, default=16)
    args = parser.parse_args()

    if YOLO is None:
        raise RuntimeError("ultralytics YOLO package not installed")

    model = YOLO(args.model)
    # This uses ultralytics .train API
    model.train(data=args.data, epochs=args.epochs, batch=args.batch)


if __name__ == '__main__':
    main()
