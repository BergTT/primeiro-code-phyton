# Colocando lista para usuário verificar os filmes disponiveis (pode usar Control + C e Control + V para copiar e colar nome do filme que desejar informação)
filmes = ['O Poderoso Chefão', 'Um Sonho de Liberdade', 'Batman - O Cavaleiro das Trevas', 'O Poderoso Chefão II', '12 Homens e Uma Sentença', 'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction - Tempo de Violência', 'O Senhor dos Anéis: A Sociedade do Anel', ' Três Homens em Conflito'] 
print(filmes)
# Criando um dicionário com informações de nome, ano e sinopse
top_filmesIMDB = {
    'O Poderoso Chefão': {'ano': 1972, 'sinopse': 'A história de uma família mafiosa da Sicília que tenta transferir o controle de sua operação ilegal para os Estados Unidos.'},
    'Um Sonho de Liberdade': {'ano': 1994, 'sinopse': 'A história de um homem inocente que é condenado à prisão perpétua por um crime que não cometeu e sua amizade com outro prisioneiro ao longo dos anos.'},
    'Batman - O Cavaleiro das Trevas': {'ano': 2008, 'sinopse': 'Batman enfrenta o terrível Coringa em uma batalha pela alma de Gotham City.'},
    'O Poderoso Chefão II': {'ano': 1974, 'sinopse': 'A continuação da saga da família Corleone, mostrando tanto o passado quanto o presente de Vito Corleone e seu filho, Michael.'},
    '12 Homens e Uma Sentença': {'ano': 1957, 'sinopse': 'Doze jurados devem decidir o destino de um jovem acusado de homicídio, mas um deles tem dúvidas razoáveis sobre a culpa do réu.'},
    'A Lista de Schindler': {'ano': 1993, 'sinopse': 'A história real de Oskar Schindler, um empresário alemão que salva a vida de mais de mil refugiados judeus durante o Holocausto.'},
    'O Senhor dos Anéis: O Retorno do Rei': {'ano': 2003, 'sinopse': 'A conclusão épica da trilogia O Senhor dos Anéis, onde Frodo e Sam continuam sua jornada para destruir o Um Anel enquanto uma grande batalha acontece na Terra Média.'},
    'Pulp Fiction - Tempo de Violência': {'ano': 1994, 'sinopse': 'Uma série de histórias interligadas sobre gangsters, boxeadores, assassinos e outros personagens de Los Angeles.'},
    'O Senhor dos Anéis: A Sociedade do Anel': {'ano': 2001, 'sinopse': 'A primeira parte da trilogia O Senhor dos Anéis, onde um grupo de heróis se reúne para destruir um anel mágico e impedir que caia nas mãos do mal.'},
    'Três Homens em Conflito': {'ano': 1966, 'sinopse': 'Durante a Guerra Civil Americana, três homens procuram um tesouro enterrado, mas cada um deles tem seus próprios planos e lealdades.'}
}

# Solicitando ao usuário que insira o nome do filme
nome_filme = input("Digite o nome do filme que deseja obter informações: ")

# Verificando se o filme contem no dicionário
if nome_filme in top_filmesIMDB:
    # Obtendo informações detalhada do filme
    info_filme = top_filmesIMDB[nome_filme]
    print(f"Informações sobre {nome_filme}:")
    print(f"Ano do Filme é", info_filme["ano"])
    print("Sinopse:\n", info_filme["sinopse"])
else:
    print(f"{nome_filme} não está na lista de mais populares do IMDB.") # Se usuário digitar nome de filme que não esteja no dicionário