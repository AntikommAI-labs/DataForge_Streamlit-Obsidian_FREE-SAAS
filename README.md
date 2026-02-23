# DataForge_Streamlit-Obsidian_FREE-SAAS

# 🛸 Antigravity Core : Souveraineté Numérique par Design

Système de gestion et de sécurité **Offline-First**, fusionnant la puissance de calcul de **Streamlit** (Actionneur) et la gestion de connaissance d'**Obsidian** (Mémoire).

## 🗺️ Roadmap & Todo

* [x] **Core :** Liaison bidirectionnelle Streamlit ↔ Obsidian via Markdown/YAML.
* [x] **Interface :** Intégration Custom Frames (UI unifiée).
* [ ] **Module PME :** Générateur de devis/factures avec moteur de calcul local.
* [ ] **Module Ghost :** Forge d'identités, scrubber de métadonnées et watcher de compromission.
* [ ] **God Mode :** Connexion LLM pour modification de l'UI en temps réel.

---

## 🛠️ Tutoriel Step-by-Step : L'Assemblage

### 1. Préparation de la Mémoire (Obsidian)

* Crée un nouveau Vault : `Antigravity_Vault`.
* Installe le plugin **Custom Frames**.
* Structure tes dossiers :
* `📂 10_GHOST_FORGE` (Usage expert/furtif)
* `📂 20_PME_SOUVERAINE` (Usage gestion/pro)
* `📂 99_SYSTEM` (Scripts et templates)



### 2. Installation du Moteur (Python)

Dans ton terminal :

```bash
# 1. Créer l'environnement
mkdir Antigravity_Project && cd Antigravity_Project
python -m venv env && source env/bin/activate

# 2. Installer les briques (100% Gratuit)
pip install streamlit pandas pyyaml fpdf2 piexif pillow watchdog

```

### 3. Le Pont (Liaison Visuelle)

* Lance ton app : `streamlit run app.py`.
* Dans Obsidian, configure Custom Frames sur `http://localhost:8501`.
* **Résultat :** Ton application Python est désormais une partie native de ton second cerveau.

---

## 📝 Prompts de Génération d'Interface (IA)

### Cas n°1 : La PME de Marc (L'Utilité)

> **Prompt :** *"Génère une interface Streamlit pour une PME. Inclus un onglet 'CRM' pour créer des fiches clients en Markdown dans le dossier './20_PME_SOUVERAINE/' et un onglet 'Facturation' qui calcule automatiquement la TVA et exporte un devis formaté. Le style doit être pro et épuré."*

### Cas n°2 : L'ID Forge d'Alpha (La Puissance)

> **Prompt :** *"Génère une interface Streamlit nommée 'Ghost Forge'. Inclus un module de 'Nettoyage EXIF' utilisant piexif, un sélecteur de score de compromission (1 à 5), et une fonction qui génère une note Obsidian contenant les identifiants d'un avatar furtif dans './10_GHOST_FORGE/'. Style Dark Cyberpunk."*

---

## ⚡ Bonus : Le "God Mode" (Watcher UI)

Voici le script `watcher.py` qui permet de modifier ton interface en temps réel depuis Obsidian.

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class UIWatcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("UI_CONFIG.md"):
            print("Modification détectée dans Obsidian...")
            # Ici, tu connectes ton LLM (Ollama/OpenAI) 
            # pour lire le fichier et réécrire app.py
            # prompt = read("UI_CONFIG.md") -> LLM -> write("app.py")

observer = Observer()
observer.schedule(UIWatcher(), path='./Antigravity_Vault/99_SYSTEM/', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

```

###
