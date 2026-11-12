#include <iostream>
#include <format>
using namespace std;

int main() {
    int numero1;
    int numero2;

    cout << "Digite o primeiro número: ";
    cin >> numero1;

    cout << "Digite o segundo número: ";
    cin >> numero2;

    if (numero1 > numero2) {
        cout << "O primeiro número é maior." << endl;
    } else if (numero2 > numero1) {
        cout << "O segundo número é maior." << endl;
    } else {
        cout << "Os dois números são iguais.";
    }

    if (numero1 > 0) {
        cout << "O primeiro número é positivo." << endl;
    } else if (numero1 == 0) {
        cout << "O primeiro número é 0." << endl;
    } else {
        cout << "O primeiro número é negativo." << endl;
    }

    if (numero2 > 0) {
        cout << "O segundo número é positivo." << endl;
    } else if (numero2 == 0) {
        cout << "O segundo número é zero." << endl;
    } else {
        cout << "O segundo número é negativo." << endl;
    }

    if (numero1 % 2 == 0 && numero2 % 2 == 0) {
        cout << "Os dois números são pares." << endl;
    } else if (numero1 % 2 != 0 && numero2 % 2 != 0) {
        cout << "Os dois números são ímpares." << endl;
    } else {
        cout << "Um número é par e outro é ímpar." << endl;
    }

    return 0;
}