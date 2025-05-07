import json
import os

# Dossier ou les cartes seront sauvegardees
DATA_DIR = "data"

# Sauvegarde une carte mentale dans un fichier JSON
def save_mindmap(manager, filename):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"{filename}.json")
    with open(path, "w") as f:
        json.dump(manager.to_dict(), f, ensure_ascii=False, indent=2)

# Charge une carte depuis un fichier
def load_mindmap(filename):
    path = os.path.join(DATA_DIR, f"{filename}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        from .manager import MindMapManager
        data = json.load(f)
        return MindMapManager.from_dict(data)

# Retourne la liste des cartes disponibles
def list_mindmaps():
    if not os.path.exists(DATA_DIR):
        return []
    return [f[:-5] for f in os.listdir(DATA_DIR) if f.endswith(".json")]
