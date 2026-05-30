# SistemaAgendamentoAtividades

Projeto desenvolvido para a disciplina de **Análise e Projeto de Algoritmos** da Universidade Federal da Bahia (UFBA - 2026.1).

## Integrantes da Dupla
- [Nicole Silva](https://github.com/Nicolesilvaa)
- [Yuri Chagas](https://github.com/Snorlaxch)  

## Objetivo

> Desenvolver um sistema capaz de selecionar o maior número possível de atividades sem conflito de horários, além de comparar diferentes abordagens algorítmicas para o problema.
***

## Caso de uso
> Uma empresa organiza diariamente treinamentos, palestras e reuniões. Entretanto muitas atividades possuem conflito
de horário, dificultando o planejamento adequado da agenda.
Diante disso, a empresa deseja desenvolver um sistema capaz de selecionar o maior número possível de atividades
sem sobreposição de horários.

**Além disso, o sistema deverá permitir:**
- Organização das atividades
- Busca de atividades
- Comparação entre as soluções
- Análise de desempenho dos algoritmos

**Cada atividade possui:**
- Código da atividade
- Nome da atividade
- Horário de início
- Horário de fim
- Prioridade
- Quantidade de participantes

> O sistema deverá determinar quais atividades podem ser selecionadas sem conflito de horários.
> O sistema deverá possuir funcionalidades como: cadastro de atividades, organização de atividades (ordenar atividades
> por horário de início, horário de término e prioridade), seleção de atividades e comparação entre estratégias utilizadas.

## Funcionalidades

- Cadastro de atividades
- Organização de atividades (ordenadas por diferentes critérios)
- Seleção de atividades sem sobreposição
- Comparação entre algoritmos
- Análise de desempenho

## Algoritmos Utilizados

- Merge Sort (para ordenação)
- Algoritmo Guloso (seleção de atividades)
- Programação Dinâmica (maximização de benefício)

## Testes

O sistema será testado com três conjuntos de dados:

- Pequeno (5 a 8 atividades)
- Médio (10 a 20 atividades)
- Grande (mais de 30 atividades)

## Tecnologias

- Python 3

## Execução

```bash
python src/Main.py
