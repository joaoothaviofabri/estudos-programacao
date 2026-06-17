nomes = ["João", "Ana", "Laís"]

dict = {nome: "João", idade: 16, altura:1.82}

nomes.each do |nome|
    puts nome
end

dict.each do |chave, valor|
    puts "#{chave.capitalize}: #{valor}"
end