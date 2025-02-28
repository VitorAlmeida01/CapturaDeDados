import mysql.connector  # Biblioteca para conexão com o mysql
import time  # Biblioteca para contar o tempo
import psutil  # Biblioteca para captura dos recursos computacionais
from mysql.connector import Error

def obter_dados():
    cpuPercent = psutil.cpu_percent(interval=1)  # Porcentagem em uso do CPU
    cpuFreq = psutil.cpu_freq().max
    cpuByte = psutil.cpu_freq().current

    diskUsage = psutil.disk_usage('/')
    diskUsageTotal = round(diskUsage.total / (1024**3), 2)  # Total do disco em GB
    diskPercent = psutil.disk_usage('/').percent # Trocar para discol local C: caso o SO seja windows
    diskByte = psutil.disk_usage('/').used


    memory = psutil.virtual_memory()

    memoryTotal = round(memory.total / (1024**3), 2)  # Total de memória RAM
    memoryPercent = psutil.virtual_memory().percent
    memoryByte = psutil.virtual_memory().used


    return cpuPercent, memoryPercent, diskPercent, memoryTotal, cpuFreq, diskUsageTotal, memoryByte, diskByte, cpuByte

# Efetua a conexão com o banco de dados
mydb = mysql.connector.connect(
    host="10.18.32.65",
    user="insert_user",
    password="borainserir123",
    database="python"
)

mydb2 = mysql.connector.connect(
    host="10.18.32.65", 
    user="select_user",
    passwd="boraselecionar123",
    database="python"
)

print(mydb)

mycursor = mydb.cursor()
mycursor2 = mydb2.cursor()

dados = obter_dados() # Atribuo a função de captura de dados a uma variável


ramTotal = dados[3]
cpuTotal = dados[4]
diskTotal = dados[5]
ramByte = dados[6]
diskByte = dados[7]
cpuByte = dados[8]


cod_maq = input("Digite o código da sua máquina (caso ja tenha um codigo).")

sql3 = f"Select cod from maquina where cod = {cod_maq}"
mycursor2.execute(sql3)
resultado = mycursor2.fetchone()

if resultado is None:
    sql2 = "Insert into maquina values (%s, %s, %s, %s)"
    val2 = (cod_maq, ramTotal, cpuTotal, diskTotal )
    mycursor.execute(sql2, val2)
    mydb.commit()


# Loop que sempre será verdadeiro até que o usuario interrompa
while True:
    # Perguntar ao usuário qual informação deseja ver

    cpu_percent = dados[0]
    ram_percent = dados[1]
    disk_percent = dados[2]
    ramByte = dados[6]
    diskByte = dados[7]
    cpuByte = dados[8]

        # Crio o comando de INSERT no banco
    sql = "INSERT INTO dados (cpu_percent, ram_percent, disk_percent, cpu_byte, ram_byte, disk_byte, fkMaquina) VALUES(%s, %s, %s, %s, %s, %s, %s);"
    val = (cpu_percent, ram_percent, disk_percent, cpuByte, ramByte, diskByte, cod_maq)
        
        # Executo o comando sql e os valores de seus respectivos campos que serão enviados para o banco
    mycursor.execute(sql, val)
    mydb.commit()

        # Exibe os dados que foram inseridos
    print("\n---- Dados de CPU ----")
    print(f"Porcentagem da cpu: {cpu_percent}")
  

    print("\n---- Dados de RAM ----")
    print(f"Porcentage de RAM: {ram_percent}")


    print("\n---- Dados de Disco ----")
    print(f"Porcentagem do disco: {disk_percent}GB \n")

    print('-------------------------------------------')

    # Pausa o código por 2 segundos antes de repetir o loop
    time.sleep(2)
