# 🧠 Desafio de Programação com Python e SQLite

Este projeto resolve um desafio de automação de processo seletivo com uso de **Python** e **SQLite**, simulando o cadastro de candidatos e avaliação com base na **sequência de Fibonacci**.

---

## 📋 Descrição do Desafio

O problema consiste em:

1. Criar um banco de dados SQLite com duas tabelas:
   - `SELECAO_CANDIDATO`: armazena informações do candidato.
   - `SELECAO_TESTE`: armazena números da sequência de Fibonacci associados ao candidato.
   
2. Inserir um candidato fictício no banco.

3. Gerar os **30 primeiros números da sequência de Fibonacci**, verificando para cada número se ele é **par** ou **ímpar**, e salvando essas informações.

4. Realizar consultas SQL para:
   - Listar todos os números da sequência.
   - Mostrar os 5 maiores números.
   - Contar quantos são pares e quantos ímpares.
   - Excluir todos os números maiores que 5000.
   - Exibir novamente a sequência atualizada.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- SQLite (via `sqlite3`, nativo do Python)
- SQL (comandos básicos: `CREATE`, `INSERT`, `SELECT`, `DELETE`)

---

## 📁 Estrutura do Projeto

📦 sql-desafio
┣ 📄 desafio.py → Script principal que executa toda a lógica
┣ 📄 meu_banco.db → Banco de dados gerado automaticamente
┗ 📄 README.md → Documentação do projeto
