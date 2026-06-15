nomes = ["João", "Ana", "Lais"]

dict = {nome: "João", idade: 16, altura: 1.82}

# for nome in nomes do
#     puts nome
# end

for k, v in dict do
    puts "#{k.capitalize}: #{v}"
end