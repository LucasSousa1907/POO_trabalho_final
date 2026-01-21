# SISTEMA DE IDENTIFICAÇÃO DE PLANTAS DA AMAZÔNIA

## Descrição do projeto
Este projeto foi desenvolvido como Trabalho Final da disciplina de Programação Orientada a Objetos (POO).
O software simula um sistema taxonômico automatizado para identificar espécies vegetais da flora amazônica, utilizando
uma árvore de decisão baseada em perguntas morfológicas (flores, frutos, caule e folhas) através de um menu CLI.
após fazer a identificação da planta, o usuario pode visualizar as plantas identificadas e consultar a hierarquia taxonômica básica de cada planta.

## instruções de execução
### pré requisitos:
-python 3.8 ou superior
-IDE

### execução:
-Clone este repositório ou baixe os arquivos.
-Abra o terminal na pasta raiz do projeto.
-Execute o arquivo principal(main_menu.py):
o programa exibirá um menu interativo no terminal, do qual a primeira opção é a de identificação de plantas através da resposta de perguntas.
As plantas identificadas ficam registradas enquanto o programa estiver em execução.

### observações
os dados não são guardados após a execução do programa
as respostas devem seguir o formato solicitado

## evidências de resultados obtidos
### entrada do usuário:
A planta em questão possui flores ? (s/n)
s
A planta possui frutos ? (s/n)
s
A planta possui:
1. Folhas finas e compridas
2. Folhas largas e espalhadas
Escolha uma opção:
### saída esperada:
Planta identificada: castanheira-do-pará

### vizualização das plantas identificadas:
Plantas identificadas:
1. castanheira-do-pará
2. bananeira amazônica

### hierarquia das plantas
entrada:
Escolha uma das plantas identificadas:
>1
saída:
>castanheira-do-pará < Bertholletia < Reino Plantae

