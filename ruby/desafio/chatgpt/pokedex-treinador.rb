pokemon_armazenados = []

loop do
    puts "==== POKEDEX ===="
    puts "1 - Adicionar Pokémon"
    puts "2 - Ver esquipe"
    puts "3 - Procurar Pokḿeon"
    puts "4 - Mostrar estatísticas"
    puts "5 - Remover Pokémon"
    puts "6 - Sair"
    puts ""

    print "Escolha: "
    escolha_usuario = gets.chomp.to_i

    case escolha_usuario
    when 1
        print "Nome: "
        nome = gets.chomp.capitalize

        print "Tipo(s): "
        tipo = gets.chomp.capitalize

        print "Nível: "
        nivel = gets.chomp.to_i

        adicao_pokemon = {nome_pokemon: nome, tipo_pokemon: tipo, nivel_pokemon: nivel}
        pokemon_armazenados << adicao_pokemon
        puts "Pokémon Adicionado!"

    when 2
        classificacao_nivel = ""
        if pokemon_armazenados.empty?
            puts "A sua equipe está vazia!"
        else
            for valor in pokemon_armazenados do
                case valor[:nivel_pokemon]
                when 1..20
                    classificacao_nivel = "Iniciante"
                when 21..50
                    classificacao_nivel = "Experiente"
                else
                    classificacao_nivel = "Elite"
                end
                puts "#{valor[:nome_pokemon]} - #{valor[:tipo_pokemon]} - Lv.#{valor[:nivel_pokemon]}  -> #{classificacao_nivel}"
            end
        end

    when 3
        puts "Digite o nome: "
        print "> "
        pesquisa_pokemon = gets.chomp.capitalize
        pesquisa_pokemon_encontrado = false

        for valor in pokemon_armazenados do
            if valor[:nome_pokemon] == pesquisa_pokemon
                pesquisa_pokemon_encontrado = true
                puts "Pokémon encontrado!"
                puts "Tipo: #{valor[:tipo_pokemon]}"
                puts "Nível: #{valor[:nivel_pokemon]}"
                break
            end
        end
        if !pesquisa_pokemon_encontrado
            puts "Pokémon não encontrado!"
        end

    when 4
        if pokemon_armazenados.empty?
            puts "Você não possui pokémon ainda!"
        else
            quantidade_pokemon = pokemon_armazenados.count
            puts "Total de Pokémon: #{quantidade_pokemon}"

            soma_nivel = 0
            for valor in pokemon_armazenados do
                soma_nivel = valor[:nivel_pokemon] + soma_nivel
            end
            puts "Soma dos níveis: #{soma_nivel}"

            media_nivel = soma_nivel / quantidade_pokemon
            puts "Média dos níveis: #{media_nivel}"

            pokemon_mais_forte = pokemon_armazenados[0]
            for valor in pokemon_armazenados do
                if pokemon_mais_forte[:nivel_pokemon] < valor[:nivel_pokemon]
                    pokemon_mais_forte = valor
                end
            end
            puts "Pokémon mais forte:"
            puts "#{pokemon_mais_forte[:nome_pokemon]} (Lv.#{pokemon_mais_forte[:nivel_pokemon]})"
        end

    when 5
        puts "Remover qual pokémon?"
        print "> "
        remover_pokemon = gets.chomp.capitalize
        remover_pokemon_encontrado = false

        for valor in pokemon_armazenados do
            if valor[:nome_pokemon] == remover_pokemon
                pokemon_armazenados.delete(valor)
                remover_pokemon_encontrado = true
                puts "Pokémon removido!"
                break
            end
        end
        if !remover_pokemon_encontrado
            puts "Esse pokémon não está na sua equipe!"
        end

    when 6
        puts "Desligando Pokedex..."
        break
    end
end