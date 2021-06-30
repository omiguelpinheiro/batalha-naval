# Batalha-Naval
Projeto de INF1301

Criação de um jogo de Batalha Naval para a disciplina de Programação Modular.

Para iniciar um jogo:
```bash
git clone https://github.com/omiguelpinheiro/batalha_naval.git
cd batalha_naval
```
Para o jogo funcionar é necessário fazer o download de algumas bibliotecas extras. Rodar o commando abaixo também fará o download das bibliotecas necessárias para fazer os testes que serão mencionados mais abaixo. Certifique-se que está dentro da pasta do jogo que tem o arquivo requirements.txt dentro e execute:
```bash
pip install -r requirements.txt
```
Para rodar o jogo use o commando conveniente:
```bash
python run.py
```
Para fazer os testes automáticos use o commando:
```bash
pytest --cov=essencial -p no:cacheprovider
```
Por:

Leonardo Trote Martins\
Luiza Bretas Junqueira Correa Luiz\
Marina Magagnin Ribeiro\
Miguel Pinheiro da Costa
