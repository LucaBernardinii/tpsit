import os
import multiprocessing

def calcolax():
    print("Elab. parallela x = 5 + 3")
    x = 5+ 3
    return x

def calcolay():
    print("Elab. parallela y = 4 - 2")
    y = 4 - 2
    return y

if __name__ == "__main__":
    pid = os.fork()
    if pid == 0:
        print("Sono il figlio.")
        x = calcolax()
        os._exit(x)
    else:
        print("Sono il padre.")
        y = calcolay()

pid, status = os.wait()
x = os.WEXITSTATUS(status)
p = x * y
print(f"p = {p}")