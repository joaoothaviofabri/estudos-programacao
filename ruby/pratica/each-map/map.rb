nomes = ["João", "Maria", "José", "Mateus"]

nomes_completos = nomes.map do |nome_completo|
    nome_completo + " sobrenome"
end

# nomes.map! do |nome_completo|
#     nome_completo + " sobrenome"
# end

puts nomes
puts "-" * 10
puts nomes_completos