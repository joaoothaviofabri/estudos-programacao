#include <iostream>
#include <format>
using namespace std;

int main() {
    string nome;
    int idade;
    string cidade;

    cout << "Qual o seu nome? ";
    getline(cin, nome);

    cout << "Quantos anos você tem? ";
    cin >> idade;

    cin.ignore();

    cout << "Onde você mora? ";
    getline(cin, cidade);
    
    cout << format(
        "Olá, {}! Você tem {} anos e mora na cidade de {}.", 
        nome, idade, cidade
    );

    return 0;
}