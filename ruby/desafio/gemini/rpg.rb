def exibir_menu
    puts "==== RPG ===="
    puts "1 - Recrutar Aventureiro"
    puts "2 - Listar Aventureiros"
    puts "3 - Enviar para Missão"
    puts "4 - Painel do Mestre"
    puts "5 - Sair"
end

def recrutar_membro (guilda)
    print "Digite o nome do aventureiro: "
    nome_aventureiro = gets.chomp.capitalize

    print "Digite a classe do aventureiro: "
    classe_aventureiro = gets.chomp.capitalize

    print "Digite o nível do aventureiro: "
    nivel_aventureiro = gets.chomp.to_i
    
    print "Está em uma missão no momento? [S/N]: "
    resposta_missao = gets.chomp.upcase
    status_aventureiro = (resposta_missao == "S")

    dados_aventureiro = {nome: nome_aventureiro, classe: classe_aventureiro, nivel: nivel_aventureiro, status: status_aventureiro}
    guilda << dados_aventureiro
end

def listar_membros (guilda)
    if guilda.empty?
        puts "Sua guilda ainda não possui membros!"
    else
        guilda.each do |aventureiros|
            puts "Nome: #{aventureiros[:nome]}"
            puts "Status: #{aventureiros[:status] ? "Em missão" : "Livre"}"
        end
    end
end

def enviar_missao (guilda)
    print "Quem você quer mandar para uma missão? "
    enviar_missao = gets.chomp.capitalize

    aventureiro_enviado = guilda.find { |enviado| enviado[:nome] == enviar_missao}
    if !aventureiro_enviado
        puts "Aventureiro não encontrado na guilda!"
    else
        if aventureiro_enviado[:status]
            puts "Esse aventureiro já está em uma missão!"
        else
            aventureiro_enviado[:status] = true
            puts "Aventureiro enviado para uma missão!"
        end
    end
end

def painel_mestre (guilda)
    if guilda.empty?
        puts "Sua guilda ainda não possui membros!"
    else
        puts "Total de membros: #{guilda.count}"
        
        soma_nivel = guilda.sum { |a| a[:nivel]}
        media_nivel = soma_nivel / guilda.count
        puts "A média de nível da guilda é: #{media_nivel}"

        lider = guilda.max_by { |a| a[:nivel]}
        puts "O membro com nível mais alto é: #{lider[:nome]} - Nv.#{lider[:nivel]}"

        em_missao = guilda.count { |a| a[:status] == true}
        puts "A quantidade total de membros em missão é: #{em_missao}"
    end
end

guilda = []

loop do
    exibir_menu
    print "Escolha: "
    escolha_usuario = gets.chomp.to_i

    case escolha_usuario
    when 1
        recrutar_membro(guilda)
    when 2
        listar_membros(guilda)
    when 3
        enviar_missao(guilda)
    when 4
        painel_mestre(guilda)
    when 5
        puts "Encerrando..."
        break
    else
        puts "Opção inválida!"
    end

    puts "\n"
end