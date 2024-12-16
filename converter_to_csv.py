import os
from bs4 import BeautifulSoup
import pandas as pd

# Script para extrair palavras japonesas de arquivos HTML exportados do Telegram
# Objetivo: Converter mensagens de conversas de aprendizado de japonês em uma planilha CSV estruturada

# Lista de arquivos HTML de origem que contêm as mensagens
file_paths = ["messages.html", "messages2.html"]

# Lista para armazenar os dados extraídos
data = []

# Itera sobre cada arquivo HTML na lista
for file_path in file_paths:
    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        continue

    # Abre e analisa o arquivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        # Usa BeautifulSoup para parsear o HTML
        soup = BeautifulSoup(file, 'html.parser')
        
        # Encontra todas as divs com classe "text" que contêm as mensagens
        for div in soup.find_all("div", class_="text"):
            # Obtém o texto da div, removendo espaços extras
            text = div.get_text(strip=True)
            
            # Verifica se a mensagem contém bandeiras do Japão e Brasil (formato específico)
            if "🇯🇵" in text and "🇧🇷" in text:
                # Divide o texto usando as bandeiras como separadores
                parts = text.split("🇯🇵")[1].split("🇧🇷")
                jp_part = parts[0].strip()
                pt_part = parts[1].strip()
                
                # Extrai palavra, leitura e tradução
                # Formato esperado: Palavra 【Leitura】 🇧🇷 Tradução
                if "【" in jp_part and "】" in jp_part:
                    word, reading = jp_part.split("【")
                    reading = reading.strip("】")
                    
                    # Adiciona os dados extraídos à lista
                    data.append({
                        "word": word.strip(), 
                        "reading": reading.strip(), 
                        "translation-pt-br": pt_part, 
                        "jlpt": "N5"  # Nível JLPT padrão (pode ser ajustado)
                    })

# Cria um DataFrame do pandas com os dados extraídos
df = pd.DataFrame(data)

# Adiciona uma coluna de ID sequencial
df.insert(0, 'id', range(1, len(df) + 1))

# Define o diretório de saída para o arquivo CSV
output_dir = "\data"

# Cria o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Caminho completo para o arquivo CSV
output_path = os.path.join(output_dir, "word_list.csv")

# Salva o DataFrame como um arquivo CSV
df.to_csv(output_path, index=False)

# Mensagens de confirmação
print(f"Palavras salvas em {output_path}")
print(f"Total de palavras extraídas: {len(df)}")