
# Machine Learning Engineer Nanodegree
# Capstone Project
## Project: Análise de Rotas de Veículos

### Visão Geral do Projeto
Este trabalho trata-se de uma análise de rotas de veículos que transitam na cidade de Fortaleza – CE. Os dados são fornecidos pela polícia, que, através de uma rede de pontos de monitoramento na cidade, registra as passagens dos veículos automotores pelos pontos monitorados. O sistema é utilizado para recuperar veículos que possuem alguma restrição (roubo, furto, clone) registrada no banco de dados da polícia. A proposta que será aqui apresentada é encontrar veículos, que mesmo sem alguma restrição registrada, tenha uma probabilidade mais alta de estar em cometimento de algum crime. Através dessa identificação, a polícia poderá otimizar seu trabalho concentrando seus esforços em abordar veículos deste grupo de risco, o que poderá tornar a cidade mais segura.
### Problema
Dadas as passagens de veículos por pontos de monitoramento na cidade, a serão identificados padrões de rotas dos veículos, considerando a quantidade de vezes em que cada veículo passou em cada local. Para isso, serão consideradas como características de cada veículo o número de passagens em cada local, os veículos então serão agrupados por meio de técnicas de Aprendizado de Máquina Não Supervisionado de clusterização. Após os agrupamentos serem definidos, um segundo conjunto de dados será utilizado. Este conjunto contém veículos com restrições de envolvimento em crimes, como roubo, furto e veículos clonados. Será aplicado ao novo conjunto de dados o clusterizador treinado com o conjunto geral, o que fará com que os veículos com restrição sejam encaixados nos agrupamentos já definidos. O objetivo é verificar se em alguns dos padrões encontrados há um predomínio de veículos com restrição, evidenciando veículos que, mesmo sem restrição, se comportam de forma parecida com os veículos rotulados com restrição.



### Install
 
Este projeto requere o **Python 2.7** Jupyter notebook instalado e as seguintes bibliotecas:
- numpy
- pandas
- renders (disponibilizada neste repositório)
- matplotlib
- sklearn


### Code

O código do projeto está no arquivo Analise_de_rotas_de_veiculos.ipynb

### Run

Para executar o projeto é necessário que se encontre no mesmo diretório os arquivos de base de dados:
- veiculos_14e15set_trans.csv
- veiculosrestricao12e13out_trans.csv
- veiculosrestricao21e22set_trans.csv


```python

```
