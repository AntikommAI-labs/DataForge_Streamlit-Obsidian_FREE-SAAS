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
