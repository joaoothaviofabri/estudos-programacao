print "Digite um número: "
x = gets.chomp.to_i

if x.between?(10, 20)
    puts "O número digitado (#{x}) está entre 10 e 20."
elsif x > 20
    puts "O número digitado (#{x}) é maior que 20."
else
    puts "O número digitado (#{x}) é menor que 10."
end

# puts false && true
# puts false || true
# puts !false && true