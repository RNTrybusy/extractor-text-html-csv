# Extrator de Palavras

## Visão Geral
Este projeto consiste em scripts Python para extrair palavras japonesas de arquivos HTML de mensagens, criando uma lista de palavras em formato CSV com traduções.

## Funcionalidades
- Extração de palavras japonesas, leituras e traduções em português de arquivos HTML
- Geração de arquivo CSV estruturado com palavras e metadados
- Visualização interativa da lista de palavras no terminal

## Requisitos
- Python 3.x
- Bibliotecas necessárias: 
  - BeautifulSoup
  - pandas
  - tabulate

## Como Usar

### 1. Extração de Palavras
Execute `converter_to_csv.py` para:
- Analisar arquivos de mensagens HTML
- Extrair palavras japonesas com suas leituras e traduções
- Criar um arquivo CSV no diretório `data`

### 2. Visualização das Palavras
Execute `csv_visualizator.py` para:
- Visualizar a lista de palavras extraídas no terminal
- Navegar interativamente pelas linhas

## Configuração
- Modifique a lista `file_paths` em `converter_to_csv.py` para incluir seus arquivos HTML
- Ajuste `output_dir` para alterar o local de salvamento do CSV

## Formato dos Dados
- ID: Identificador único
- Palavra: Palavra em japonês
- Leitura: Leitura da palavra em kana
- Tradução: Tradução para português
- JLPT: Nível do Teste de Proficiência em Língua Japonesa

## Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Problemas Conhecidos
- Atualmente, o script assume um formato específico de mensagem com bandeiras 🇯🇵 e 🇧🇷
- Pode precisar de ajustes para diferentes formatos de exportação de mensagens

___
# Japanese Word Extractor

## Overview
This project provides a set of Python scripts to extract Japanese words from HTML message files and create a CSV word list with translations.

## Features
- Extract Japanese words, readings, and Portuguese translations from HTML files
- Generate a structured CSV file with words and metadata
- Visualize the extracted word list in the terminal

## Requirements
- Python 3.x
- Libraries: 
  - BeautifulSoup
  - pandas
  - tabulate

## How to Use

### 1. Extract Words
Run `converter_to_csv.py` to:
- Parse HTML message files
- Extract Japanese words with readings and translations
- Create a CSV file in the `data` directory

### 2. Visualize Words
Run `csv_visualizator.py` to:
- View the extracted word list in the terminal
- Interactively browse through rows

## Configuration
- Modify `file_paths` in `converter_to_csv.py` to include your HTML files
- Adjust the `output_dir` to change the CSV save location

## Sample Data Format
- ID: Unique identifier
- Word: Japanese word
- Reading: Japanese reading (in kana)
- Translation: Portuguese translation
- JLPT: Japanese Language Proficiency Test level