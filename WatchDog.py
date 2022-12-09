import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/inno/Desktop"

class FileHandler(FileSystemEventHandler):
     def on_created(self, event):
         print(f"Created {event.src_path}")
     def on_deleted(self, event):
         print(f"Oops deleted {event.src_path}")
     def on_modified(self, event): 
         print(f"Modified {event.src_path}")
     def on_moved(self, event): 
         print(f"Moved {event.src_path}")

observer = Observer()
x = FileHandler()
observer.schedule(x,from_dir,recursive=True)
observer.start()

try:
   while True:
    time.sleep(2)
    y = FileHandler()
    print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()
