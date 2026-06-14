print "Digite um mês: "
mes = gets.chomp.strip.downcase

case mes
when "junho"
    puts "Esse mês tem 30 dias."
when "julho"
    puts "Esse mês tem 31 dias."
when "agosto"
    puts "Esse mês tem 31 dias."
else
    puts "Não sei quantos dias tem esse mês."
end