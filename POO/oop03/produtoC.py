import produtoOOP as p

#Entrada de dados
print("Entre com os dados do produtos:")
nome = input("Nome: ")
preco = float(input("Preço: R$"))
saldo = int(input("Quantidade: "))

#Instanciar o meu objeto
#ps = p.Produto(nome, preco, saldo)
ps = p.Produto(nome, preco)

#Saída de dados
print(ps.dadosDoProduto())