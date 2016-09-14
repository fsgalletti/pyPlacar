# coding: utf-8

from flask import Flask, render_template, Markup
from lxml import html
import requests

app = Flask(__name__)

@app.route('/futebol')
def futebol():
	html = Markup(start());
   	return render_template('futebol.html', resultados=html);

def start():
    return buscarResultados('brasileirao-serie-a', None);

def buscarResultados(campeonato, clubeSelecionado):

    page = requests.get('http://globoesporte.globo.com/futebol/' + campeonato + '/');
    page.encoding = 'utf-8'
    tree = html.fromstring(page.text);
    jogos = tree.xpath(".//*[@id='container-para-tabela-simulador-ou-navegacao-js']/article/aside/ul/li");
    retorno = '<ul class="lista-de-jogos-conteudo">';
    for idx, item in enumerate(jogos):
        if clubeSelecionado is not None:
            mandante = jogos[idx].find("div/a/div[2]/span[1]/span[2]");
            visitante = jogos[idx].find("div/a/div[2]/span[3]/span[2]");
            if verificarClubeSelecionado(mandante, visitante, clubeSelecionado):
                retorno += html.tostring(jogos[idx], pretty_print=True);

            if (mandante is not None):
                retorno += mandante.text + " x " + visitante.text;
        else:
            retorno += html.tostring(item, pretty_print=True);

    retorno += '</ul>';
    return retorno;

def verificarClubeSelecionado(mandante, visitante, escolhido):
    if mandante is None: return False;

    if (mandante.text == escolhido or visitante.text == escolhido):
        return True;
    else:
        return False;

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)