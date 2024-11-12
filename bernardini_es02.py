from threading import Thread
from time import sleep
def codice_thread(arg):
    for x in range(arg):
        print(f"sto contando {x}")
        sleep(1)
        
thread = Thread(target = codice_thread, args = (5,))
thread.start()
thread.join()
print("thread terminato . fine programma!")