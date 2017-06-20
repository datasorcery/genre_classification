# Classificação de Generos

## Requisitos

* Python 3.6.1
* pip 9.0.1 
* virtualenv 15.1.0

## Instalação

Crie um novo virtualenv, ative e instale as dependencias:

`virtualenv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

## Uso

Esta POC contém duas partes:

* Um notebook **Jupyter** que prepara os dados, treina o modelo e testa a performance final;
* Uma aplicação flask onde o resultado do modelo pode ser testado com novos textos;

### Treinando o modelo

Após ativar o `virtualenv`, entre no diretório **model** inicilize o Jupyter com o comando:

`jupyter notebook`

Garanta que seus dados de treinamento estão no diretorio **train**, dentro do diretório **modelo*.
Os dados de treinamento devem estar separados em arquivos, sendo que cada um deles deverá ter dados
de apenas uma das classes. O modelo descobre as classes a partir do nome dos arquivos neste diretório.
Para treinar novas classes basta apenas incluir novos arquivos neste diretório. Inicialmente estão 
disponíves as seguintes **classes/arquivos**:

* bossa_nova.csv
* funk.csv
* gospel.csv
* sertanejo.csv

Na primeira vez em que executar o *notebook*, descomente a linha `#nltk.download()` (dentro da seção 
**Configuração**) para garantir que todo o corpus necessário esteja disponível localmente. As configurações
relevantes do modelo estão nesta célula e são:

* MODEL
* TRAINSET
* WORD_FEATURES
* TEST_RATIO
* RANDOM_SEED
* N_TREES
* CORES

