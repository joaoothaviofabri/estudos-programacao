guilda = []

loop do
    puts "==== RPG ===="
    puts "1 - Recrutar Aventureiro"
    puts "2 - Listar Aventureiros"
    puts "3 - Enviar para Missão"
    puts "4 - Painel do Mestre"
    puts "5 - Sair"

    print "Escolha: "
    escolha_usuario = gets.chomp.to_i

    case escolha_usuario
    when 1
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
    
    when 2
        if guilda.empty?
            puts "Sua guilda ainda não possui membros!"
        else
            guilda.each do |aventureiros|
                puts "Nome: #{aventureiros[:nome]}"
                puts "Status: #{aventureiros[:status] ? "Em missão" : "Livre"}"
            end
        end
    when 3
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
    when 4
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
    when 5
        puts "Encerrando..."
        break
    end
end