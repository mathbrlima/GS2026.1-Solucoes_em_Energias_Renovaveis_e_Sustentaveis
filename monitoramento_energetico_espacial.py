from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

print(Fore.LIGHTCYAN_EX + "============================================")
print(Fore.LIGHTCYAN_EX + " ARES-1 / Monitoramento Espacial Energético")
print(Fore.LIGHTCYAN_EX + "============================================")

# Entrada de dados
print("\nForneça as informações da missão:")

temperatura = float(input("Informe a temperatura (°C): "))
energia = float(input("Informe o nível de energia (%): "))
comunicacao = float(input("Informe a comunicação (%): "))
energia_solar = float(input("Informe a geração de energia solar (kW): "))
consumo = float(input("Informe o consumo energético (kW): "))

# Exibição dos dados
print(Fore.LIGHTCYAN_EX + "\n--- ESTATÍSTICAS DA NAVE ---")

print(f"Temperatura: {temperatura}°C")
print(f"Energia: {energia}%")
print(f"Comunicação: {comunicacao}%")
print(f"Energia Solar: {energia_solar} kW")
print(f"Consumo Energético: {consumo} kW")

# Alertas
print(Fore.LIGHTCYAN_EX + "\n--- ALERTAS ---")

alerta = False

if temperatura > 90:
    print(Fore.LIGHTYELLOW_EX + "⚠ ALERTA: Temperatura crítica!")
    alerta = True

if energia < 20:
    print(Fore.LIGHTYELLOW_EX + "⚠ ALERTA: Energia baixa!")
    alerta = True

if comunicacao < 80:
    print(Fore.LIGHTYELLOW_EX + "⚠ ALERTA: Falha de comunicação!")
    alerta = True

if not alerta:
    print(Fore.LIGHTGREEN_EX + "✅ Nenhum alerta encontrado.")

# Tomada de decisão automática
print(Fore.LIGHTCYAN_EX + "\n--- DECISÃO AUTOMÁTICA (IA) ---")

if energia < 20:
    print(Fore.LIGHTBLUE_EX + "🤖 Ativando modo economia de energia...")
    print(Fore.LIGHTGREEN_EX + "✅ Modo economia ativado!")

elif temperatura > 90:
    print(Fore.LIGHTBLUE_EX + "🤖 Ativando sistema de resfriamento...")
    print(Fore.LIGHTGREEN_EX + "✅ Resfriamento ativado!")

elif comunicacao < 80:
    print(Fore.LIGHTBLUE_EX + "🤖 Reiniciando sistema de comunicação...")
    print(Fore.LIGHTGREEN_EX + "✅ Sistema de comunicação reiniciado!")

else:
    print(Fore.LIGHTGREEN_EX + "✅ Operação normal.")

# Sustentabilidade
print(Fore.LIGHTCYAN_EX + "\n--- SUSTENTABILIDADE ---")

if consumo > 0:
    indice = (energia_solar / consumo) * 100
else:
    indice = 0

saldo = energia_solar - consumo

print(f"Geração Solar: {energia_solar} kW")
print(f"Consumo Energético: {consumo} kW")
print(f"Saldo Energético: {saldo:.2f} kW")
print(f"Índice Sustentável: {indice:.2f}%")

if indice >= 80:
    print(Fore.LIGHTGREEN_EX + "🌱 Missão Sustentável")

elif indice >= 60:
    print(Fore.LIGHTYELLOW_EX + "♻ Boa Eficiência Energética")

else:
    print(Fore.LIGHTRED_EX + "❌ Necessita otimização energética")

print(Fore.LIGHTCYAN_EX + "\n============================================")
print(Fore.LIGHTCYAN_EX + " FIM DO RELATÓRIO DA MISSÃO")
print(Fore.LIGHTCYAN_EX + "============================================")