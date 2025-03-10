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

    internet = psutil.net_io_counters()
    redeRecebida = round(internet.bytes_recv/(1024 ** 2), 2)
    redeEnviada = round(internet.bytes_sent/(1024 ** 2), 2)


    return cpuPercent, memoryPercent, diskPercent, memoryTotal, cpuFreq, diskUsageTotal, memoryByte, diskByte, cpuByte, redeRecebida, redeEnviada

# Efetua a conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="insert_user",
    password="borainserir123",
    database="python"
)

mydb2 = mysql.connector.connect(
    host="localhost", 
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
internetTotal = dados[9]
ramByte = dados[6]
diskByte = dados[7]
cpuByte = dados[8]



cod_maq = input("Digite o código da sua máquina (caso ja tenha um codigo): ")

sql3 = "SELECT codigoMaquina FROM maquina WHERE codigoMaquina = %s"
mycursor2.execute(sql3, (cod_maq,))
resultado = mycursor2.fetchone()

sql4 = "SELECT idComponentes FROM componentes WHERE fkMaquina = %s"
mycursor2.execute(sql4, (cod_maq,))
resultado_sql4 = mycursor2.fetchone()

if resultado is None:
    print("A sua máquina ainda nescessita de um registro")
else:
    sql2 = "UPDATE maquina SET ram = %s,  cpuFreq = %s,  disk = %s,  redeRecebida = %s WHERE codigoMaquina = %s;"
    val2 = (ramTotal, cpuTotal, diskTotal, internetTotal, cod_maq )
    mycursor.execute(sql2, val2)
    mydb.commit()

while True:
    dados = obter_dados()
    cpu_percent = dados[0]
    ram_percent = dados[1]
    disk_percent = dados[2]
    ramByte = dados[6]
    diskByte = dados[7]
    cpuByte = dados[8]
    interneteUsada = dados[10]

    sql1 = "INSERT INTO dadosDisk (diskPercent, fkComponente, fkMaquina) VALUES(%s, %s, %s);"
    val1 = (disk_percent, resultado_sql4[0], cod_maq)
    mycursor.execute(sql1, val1)

    sql2 = "INSERT INTO dadosCpu (cpuPercent, fkComponente, fkMaquina) VALUES(%s, %s, %s);"
    val2 = (cpu_percent, resultado_sql4[0], cod_maq)
    mycursor.execute(sql2, val2)

    sql3 = "INSERT INTO dadosRam (ramPercent, fkComponente, fkMaquina) VALUES(%s, %s, %s);"
    val3 = (ram_percent, resultado_sql4[0], cod_maq)
    mycursor.execute(sql3, val3)

    sql4 = "INSERT INTO dadosRede (redeEnviada, fkMaquina) VALUES(%s, %s);"
    val4 = (interneteUsada, cod_maq)
    mycursor.execute(sql4, val4)

        
    mydb.commit()
    

    
    time.sleep(2)
