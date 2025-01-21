import threading
import asyncio
import tkinter as tk

# Basic Hello World
print("Hello, World!")

# Hello World using a function
def hello_world():
    print("Hello, World!")

hello_world()

# Hello World using a class
class HelloWorld:
    def say_hello(self):
        print("Hello, World!")

hw = HelloWorld()
hw.say_hello()

# Hello World using a lambda function
hello = lambda: print("Hello, World")
hello()

# Hello World using a list comprehension
[print("Hello, World!") for _ in range(1)]

# Hello World using a generator
def hello_generator():
    yield "Hello, World!"

for message in hello_generator():
    print(message)

# Hello World using threading

def thread_hello():
    print("Hello, World!")

thread = threading.Thread(target=thread_hello)
thread.start()
thread.join()

# Hello World using asyncio

async def async_hello():
    print("Hello, World!")

asyncio.run(async_hello())

# Hello World using tkinter (GUI)

root = tk.Tk()
label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()