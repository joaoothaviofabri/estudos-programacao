nome = "João"
numero = 5

if nome.eql?("João")
    puts "Estudando Ruby"
else
    puts "Visitnate"
end

# condigcao ? verdadeiro : falso

puts nome.eql?("João") ? "Estudando Ruby" : "Visitante"

resultado = nome.eql?("João") ? "Estudando Ruby - resultado" : "Visitante - resultado"
puts resultado

soma = numero.eql?(5) ? numero + 10 : numero - 1
puts soma