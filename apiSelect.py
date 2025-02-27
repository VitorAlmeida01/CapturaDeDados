import mysql.connector
import time
import datetime

db = mysql.connector.connect(
    host="localhost", 
    user="select_user",
    passwd="boraselecionar123",
    database="python"
)

cursor = db.cursor()
    
def cpu(metrica, codigo):
    medida = int(input("""Qual o tipo de medida que deseja visualizar?\n 
                    Digite 1 para média por máquina (média dos valores de uso de cada máquina selecionada) e 2 para média total. Informe somente números: """))
    
    if medida not in (1, 2):
        print("Informe uma opção válida")
        return cpu(metrica, codigo)

    if metrica == 1:
        if medida == 1:
            contador = 0
            while True:
                comando_sql = """SELECT cpu_percent FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()

                for row in resultado:
                    print(f"CPU: {row[0]}%")

                if contador % 5 == 0:
                    continuar = input("Quer monitorar outros dados? (s/n): ").lower()

                if continuar != "s":
                    print("Monitoramento encerrado.")
                    break
                else:
                    iniciar()
        else:
           contador = 0
           while True:
                comando_sql = """SELECT cpu_byte FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"CPU: {row[0]}%")

                if contador % 5 == 0:
                    continuar = input("Quer monitorar outros dados? (s/n): ").lower()

                if continuar != "s":
                    print("Monitoramento encerrado.")
                    break
                else:
                    iniciar()
            
def ram(metrica2, codigo2):
    codigo = int(input("Informe o código da máquina que você deseja monitorar: "))

    componente = int(input("""Informe o componente que você deseja monitorar:
                       [1] - CPU
                       [2] - RAM
                       [3] - DISCO
                       [4] - TODOS
                       Informe somente números: """))
    


# def disco():
# def todos():

def iniciar():
    codigo = int(input("Informe o código da máquina que você deseja monitorar: "))

    componente = int(input("""Informe o componente que você deseja monitorar:
                       [1] - CPU
                       [2] - RAM
                       [3] - DISCO
                       [4] - TODOS
                       Informe somente números: """))
    
    if componente not in [1, 2, 3, 4]:
        print("Informe uma opção válida")
        return iniciar


    metrica = int(input("Qual a métrica que você deseja visualizar? digite 1 para Percentual e 2 para Bytes. Informe somente números: "))

    if componente == 1:
        cpu(metrica, codigo)
    if componente == 2:
        ram(metrica, codigo)
    

iniciar()



