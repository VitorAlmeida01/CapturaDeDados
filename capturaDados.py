import mysql.connector  # Biblioteca para conexão com o mysql
import time  # Biblioteca para contar o tempo
import psutil  # Biblioteca para captura dos recursos computacionais

def obter_dados():
    cpuPercent = psutil.cpu_percent(interval=1)  # Porcentagem em uso do CPU
    cpuCore = psutil.cpu_count(logical=False)  # Número de núcleos físicos da CPU
    cpuCore2 = psutil.cpu_count(logical=True)  # Número de núcleos logicos da CPU

    diskUsage = psutil.disk_usage('/')
    diskUsageTotal = round(diskUsage.total / (1024**3), 2)  # Total do disco em GB
    diskUsageFree = round(diskUsage.free / (1024**3), 2)  # Total de de disco livre em GB

    memory = psutil.virtual_memory()
    memoryAvailable = round(memory.available / (1024**3), 2)  # Total de memória RAM disponível
    memoryTotal = round(memory.total / (1024**3), 2)  # Total de memória RAM
    memoryUsed = round(memory.used / (1024 ** 3), 2)  # Total de memória RAM sendo usada

    internet = psutil.net_io_counters()
    intSent = round(internet.bytes_sent / (1024 ** 2), 2)  # Upload
    intRec = round(internet.bytes_recv / (1024 ** 2), 2)  # Download

    return cpuCore, cpuCore2, cpuPercent, diskUsageTotal, diskUsageFree, memoryTotal, memoryAvailable, memoryUsed, intSent, intRec

# Efetua a conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="aulaPython"
)

print(mydb)

mycursor = mydb.cursor()

# Loop que sempre será verdadeiro até que o usuario interrompa
while True:
    # Perguntar ao usuário qual informação deseja ver
    user_input = input("Digite 'cpu' para ver dados de CPU, 'ram' para RAM, 'disco' para Disco, 'rede' para Rede ou 'sair' para encerrar: ").lower()

    if user_input == 'cpu' or user_input == 'ram' or user_input == 'disco' or user_input == 'rede':
        dados = obter_dados()  # Atribuo a função de captura de dados a uma variável

        # Atribuo o valor de cada posição do array que contém os dados dos recursos computacionais em variáveis
        cpuCore = dados[0]
        cpuCore2 = dados[1]
        cpuPercent = dados[2]
        diskUsageTotal = dados[3]
        diskUsageFree = dados[4]
        memoryTotal = dados[5]
        memoryAvailable = dados[6]
        memoryUsed = dados[7]
        intSent = dados[8]
        intRec = dados[9]

        # Crio o comando de INSERT no banco
        sql = "INSERT INTO dados (cpuCore, cpuCoreLog, cpuPercent, diskTotal, diskFree, ramTotal, ramLivre, ramUsed, intRec, intSent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        val = (cpuCore, cpuCore2, cpuPercent, diskUsageTotal, diskUsageFree, memoryTotal, memoryAvailable, memoryUsed, intRec, intSent)
        
        # Executo o comando sql e os valores de seus respectivos campos que serão enviados para o banco
        mycursor.execute(sql, val)
        mydb.commit()

        # Exibe os dados que foram inseridos
        if user_input == 'cpu':
            print("\n---- Dados de CPU ----")
            print(f"CPU em uso: {cpuPercent}%")
            print(f"Quantidade de núcleos físicos do processador: {cpuCore}")
            print(f"Quantidade de núcleos lógicos do processador: {cpuCore2}")

        elif user_input == 'ram':
            print("\n---- Dados de RAM ----")
            print(f"Quantidade de RAM total: {memoryTotal}GB")
            print(f"Quantidade de RAM disponível: {memoryAvailable}GB")
            print(f"Quantidade de RAM sendo usada: {memoryUsed}GB")

        elif user_input == 'disco':
            print("\n---- Dados de Disco ----")
            print(f"Armazenamento total do disco: {diskUsageTotal}GB")
            print(f"Armazenamento livre do disco: {diskUsageFree}GB")

        elif user_input == 'rede':
            print("\n---- Dados de Rede ----")
            print(f"Download: {intRec}MB")
            print(f"Upload: {intSent}MB")

    elif user_input == 'sair':
        # Encerra o loop se o usuário digitar 'sair'
        print("Saindo...")
        break

    # Pausa o código por 2 segundos antes de repetir o loop
    time.sleep(2)
