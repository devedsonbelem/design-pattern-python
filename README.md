![Python Version](https://img.shields.io/badge/python-3.x-blue) 
![Coverage Status](https://coveralls.io/repos/github/USERNAME/REPOSITORY/badge.svg?branch=main)
![License](https://img.shields.io/badge/license-MIT-green)

# Sistema de Gerenciamento de Usuários

Este projeto é um sistema de gerenciamento de usuários desenvolvido em Python, que utiliza padrões de projeto e princípios SOLID para garantir flexibilidade, manutenção e segurança na criação e gestão de diferentes tipos de usuários.

## Funcionalidades

- Criação e gestão de diferentes tipos de usuários (Admin, Regular, Guest)
- Utilização do padrão Builder para facilitar a criação de usuários
- Implementação de diferentes estratégias de criptografia de senhas
- Facade para simplificar a criação de usuários

## Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto.

### Pré-requisitos

- Python 3.x instalado

### Configuração do Ambiente Virtual

1. Crie um ambiente virtual (venv):

    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:

    - No Windows:
        ```bash
        venv\Scripts\activate
        ```

    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

### Instalação de Dependências

Instale as dependências necessárias:

```bash
pip install bcrypt
```

## Configuração das Variáveis de Ambiente

Defina as seguintes variáveis de ambiente:

* No Windows:
```=
set PASSWORDADMIN="my secret admin"
set PASSWORDREGULAR="my secret regular"
set PASSWORDGUEST="my secret guest"
set MINHA_CHAVE_SECRETA="minha chave secreta"
set MINHA_OUTRA_SECRETA="minha outra secreta"
```

* No macOS/Linux:
```=
export PASSWORDADMIN="my secret admin"
export PASSWORDREGULAR="my secret regular"
export PASSWORDGUEST="my secret guest"
export MINHA_CHAVE_SECRETA="minha chave secreta"
export MINHA_OUTRA_SECRETA="minha outra secreta"
```

## Executando o Projeto

Após configurar o ambiente virtual e instalar as dependências, você pode executar o projeto conforme necessário.
No terminal, digitar o comando:
```
python main.py
```

## Estrutura do Projeto

* **users.py:** Define a classe abstrata Users e suas subclasses AdminUser, RegularUser e GuestUser.
* **users_builder.py:** Implementa o padrão Builder para a criação de usuários.
* **password_strategy.py:** Define diferentes estratégias de criptografia de senhas.
* **user_facade.py:** Facade para simplificar a criação de usuários.

### Princípios SOLID Aplicados

* **Single Responsibility Principle (SRP):** Cada classe tem uma única responsabilidade. Por exemplo, a classe Users gerencia dados do usuário, enquanto a classe PasswordStrategy lida com a criptografia.
* **Open/Closed Principle (OCP):** As classes estão abertas para extensão, mas fechadas para modificação. Por exemplo, novas estratégias de criptografia podem ser adicionadas sem alterar as classes existentes.
* **Liskov Substitution Principle (LSP):** As subclasses (AdminUser, RegularUser, GuestUser) podem ser usadas como substitutas da classe base Users sem alterar o comportamento esperado do programa.
* **Interface Segregation Principle (ISP):** As interfaces são específicas para cada propósito, como a PasswordStrategy, que define métodos necessários para qualquer estratégia de criptografia.
* **Dependency Inversion Principle (DIP):** O código depende de abstrações (interfaces) em vez de implementações concretas. A classe GeneratePassword usa a interface PasswordStrategy para aplicar diferentes estratégias de criptografia.
