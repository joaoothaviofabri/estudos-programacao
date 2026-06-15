profile_card = {treinador: "João", idade: 16, party1: "Gengar", party2: "Scrafty"}
profile_card[:party3] = "Toxtricity"

puts profile_card

profile_card.delete(:party3)
puts profile_card

puts profile_card.has_value?("Gengar")
puts profile_card.has_key?(:treinador)

puts profile_card.keys
puts "-" * 10
puts profile_card.values

puts profile_card.clear