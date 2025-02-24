import threading
import time
import random

BUFFER_SIZE = 10
ITERATIONS = 5

buffer = [0] * BUFFER_SIZE
count = 0  # Número de elementos no buffer
mutex = threading.Lock()
sem_leitor = threading.Semaphore(3)  # Inicializa o semáforo do leitor com 3 permissões
sem_escritor = threading.Semaphore(2)  # Inicializa o semáforo do escritor com 2 permissões

def calcular_e_imprimir_media(leitor_id, iteracao):
    soma = sum(buffer[:count])
    media = soma / count if count > 0 else 0
    print(f"Leitor {leitor_id} (Iteração {iteracao}): Média = {media:.2f}")

def leitor(leitor_id):
    global count  # Adiciona esta linha para indicar que 'count' é uma variável global
    for iteracao in range(ITERATIONS):
        sem_leitor.acquire()
        mutex.acquire()

        while count == 0:
            mutex.release()
            sem_escritor.release()
            sem_leitor.acquire()
            mutex.acquire()

        # Imprimir média antes de liberar o mutex
        calcular_e_imprimir_media(leitor_id, iteracao + 1)

        mutex.release()
        sem_escritor.release()

        # Simula um intervalo de leitura
        time.sleep(random.random())  # Dorme por um tempo aleatório entre 0 e 1 segundo

def escritor(escritor_id):
    global count  # Adiciona esta linha para indicar que 'count' é uma variável global
    for iteracao in range(ITERATIONS):
        sem_escritor.acquire()
        mutex.acquire()

        if count == BUFFER_SIZE:
            # Remove o primeiro elemento do buffer se estiver cheio
            buffer[:-1] = buffer[1:]
            count -= 1

        # Adiciona um novo elemento ao final do buffer
        novo_elemento = random.randint(0, 99)
        buffer[count] = novo_elemento
        count += 1

        print(f"Escritor {escritor_id} (Iteração {iteracao + 1}): Removido primeiro valor e inserido {novo_elemento}")

        # Imprimir média antes de liberar o mutex
        calcular_e_imprimir_media(escritor_id, iteracao + 1)

        mutex.release()
        sem_leitor.release()

        # Simula um intervalo de escrita
        time.sleep(random.random())  # Dorme por um tempo aleatório entre 0 e 1 segundo

if __name__ == "__main__":
    leitores = [threading.Thread(target=leitor, args=(i,)) for i in range(3)]
    escritores = [threading.Thread(target=escritor, args=(i,)) for i in range(2)]

    for leitor_thread in leitores:
        leitor_thread.start()

    for escritor_thread in escritores:
        escritor_thread.start()

    for leitor_thread in leitores:
        leitor_thread.join()

    for escritor_thread in escritores:
        escritor_thread.join()
