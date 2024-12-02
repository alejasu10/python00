""" from urllib.request import urlopen

page= urlopen("http://info.cern.ch/")
content = page.read()
print(content) """

##
# ejercio 1. pruebas con el entorno virtual
""" import time as t
from tqdm import tqdm
for i in tqdm(range(100)):
    t.sleep(0.5)
 """
### Todo se ejecuta en maquina virtual
import schedule as sc
import time as t
from tqdm import tqdm

def task1():
    print("iniciando tarea")
    for i in tqdm(range(100)):
        t.sleep(0.5)
def task3():
    print("iniciando tarea")
    for i in tqdm(range(100)):
        t.sleep(0.5)
def task2():
    print("iniciando tarea")
    for i in tqdm(range(100)):
        t.sleep(0.5)

sc.every(1).hour.do(task1)
sc.every().day.at("17:37").do(task2)
sc.every().day.monday.do(task3)

while True:
    sc.run_pending()
    t.sleep(1)