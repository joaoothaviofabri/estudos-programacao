#include <iostream>
#include <format>
using namespace std;

int main() {
    string nome;
    int idade;
    double altura;
    bool estudando;

    cout << "Digite seu nome completo: ";
    getline(cin, nome);

    cout << "Digite sua idade: ";
    cin >> idade;

    cin.ignore();

    cout << "Digite sua altura: ";
    cin >> altura;

    cout << "Você ainda está estudando? ";
    cin >> boolalpha >> estudando;

    cout << format(
        "Olá, {}! Você tem {} anos, tem {}m de altura e ainda está estudando: {}.",
        nome, idade, altura, estudando ? "Sim" : "Não"
    );

    return 0;
}