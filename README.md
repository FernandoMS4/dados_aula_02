# Bootcamp de Python
 ## Instalação das principais bibliotecas
   -  Instalação do Pyenv
   -  Pip e venv
   -  PipX
   -  Poetry

# Instalando o Pyenv

A instalação do pyenv é feita direto no terminal utilizando pip install Pyenv vide Pyenv-Win para windows

https://github.com/pyenv-win/pyenv-win

# Pip e Venv

O pip e venv é originado do próprio python, não necessitando de instalação e utilizando-os diretamente no terminal

O venv é uma virtual enviroment para utilizar uso:

comando: python -m venv .venv

para ativar: source .venv/Scripts/activate
para desativar: deactivate

### Bibliotecas por local:

Ao instalar as bibliotecas não pode ser em um local "global" de forma que eu possa centralizar as minhas versões utilizando o pyenv local 3.x.x

Para entender como está o ambiente utilizo o "pip list"
Após isso, se não tiver oque limpar ok caso o contrario posso utilizar os comandos

pip freeze //Para eu identificar a lista de todas as bibliotecas instaladas

Após a listagem eu utilizo o comando a seguir para que o pip identifique estas bibliotecas e remova todas 

comando: pip freeze | grep -v "^-e" | xargs pip uninstall -y 

# Poetry e Ipython
O poetry é uma ferramenta de gerenciamento de dependências e torna mais facil.

para Instalação basta ter instalado o pipx e utilizar o comando pipx install poetry

O primeiro passo é "dizer" ao poetry que ele vai gerenciar meu ambiente virtual utilizando o comando:
Obs: Feito isso não é necessário repetir 

poetry config virtualenvs.in-project true

pata utilização da ferramenta basta utilizar:

comando: poetry new projeto_pandas
obs: utilizar o pyenv local para definir a versão do exec do python
comando: poetry env use 3.12.1 

Para instalar uma biblioteca:

comando: poetry add pandas

Para remover uma biblioteca:

comando: poetry remove pandas
