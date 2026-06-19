class Duck:
    def speak(self):
        print("Quack")

class Human:
    def speak(self):
        print("Hello")

def call_speak(obj):
    obj.speak()

call_speak(Duck())
call_speak(Human())