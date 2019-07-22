
class Event:

    def __init__(self):
        self.subscribers = []
    
    def subscriber(self, fct):
        self.subscribers.append(fct)
    
    def send(self, **kwargs):
        for subscriber in self.subscribers:
            subscriber(**kwargs)

tick_event = Event()
hero_moved = Event()

def main():
    e = Event()
    def f(**kwargs):
        print(kwargs('message'))
    
    e.subscribe(f)


    e.send(message="hello")

if __name__ == "__main__":
    main()