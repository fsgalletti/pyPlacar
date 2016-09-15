# pyPlacar
Busca os resultados da rodada de qualquer campeonato de futebol presente em um dos mais acessados sites de esportes do país.
Pode ser usado principalmente para estudos com a linguagem Python, framework Flask, biblioteca LXML e outros.

Instale em seu ambiente o Python 2.7, o Flask e as seguintes bibliotecas com seus respectivos comandos:

sudo apt-get instapp python-lxml
sudo apt-get instapp requests

Para rodar, você pode executar o comando <b>python app.py</b> e ele irá criar um webserver na porta 80, com o app disponível.
Você pode acessar o pyPlacar usando o endereço <b>http://seuip/futebol</b> .
Caso necessite ou queira mudar a porta, acesse o arquivo app.py e altere o parâmetro port= na linha 56.

Para buscar outra tabela de campeonato de futebol no mesmo site, você pode alterar o parâmetro da função <b>buscarResultados</b> na linha 15.
Também pode escolher um time, caso queira retornar os jogos somente deste.

Exemplo: Retornar jogos do Vasco na tabela da série B:
<b>buscarResultados('brasileirao-serie-b', 'Vasco')</b>

Para consultar o link dos torneios de futebol disponíveis, acesse a área de futebol do respectivo site e veja no link o nome do campeonato.
Algumas opções:<br>
<b>brasileirao-serie-a<br>
brasileirao-serie-b<br>
brasileirao-serie-c<br>
copa-do-brasil<br>
copa-sul-americana</b>

