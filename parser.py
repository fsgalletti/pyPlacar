# coding: utf-8
from lxml import html
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return buscarResultados('brasileirao-serie-a', 'Sport'.decode('utf8'));

def buscarResultados(campeonato, clubeSelecionado):
    teste = "Buscando conteúdo";
    print("Buscando conteúdo".decode('utf8'));
    page = requests.get('http://globoesporte.globo.com/futebol/' + campeonato + '/');
    page.encoding = 'utf-8'
    tree = html.fromstring(page.text);
    jogos = tree.xpath(".//*[@id='container-para-tabela-simulador-ou-navegacao-js']/article/aside/ul/li");
    print('<ul class="lista-de-jogos-conteudo">');
    for idx, item in enumerate(jogos):
        if clubeSelecionado is not None:
            mandante = jogos[idx].find("div/a/div[2]/span[1]/span[2]");
            visitante = jogos[idx].find("div/a/div[2]/span[3]/span[2]");
            if verificarClubeSelecionado(mandante, visitante, clubeSelecionado):
                print(html.tostring(jogos[idx], pretty_print=True));

            if (mandante is not None):
                print(mandante.text + " x " + visitante.text);
        else:
            print(html.tostring(item, pretty_print=True));

    print('</ul>');

def verificarClubeSelecionado(mandante, visitante, escolhido):
    if mandante is None: return False;

    if (mandante.text == escolhido or visitante.text == escolhido):
        return True;
    else:
        return False;