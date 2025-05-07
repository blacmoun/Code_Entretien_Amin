import json
import os

DATA_DIR = "data"

def save_mindmap(manager, filename):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"{filename}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(manager.to_dict(), f, ensure_ascii=False, indent=2)

def load_mindmap(filename):
    path = os.path.join(DATA_DIR, f"{filename}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        from .manager import MindMapManager
        data = json.load(f)
        return MindMapManager.from_dict(data)

def list_mindmaps():
    if not os.path.exists(DATA_DIR):
        return []
    return [f[:-5] for f in os.listdir(DATA_DIR) if f.endswith(".json")]
