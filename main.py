import random
import time

class PollingLogic:
    def __init__(self, jitter_range):
        self.jitter_range = jitter_range
        self.last_request_time = time.time()

    def get_translation_result(self):
        # Simulate translation result
        result = "Translation result"

        # Jitter logic
        jitter_time = random.uniform(-self.jitter_range, self.jitter_range)
        sleep_time = max(0, 0.1 + jitter_time)

        # Polling logic
        while True:
            current_time = time.time()
            if current_time - self.last_request_time >= sleep_time:
                self.last_request_time = current_time
                return result
            time.sleep(0.01)

# Misol foydalanuvchi
polling_logic = PollingLogic(jitter_range=0.5)
print(polling_logic.get_translation_result())
```

Kodda `PollingLogic` klassi yaratilib, unda `jitter_range` parametriga asosan jitter logigasi ishlaydi. `get_translation_result` metodida polling logigasi ishlaydi. Jitter logigasi uchun `random.uniform` funksiyasi ishlatilib, polling logigasi uchun `time.sleep` funksiyasi ishlatiladi.
