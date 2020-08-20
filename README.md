<img id="introducao" src="img/1.png" style="height:300px, ">

<!--- # Requisição de CEP, Rua, Cidade e Estados --->

<p>
    API Client criado para visualizar fotos e vídeos de <b>doguinhos e gatinhos</b>. O objetivo é praticar diversos conceitos da linguagem e padrões de projeto, além de descontrair com imagens e vídeos engraçados durante a quarentena. O padrão de projeto escolhido para o desenvolvimento é o <b>MVC (Model-View-Controller)</b>, implementado em <b>Python</b>. 
</p>

<p>
    <i><b>edit:</b> Infelizmente a API que seria utilizada para visualizar os gatinhos parou de funcionar durante o desenvolvimento, portanto foi substituída por outra responsável por visualizar raposas! Em respeito aos gatinhos que seriam mostrados e eram muito legais, as referências visuais a eles serão mantidas no repositório.
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
    - [Visualização de fotos](#fotos-animais)
    - [Visualização de vídeos](#videos-animais)
5. [Teste na sua máquina sem precisar do python](#exec)

---

# Instalando pacotes <a id="instalacao"></a>

Para instalar os pacotes utilizados no projeto, basta ter o <i>python 3</i> e <i>pip</i> instalado e utilizar o comando a seguir na pasta do projeto:

`pip install -r requirements.txt`

- *requests* é utilizado para realizar todas as requisições à API's citadas na introdução
- *numpy* é utilizado para fazer as transformações da imagem em array, para que todas as informações dos pixels (RGB) sejam armazenadas de uma forma que o opencv consiga ler
- *open_cv* carrega as imagens e vídeos para visualização na tela. 

---

<img id="mvc" src="img/2.png" style="height:300px, ">

## AnimalModel <a id="animalmodel"></a>

<p>
    A implementação do <i>AnimalModel</i> consiste em realizar as requisições para as API's e tratar dados como tipo de arquivo, se é imagem, vídeo, gif. Cada classe (Cachorro e Gato) possui suas próprias requisições, a fim de resolver as particularidades de cada tipo de dado que é retornado. Além disso, lança <i>exceções</i> para diversos problemas que podem ocorrer no processo, seja pelo usuário ou pela API.
</p>

## AnimalView <a id="animalview"></a>
 
<p>
    A implementação do <i>AnimalView</i> consiste apenas em organizar a visualização dos dados retornados pelo <i>AnimalModel</i>. A visualização deve ser feita de forma clara para o usuário, a fim de oferecer uma experiência boa para quem utiliza. Atualmente toda a visualização é feita utilizando o <i>Opencv</i>, utilizando a janela padrão de visualização. Com a classe de visualização separada o projeto se torna mais modularizado, com responsabilidades independentes, tornando mais fácil futuras manutenções e melhorias. 
</p>

## AnimalController <a id="animalcontroller"></a>

<p>
    A implementação do <i>AnimalControl</i> é feita para que o usuário tenha acesso aos métodos para o uso da API como um cliente. Estes métodos coletam os dados necessários do usuário, invoca o <i>model</i> para tratá-los e organizar os dados, depois utiliza esses resultados para invocar o <i>view</i> e exibir os dados para o usuário. Essa orquestração é feita apenas pelo <i>controller</i>, ao qual o usuário tem contato. Nele também são feitos os tratamentos de exceção, simplificando ainda mais o retorno para o usuário verificar e realizar ações a respeito.
</p>

---

<img id="todo-list" src="img/3.png" style="height:300px, ">

<p>
    Aqui serão apresentadas as próximas ideias a serem implementadas para que o projeto tenha cada vez mais funcionalidades.
</p>

- [x] Visualiza fotos de doguinhos
- [x] Visualiza vídeos de doguinhos
- [x] Visualiza fotos e vídeos de doguinhos
- [x] Ajuste de dimensão
    - [x] Fotos
    - [x] Videos
<!--- [ ] Visualizar fotos de gatinhos
- [ ] Visualizar vídeos de gatinhos-->
- [x] Visualizar fotos de raposinhas
- [x] Salvar fotos e vídeos que gostou

<p>
    <i>edit: Todos os itens da lista foram concluídos durante a live e algumas pequenas melhorias após o final do projeto, com o objetivo de garantir o funcionamento sem erros.</i>
</p>

---

<img id="usage" src="img/4.png" style="height:300px, ">

> Versão do Python que funcionará: Python 3.x

<p>
    A versão final da aplicação oferece 4 opções quando o <code>main.py</code> é <b>executado</b>:

</p>

<ol>
    <li> Visualizar apenas fotos de doguinhos </li>
    <li> Visualizar apenas vídeos de doguinhos </li>
    <li> Visualizar fotos e vídeos de doguinhos </li>
    <li> Visualizar apenas fotos de raposas </li>
</ol>

<p>
    Em todas elas os seguintes <b>comandos</b> são válidos:
</p>

<ul>
    <li> Pressionar letra 's' para salvar foto ou vídeo</li>
    <li> Pressiocar ESC para encerrar aplicação</li>
    <li> Pressionar qualquer outra letra para carregar próxima foto ou vídeo </li>
</ul>

## 1. Visualizando apenas fotos <a id="fotos-animais"></a>

> main.py

```python
python main.py

> Escolha opção de fotos

Pressione letra 'ESC' para fechar a visualização
Pressione a letra 's' para salvar a foto
Pressione qualquer outra tecla para ver mais fotos
```

<p align='center'>
<img src="https://github.com/mateustoin/Caes-e-Gatos/blob/master/img/fotos.gif?raw=true">&nbsp;&nbsp;
</p>    

## 2. Visualizando apenas vídeos <a id="videos-animais"></a>

> main.py

```python
python main.py

> Escolha opção de fotos

Pressione letra 'ESC' para fechar a visualização
Pressione a letra 's' para salvar o vídeo
Pressione qualquer outra tecla para ver mais fotos
```

<p align='center'>
<img src="https://github.com/mateustoin/Caes-e-Gatos/blob/master/img/videos.gif?raw=true">&nbsp;&nbsp;
</p> 

# Teste na sua máquina sem precisar do python <a id="exec"></a>

<p>
    Utilizando a biblioteca <i>pyinstaller</i> foi possível realizar um build para criar um executável do protótipo apresentado, a fim de que possa ser executado em qualquer máquina com Windows ou Linux.
</p>

## Executando no Windows

<a href="https://www.dropbox.com/s/ma7anfgq5voyr7i/app_caes_e_raposas_win.exe?dl=0">Download do executável para Windows</a>

<p>
    Foi realizado o upload do executável para windows, portanto basta fazer o <b><a href="https://www.dropbox.com/s/ma7anfgq5voyr7i/app_caes_e_raposas_win.exe?dl=0">download</a></b> e executar na sua máquina. É possível que apareça uma mensagem dizendo que o executável pode não ser seguro. Ainda não sei como resolver isso, mas caso tenha dúvidas, pode analisar o código e criar seu próprio executável utilizando a biblioteca citada acima.
</p>

## Executando no Linux

<a href="https://www.dropbox.com/s/bz92q157rde9trz/app-caes-e-raposas-linux?dl=0">Download do executável para linux</a>

<p>
    Foi realizado o upload do executável para linux também, portanto basta fazer o <b><a href="https://www.dropbox.com/s/bz92q157rde9trz/app-caes-e-raposas-linux?dl=0">download</a></b> e executar pelo terminal na sua máquina. No linux não há problemas com mensagens de segurança, basta abrir a pasta do arquivo no terminal e executar o comando:
</p>

<code>./app-caes-e-raposas-linux</code>

