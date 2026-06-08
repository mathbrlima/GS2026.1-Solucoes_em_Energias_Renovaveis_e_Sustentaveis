# GS2026.1 - Soluções em Energias Renováveis e Sustentáveis

## Integrantes: 

Enzo Stahal Freitas | 569001

Matheus Bruno de Lima | 572944


## Sobre o Projeto:

O objetivo do projeto é monitorar condições operacionais de uma missão espacial experimental, analisando informações relacionadas à temperatura, energia, comunicação e sustentabilidade da nave.
A solução utiliza conceitos básicos de programação para gerar alertas automáticos e auxiliar na tomada de decisão diante de situações críticas.

## Objetivo:

Desenvolver um sistema capaz de:

- Coletar dados do usuário
- Monitorar dados operacionais da missão.
- Identificar situações críticas.
- Gerar alertas automáticos.
- Auxiliar na tomada de decisão.
- Avaliar a sustentabilidade energética da missão.

## Funcionalidades
MONITORAMENTO

O usuário informa:

- Temperatura do módulo (°C)
- Nível de energia (%)
- Qualidade da comunicação (%)
- Geração de energia solar (kW)
- Consumo energético (kW)

ALERTAS AUTOMÁTICOS

O sistema identifica:

- Temperatura crítica (temperatura > 90°C)
- Energia baixa (energia < 20%)
- Falhas de comunicação (comunicação < 80%)

TOMADA DE DECISÃO

O sistema realiza ações automatizadas como:

- Ativação do modo economia de energia (energia < 20%)
- Ativação do sistema de resfriamento (temp. > 90°C)
- Reinicialização da comunicação (comun. < 80%)
- Sem Alertas (operação normal é mantida)

SUSTENTABILIDADE

O sistema calcula o Índice Sustentável da missão utilizando a relação entre energia gerada pelos painéis solares e o consumo energético.

## Relação com Energias Renováveis

A missão utiliza energia solar como principal fonte de energia renovável.

O sistema monitora a geração energética dos painéis solares e compara com o consumo da nave, permitindo avaliar a eficiência energética e a sustentabilidade da operação.

## Relação com "inteligência artificial introdutória"

Ultilizamos uma IA baseada em regras. O sistema analisa os dados recebidos e toma decisões automaticamente através de estruturas condicionais. Apesar de ser uma IA introdutória, ela atende ao objetivo proposto pelo desafio, que era implementar tomada de decisão automatizada diante de situações críticas. A lógica if/elif/else garante que apenas uma ação seja executada por ciclo.

## Tecnologias Utilizadas
- Python (linguagem de programação)

- Colorama (biblioteca do Python) - estilização do terminal para destacar visualmente cada seção do sistema, tornando a leitura mais clara e intuitiva ao usuário

## Exemplo de Uso

Temperatura: 95°C

Energia: 15%

Comunicação: 70%

Energia Solar: 80 kW

Consumo: 120 kW

Resultado:

- Alerta de temperatura crítica

- Alerta de energia baixa

- Alerta de comunicação

- Ativação do modo economia de energia

- Cálculo do índice sustentável
