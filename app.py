# coding: utf-8

from flask import Flask, render_template, Markup
from lxml import html
import requests

app = Flask(__name__)

@app.route('/futebol')
def futebol():
	#A classe Markup renderiza o código HTML como parte construtiva da página, ao invés de tratar como conteúdo.
	html = Markup(start());
   	return render_template('futebol.html', resultados=html);

def start():
    return buscarResultados('brasileirao-serie-a', None);

#buscarResultados
#campeonato = Nome do campeonato de acordo com a URL disponível no site. Verifique na documentação os campeonatos disponíveis
#clubeSelecionado = Insira o nome de um clube de futebol para filtrar para os jogos somente deste.
def buscarResultados(campeonato, clubeSelecionado):

	#Busca o conteúdo da página inteira
    page = requests.get('http://globoesporte.globo.com/futebol/' + campeonato + '/');
    page.encoding = 'utf-8'
    tree = html.fromstring(page.text);
	#Usa o caminho Xpath para buscar os objetos com o conteúdo exclusivo da tabela da rodada do campeonato. Você pode usar o FirePath no Firefox para encontrar o caminho que precisa dentro do código HTML de qualquer página.
    jogos = tree.xpath(".//*[@id='container-para-tabela-simulador-ou-navegacao-js']/article/aside/ul/li");
    retorno = '<ul class="lista-de-jogos-conteudo">';
    for idx, item in enumerate(jogos):
        if clubeSelecionado is not None:
            mandante = jogos[idx].find("div/a/div[2]/span[1]/span[2]");
            visitante = jogos[idx].find("div/a/div[2]/span[3]/span[2]");
            if verificarClubeSelecionado(mandante, visitante, clubeSelecionado):
                retorno += html.tostring(jogos[idx], pretty_print=True);
        else:
            retorno += html.tostring(item, pretty_print=True);

    retorno += '</ul>';
    return retorno;

#verificarClubeSelecionado
#mandante = Clube mandante da partida
#visitante = Clube visitante da partida
#escolhido = Clube escolhido pelo programador para ser o único a retornar dados
def verificarClubeSelecionado(mandante, visitante, escolhido):
    if mandante is None: return False;

    if (mandante.text == escolhido or visitante.text == escolhido):
        return True;
    else:
        return False;

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)