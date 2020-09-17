# Desafio técnico da Atados

https://www.pyjobs.com.br/job/1395/challenge_submit/

#### Rodando a aplicação

- Dentro de seu ambiente virtual rode: **pip install -r requirements.txt**;
- Após a instalação das dependencias, na raiz do projeto, rode: **./manage.py runserver** para executar a aplicação.

#### Rodando aplicação dentro do container

- Para rodar a aplicação dentro do container configurado para a mesma, basta executar o seguinte comando: **docker-compose up**.

#### URLS da API

*/api/v1/* -> raiz da API;
*/api/v1/voluntarios/* -> endpoint dos volutarios;
*/api/v1/acoes/* -> endpoint das ações;

#### Rodando os testes

- Na raiz da aplicação rode o seguinte comando: **./manage.py test**

#### extras

- Na raiz do projeto há um script em shell que pode ser executado para facilitar as migrações dentro do container, mas o recomendado é que seja feito manualmente esse procedimento.