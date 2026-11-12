#include <iostream>
#include <format>
using namespace std;

int main() {
    int numero1;
    int numero2;

    cout << "Digite o primeiro número: ";
    cin >> numero1;

    cout << "Digite o segundo número ";
    cin >> numero2;

    int soma = numero1 + numero2;
    int subt = numero1 - numero2;
    int mult = numero1 * numero2;
    double div = static_cast<double>(numero1) / numero2;

    auto primeiroNumeroMaior = numero1 > numero2;
    auto numerosIguais = numero1 == numero2;
    auto numerosPositivos = numero1 > 0 && numero2 > 0;

    cout << format(
        "Soma: {}\n"
        "Subtração: {}\n"
        "Multiplicação: {}\n"
        "Divisão: {}\n"
        "O primeiro número é maior que o segundo? {}\n"
        "Os dois números são iguais? {}\n"
        "Os dois números são positivos? {}",
        soma, subt, mult, div,
        primeiroNumeroMaior, numerosIguais, numerosPositivos
    );
    
    return 0;
}