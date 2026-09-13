import pandas as pd

def carregar_dados(caminho_arquivo):
    """Carrega uma planilha de fornecedores em um DataFrame."""
    return pd.read_excel(caminho_arquivo)


def remover_duplicatas(df):
    """Remove registros duplicados com base no CNPJ."""
    return df.drop_duplicates(subset="cnpj", keep="first")


def padronizar_texto(df):
    """Padroniza campos de texto: remove espaços extras e deixa em maiúsculas."""
    colunas_texto = ["nome_fornecedor", "categoria"]
    for coluna in colunas_texto:
        if coluna in df.columns:
            df[coluna] = df[coluna].astype(str).str.strip().str.upper()
    return df


def cruzar_bases(df_fornecedores, df_pedidos, chave="cnpj"):
    """Cruza a base de fornecedores com a base de pedidos usando o CNPJ como chave."""
    return pd.merge(df_fornecedores, df_pedidos, on=chave, how="left")


def exportar_resultado(df, caminho_saida):
    """Exporta o resultado tratado para uma nova planilha."""
    df.to_excel(caminho_saida, index=False)
    print(f"Arquivo exportado com sucesso: {caminho_saida}")


def main():
    # Exemplo de uso com dados fictícios
    fornecedores = pd.DataFrame({
        "cnpj": ["11.111.111/0001-11", "22.222.222/0001-22", "11.111.111/0001-11"],
        "nome_fornecedor": [" fornecedor a ", "Fornecedor B", " fornecedor a "],
        "categoria": ["material eletrico", "servicos", "material eletrico"],
    })

    pedidos = pd.DataFrame({
        "cnpj": ["11.111.111/0001-11", "22.222.222/0001-22"],
        "valor_pedido": [15000.00, 8500.00],
    })

    df = remover_duplicatas(fornecedores)
    df = padronizar_texto(df)
    df_final = cruzar_bases(df, pedidos)

    print(df_final)
    exportar_resultado(df_final, "fornecedores_tratados.xlsx")


if __name__ == "__main__":
    main()
