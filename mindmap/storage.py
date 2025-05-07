import json
import os

# Dossier ou les fichiers de cartes sont sauvegardes
DATA_DIR = "data"

def save_mindmap(manager, filename):
    # Sauvegarde la carte sous forme de fichier JSON
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"{filename}.json")
    with open(path, "w") as f:
        json.dump(manager.to_dict(), f, ensure_ascii=False, indent=2)

def load_mindmap(filename):
    # Charge une carte a partir d'un fichier JSON
    path = os.path.join(DATA_DIR, f"{filename}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        from .manager import MindMapManager
        data = json.load(f)
        return MindMapManager.from_dict(data)

def list_mindmaps():
    # Retourne la liste des fichiers .json presents dans le dossier data
    if not os.path.exists(DATA_DIR):
        return []
    return [f[:-5] for f in os.listdir(DATA_DIR) if f.endswith(".json")]
