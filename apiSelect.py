import mysql.connector
import time

db = mysql.connector.connect(
    host="10.18.32.65", 
    user="select_user",
    passwd="boraselecionar123",
    database="python"
)

cursor = db.cursor()
    
def cpu(metrica, codigo):
    medida = int(input("""\nQual o tipo de medida que deseja visualizar? Digite 1 para média por máquina (média dos valores de uso de cada máquina selecionada) e 2 para média total. Informe somente números: """))
    
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
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
        else:
           contador = 0
           while True:
                comando_sql = """SELECT AVG(cpu_percent) FROM dados;"""

                cursor.execute(comando_sql)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"CPU: {row[0]:.2f}%")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
                time.sleep(2)
    else:
        if medida == 1:
            contador = 0
            while True:
                comando_sql = """SELECT cpu_byte FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()

                for row in resultado:
                    print(f"CPU: {row[0]}")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
                time.sleep(2)
        else:
           contador = 0
           while True:
                comando_sql = """SELECT AVG(cpu_byte) FROM dados;"""

                cursor.execute(comando_sql)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"CPU: {row[0]:.2f}")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
                
                time.sleep(2)

            
def ram(metrica, codigo):
    medida = int(input("""\nQual o tipo de medida que deseja visualizar? Digite 1 para média por máquina (média dos valores de uso de cada máquina selecionada) e 2 para média total. Informe somente números: """))
    
    if medida not in (1, 2):
        print("Informe uma opção válida")
        return cpu(metrica, codigo)

    if metrica == 1:
        if medida == 1:
            contador = 0
            while True:
                
                comando_sql = """SELECT ram_percent FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()

                for row in resultado:
                    time.sleep(2)
                    print(f"RAM: {row[0]}%")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()


        else:
           contador = 0
           while True:
                comando_sql = """SELECT AVG(ram_percent) FROM dados;"""

                cursor.execute(comando_sql)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"RAM: {row[0]:.2f}%")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
                time.sleep(2)
        
    else:
        if medida == 1:
            contador = 0
            while True:
                comando_sql = """SELECT ram_byte FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()

                for row in resultado:
                    print(f"RAM: {row[0]}")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
                time.sleep(2)

        else:
           contador = 0
           while True:
                comando_sql = "SELECT AVG(ram_byte) FROM dados;"

                cursor.execute(comando_sql)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"RAM: {row[0]}")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()
                time.sleep(2)


def disco(metrica, codigo):
    medida = int(input("""\nQual o tipo de medida que deseja visualizar? Digite 1 para média por máquina (média dos valores de uso de cada máquina selecionada) e 2 para média total. Informe somente números: """))
    
    if medida not in (1, 2):
        print("Informe uma opção válida")
        return cpu(metrica, codigo)

    if metrica == 1:
        if medida == 1:
            contador = 0
            while True:
                comando_sql = """SELECT disk_percent FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()

                for row in resultado:
                    print(f"DISCO: {row[0]}%")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()

                time.sleep(2)

        else:
           contador = 0
           while True:
                comando_sql = """SELECT AVG(disk_percent) FROM dados;"""

                cursor.execute(comando_sql)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"DISCO: {row[0]:.2f}%")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()

                time.sleep(2)
    else:
        if medida == 1:
            contador = 0
            while True:
                comando_sql = """SELECT disk_byte FROM dados JOIN maquina on fkMaquina = cod
                                 WHERE cod = %s;"""
                
                valores = (codigo,)

                cursor.execute(comando_sql, valores)

                resultado = cursor.fetchall()

                for row in resultado:
                    print(f"DISCO: {row[0]}")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()

                time.sleep(2)

        else:
           contador = 0
           while True:
                comando_sql = """SELECT AVG(disk_byte) FROM dados;"""

                cursor.execute(comando_sql)

                resultado = cursor.fetchall()



                for row in resultado:
                    print(f"DISCO: {row[0]:.2f}")

                if contador % 5 == 0:
                    continuar = input("Quer continuar monitorando? (s/n): ").lower()

                if continuar != "s":
                    outrosComponentes = input("Deseja monitorar outros componentes? (s/n)").lower()
                    if outrosComponentes != "s":
                        print("Monitoramento encerrado")
                        break
                    else:
                        iniciar()

                time.sleep(2)

def iniciar():
    codigo = int(input("Informe o código da máquina que você deseja monitorar: "))

    componente = int(input("""\nInforme o componente que você deseja monitorar:
                       [1] - CPU
                       [2] - RAM
                       [3] - DISCO
                       Informe somente números: """))
    
    if componente not in [1, 2, 3]:
        print("Informe uma opção válida")
        return iniciar


    metrica = int(input("\nQual a métrica que você deseja visualizar? digite 1 para Percentual e 2 para Bytes. Informe somente números: "))

    if componente == 1:
        cpu(metrica, codigo)
    elif componente == 2:
        ram(metrica, codigo)
    elif componente == 3:
        disco(metrica, codigo)
    

iniciar()