import pandas as pd
from tabulate import tabulate

def visualize_csv(file_path):
    """
    Função para visualizar o conteúdo de um arquivo CSV no terminal.
    
    Recursos:
    - Carrega o arquivo CSV usando pandas
    - Exibe as primeiras linhas em uma tabela formatada
    - Permite ao usuário visualizar mais linhas interativamente
    
    Tratamento de erros:
    - Lida com arquivos não encontrados
    - Lida com arquivos vazios
    - Lida com erros de parsing do CSV
    
    Args:
        file_path (str): Caminho completo para o arquivo CSV
    """
    try:
        # Carrega o arquivo CSV usando pandas
        df = pd.read_csv(file_path)

        # Exibe as primeiras linhas do arquivo CSV
        # Usa tabulate para formatação de tabela no terminal
        print(tabulate(df.head(), headers='keys', tablefmt='psql'))

        # Loop interativo para visualização de mais linhas
        while True:
            # Pergunta ao usuário se deseja ver mais linhas
            choice = input("Do you want to view more rows? (yes/no): ")
            
            if choice.lower() == 'yes':
                # Solicita o número de linhas a serem exibidas
                num_rows = int(input("Enter the number of rows to view: "))
                
                # Exibe as linhas solicitadas
                print(tabulate(df.head(num_rows), headers='keys', tablefmt='psql'))
            
            elif choice.lower() == 'no':
                # Encerra a visualização se o usuário escolher 'no'
                break
            
            else:
                # Trata entradas inválidas
                print("Invalid choice. Please enter 'yes' or 'no'.")

    # Tratamento de exceções específicas
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"The file {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error parsing the file {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Caminho padrão para o arquivo CSV gerado
path = "data\word_list.csv"

# Chama a função de visualização com o caminho do arquivo
visualize_csv(path)