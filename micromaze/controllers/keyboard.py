from..events import tick_event


class KeyboardController:
    
    def __init__(self):
        tick_event.subscribe(self.on_tick)

    
    def on_tick(self):
        print("j ecoute l utilisateur")