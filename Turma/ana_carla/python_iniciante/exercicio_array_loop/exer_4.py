#buscar produto no estoque
def analise_de_produto(nome_produto, lista_nome, lista_qtd):
    # verificar qual é a quantidade de produto tem na lista de quantidade e retornar o valor 
        for i in range(len(lista_nome)):
             if lista_nome[i] == nome_produto:
                  return lista_qtd[i]
        return None
                

def main():
    
    produto_nomes = ["papel", "apontador", "caneta", "caderno", "tesoura", "borracha"]
    produto_quantidade = [500, 50, 25, 62, 40, 81]

    while True:
        nome_produto = input("Digite o nome do produto que esta buscando:").strip().lower()
        quantidade = analise_de_produto(nome_produto, produto_nomes, produto_quantidade)

        if quantidade is not None:
             print(f"O produto {nome_produto} esta disponivél e tem {quantidade} unidades")
             break
        else:
            continuar_busca = input("Produto inexistente. Gostaria de continuar a sua busca? (responda sim ou nao)").strip().lower()
            if continuar_busca == "sim":
                continue
            elif continuar_busca == "nao" or continuar_busca == "não":
                print("Busca encerrada")
                break
            else:
                 print("Resposta Inválida. Encerrando busca por segurança.")
                 break
  
   
        
if __name__ == "__main__":
    main()