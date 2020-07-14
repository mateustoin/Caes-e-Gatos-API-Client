<img id="introducao" src="img/1.png" style="height:300px, ">

<!--- # Requisição de CEP, Rua, Cidade e Estados --->

<p>
    API Client criado para visualizar fotos e vídeos de <b>doguinhos e gatinhos</b>. O objetivo é praticar diversos conceitos da linguagem e padrões de projeto, além de descontrair com imagens e vídeos engraçados durante a quarentena. O padrão de projeto escolhido para o desenvolvimento é o <b>MVC (Model-View-Controller)</b>, implementado em <b>Python</b>.
</p>

<p>
    As API's utilizadas neste projeto foram a <a href="https://random.dog/">random.dog/</a> e <a href="https://aws.random.cat/">aws.random.cat/</a>, que disponibilizam acesso gratuito e sem registro. Nessas API's é possível realizar requisições que retornam links de vídeos e fotos de gatos e cachorros aleatórios. Na maioria das vezes são imagens engraçadas e divertidas de assistir, por isso é perfeito para o objetivo desse projeto. Os links são processados e as imagens e vídeos baixados para que os resultados sejam visualizados na tela. Diversas funcionalidades como utilização do teclado são utilizados para passar as imagens e oferecer uma experiência mais fácil. <i>A velocidade em que as imagens aparecem dependem diretamente da velocidade da internet do usuário</i>.
</p>

---

# Sumário
1. [Introdução](#introducao) 
1. [Instalando pacotes](#instalacao)
2. [Padrão Model-View-Controller](#mvc)
    - [AnimalModel](#animalmodel)
    - [AnimalView](#animalview)
    - [AnimalController](#animalcontroller)
3. [To-Do List da Aplicação](#todo-list)
4. [Uso do API Client](#usage)
    - [](#)
    - [](#)

---

# Instalando pacotes <a id="instalacao"></a>

Para instalar os pacotes utilizados no projeto, basta ter o <i>pip</i> instalado e utilizar o comando a seguir:

`pip install -r requirements.txt`

- *requests* é utilizado para realizar todas as requisições à API cep.la
<!--
- *rich* é utilizado para formatar os resultados, implementados em CepView para a visualização do usuário
-->
---

<img id="mvc" src="img/2.png" style="height:300px, ">

## AnimalModel <a id="animalmodel"></a>
<!--
<p>
    A implementação do <i>CepModel</i> consiste em realizar as requisições para a API, além de tratar os dados inseridos pelo usuário e retornar os dados de resposta da API, de uma maneira que possa ser utilizada por outras estruturas. Além disso, lança <i>exceções</i> para diversos problemas que podem ocorrer no processo, seja pelo usuário ou pela API.
</p>
-->
## AnimalView <a id="animalview"></a>
<!--
<p>
    A implementação do <i>CepView</i> consiste apenas em organizar a visualização dos dados retornados pelo <i>CepModel</i>. A visualização deve ser feita de forma clara para o usuário, a fim de oferecer uma experiência boa para quem utiliza. No momento é feita através de prints no terminal, porém a forma como o projeto está organizado permite que, caso o projeto escale e seja feita uma interface gráfica, por exemplo, os únicos métodos que deveriam ser modificadas seriam as de <i>CepView</i>. 
</p>
-->
## AnimalController <a id="animalcontroller"></a>
<!--
<p>
    A implementação do <i>CepControl</i> é feita para que o usuário tenha acesso aos métodos para o uso da API como um cliente. Estes métodos coletam os dados necessários do usuário, invoca o <i>model</i> para tratá-los e organizar os dados, depois utiliza esses resultados para invocar o <i>view</i> e exibir os dados para o usuário. Essa orquestração é feita apenas pelo <i>controller</i>, ao qual o usuário tem contato. Nele também são feitos os tratamentos de exceção, simplificando ainda mais o retorno para o usuário verificar e realizar ações a respeito.
</p>
-->
---

<img id="todo-list" src="img/3.png" style="height:300px, ">

<p>
    Aqui serão apresentadas as próximas ideias a serem implementadas para que o projeto tenha cada vez mais funcionalidades.
</p>

- [x] Visualiza fotos de doguinhos
- [x] Visualiza vídeos de doguinhos
- [ ] Visualiza fotos e vídeos de doguinhos
- Ajuste de dimensão
    - [ ] Fotos
    - [ ] Videos
- [ ] Visualizar fotos de gatinhos
- [ ] Visualizar vídeos de gatinhos
- [ ] Salvar fotos e vídeos que gostou

---

<img id="usage" src="img/4.png" style="height:300px, ">
<!--

## 1. Procura informações de endereço através de um CEP <a id="cep"></a>

> main.py

```python
from CepControl import CepControl

if __name__ == '__main__':
    control = CepControl()
    control.search_by_cep(input('Insira um CEP válido: '))
```
> TERMINAL

<img src="img/out_cep.png" style="height:300px, ">

## 2. Procura nomes dos bairros de cidades <a id="bairro"></a>

> main.py

```python
from CepControl import CepControl

if __name__ == '__main__':
    control = CepControl()
    control.search_by_neighborhood(uf='pe', city='recife')
```

> TERMINAL (apenas parte da saída na imagem)

<img src="img/bairro.png" style="height:300px, ">
-->