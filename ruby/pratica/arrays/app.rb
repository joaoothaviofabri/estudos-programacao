party = []

print "Digite seu nome: "
treinador = gets.chomp
party.push(treinador)

print "Digite o primeiro pokémon da party: "
pokemon_1 = gets.chomp
party << pokemon_1

print "Digite o segundo pokémon da party: "
pokemon_2 = gets.chomp
party << pokemon_2

print "Digite o terceiro pokémon da party: "
pokemon_3 = gets.chomp
party << pokemon_3

party_organizada = party.sort

puts party_organizada[1..2]