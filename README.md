# BEATING SUDOKU
Script utilizado para resolução dos jogos de 'SUDOKU'
## O que é Sudoku?
De acordo com a Wikipedia:

'*Sudoku*, por vezes escrito *Su Doku* (数独 sūdoku?) é um jogo baseado na colocação lógica de números. O objetivo do jogo é a colocação de números de 1 a 9 em cada uma das células vazias numa grade de 9×9, constituída por 3×3 subgrades chamadas regiões. O quebra-cabeça contém algumas pistas iniciais, que são números inseridos em algumas células, de maneira a permitir uma indução ou dedução dos números em células que estejam vazias. Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9. Resolver o problema requer apenas raciocínio lógico e algum tempo. Os problemas são normalmente classificados em relação à sua realização. O aspecto do sudoku lembra outros quebra-cabeças de jornal.'

Embora o Sudoku seja muitas vezes evitado devido à sua percebida complexidade, é importante ressaltar que os benefícios associados a esse jogo vão além da superfície desafiadora que ele apresenta. A prática do Sudoku não apenas aprimora o raciocínio lógico, mas também contribui para o desenvolvimento da memória e promove uma maior afinidade com números. Este jogo, muitas vezes subestimado, oferece uma oportunidade valiosa para o aprimoramento de habilidades cognitivas e a incorporação de aspectos positivos na vida cotidiana.




![SUDOKU](https://github.com/Karasam0506/BEATING_SUDOKU/assets/138382119/5df8e2ad-7c39-45a3-9b1f-2e69b2065a32)




## Objetivo/Método
A complexidade do Sudoku varia de acordo com o nível do jogo, apresentando desafios crescentes. Compreendendo essa dinâmica, este projeto visa desenvolver uma solução capaz de resolver a maioria das configurações do tabuleiro de Sudoku. A intenção é criar uma ferramenta eficaz e versátil para a resolução automatizada desse quebra-cabeça, contribuindo para a experiência e aprendizado relacionados ao Sudoku.

Utilizaremos o Python como nosso motor de alterações dentro do tabuleiro. Inicialmente, o processo apresenta os seguintes desafios:

1. Criação da Variável para Números no Tabuleiro: Estabelecer uma estrutura de dados eficiente para armazenar os números no tabuleiro: Utilizaremos o NumPy para criar uma matriz 9x9 que receberá os valores dispostos no tabuleiro de Sudoku. Na leitura inicial do tabuleiro, os espaços vazios são representados pelo valor '0', enquanto os demais valores são indicados pelos números de 1 a 9.

2. Visualização Aprimorada do Tabuleiro: Desenvolver uma visualização clara e amigável do tabuleiro: Para isso, foi criada uma função que imprime o tabuleiro 9x9, onde os valores por coluna são separados por '|' e por linha por '_', proporcionando uma visualização semelhante à disposição do tabuleiro.

3. Implementação de Métodos para Definir Células Modificáveis: Aplicar métodos que permitam a identificação e modificação das células que podem ser alteradas. Foram utilizados diversos métodos, como x-wing, xy-wing, resolução por eliminação, resolução por eliminação no setor e cadeia forçada.

4. Iteração dos Métodos até a Conclusão do Tabuleiro: Garantir a repetição eficaz dos métodos até que o tabuleiro esteja completamente resolvido. Foi criada uma função que executa repetidamente os métodos de resolução do Sudoku até que o tabuleiro esteja totalmente preenchido ou os métodos não possam atribuir mais valores corretos ao tabuleiro.

5. Acesso a uma Aplicação de Sudoku Online: Estabelecer uma conexão com um site que ofereça uma aplicação de Sudoku online. Foi escolhido o site 'https://sudoku.com/pt' para realizar as interações.

6. Leitura de Dados do Tabuleiro Online: Desenvolver mecanismos eficientes para extrair dados do tabuleiro online. Foi criada uma função que lê o HTML do site e adiciona as informações ao tabuleiro.

7. Interação com o Tabuleiro Online: Implementar funcionalidades que permitam interagir de forma coordenada com o tabuleiro online.

8. Tratamento de Erros quando o Valor Indicado não Estiver Correto: Implementar procedimentos para lidar com situações em que os valores indicados pelo projeto não correspondem aos requisitos esperados.
