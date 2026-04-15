# Sistemas Operacionais e Redes de Computadores

### Definições:

*Sistema Operacional:* é o software de sistema mais importante do computador. Ele se posiciona entre o hardware e o usuário, gerenciando todos os recursos e fornecendo uma base para a execução de programas. Coração: Kernel - responsável por gerenciamento de processos, memória e drivers de dispositivo (falar com o hardware - teclado, mouse, etc)
Obs: Diferente de um "software de aplicação" (como VS Code), o SO é a infraestrutura que permite que os aplicativos existam e funcionem.

*Processo:* pode ser definido como um programa em execução. Ele possui estados (como pronto ou esperando) e utiliza recursos do sistema (CPU, memória, arquivos...)

## Processos
### Estados de um processo

1. Novo: o processo está sendo criado
2. Pronto (Ready): Está na RAM, na "fila", esperando a CPU ficar livre;
3. Executando (Running): Agora a CPU está processando as informações passadas;
4. Esperando/Bloqueado (Waiting): O processo pausou porque precisa de algo (ex.: esperar algum comando ser digitado no terminal)
5. Terminado (Terminated): O processo encerrou sua execução.

### Anatomia de um processo

É dividido em partes principais:

- Texto (Text) - contém o código binário (instruções) que a CPU vai ler;
- Dados (Data) - Armazena variáveis globais e estáticas - que são informações importantes que precisam persistir durante toda a vida útil do programa, desde o início até o fim
- Pilha (Stack) - Armazena dados temporários (parâmetros de funções, endereços de retorno e variáveis locais)
- Heap: Memória alocada dinamicamente durante a execução (quando por exemplo criamos uma lista em Python pro Masanori e ela é armazenada na memória RAM)

### Escalonamento de Processos

É um processo que decide qual processo terá o direito de usar a CPU em um determinado momento e por quanto tempo. Busca a eficiência do sistema.

*Preemptivo:* O SO tem o poder de interromper processos no meio da execução pra dar lugar pra outro mais importante. É o que permite a multitarefa.

*Não-preemptivo:* O processo usa a CPU até terminar ou até ele mesmo pedir pra sair. Ou seja, ele não interrompe o processo à força.

Por exemplo, como o Linux é preemptivo, se meu código Flask entrar em loop infinito, ainda consigo abrir o monitor do sistema e "matar"o processo. Se fosse um sistema não-preemptivo, minha única saída seria o botão de reset.

- FIFO (First-In, First-Out) - o primeiro que chega é o primeiro na execução
- SJF (Shortest Job First) - executa primeiro o que for mais rápido
- Round Robin (RR) - Cada processo ganha um tempo fixo. Se não terminar, volta para o fim da fila. 
## Perguntas para fixação:

 1. Sobre a definição de um sistema operacional, é correto afirmar que: 
[ ] É um software de aplicação utilizado para escrever programas em linguagem de alto nível.
**[ X ] Atua como intermediário entre o hardware e os programas de aplicação.**
[ ] Não interfere na gestão de recursos como memória e CPU.
[ ] Um processo pode estar em apenas dois estados: "executando" ou "esperando".
[ ] Um processo em estado "pronto" está apto para executar, mas aguarda ser escalonado.

*Obs: a última opção também está tecnicamente correta... *

 2. Em relação ao conceito de processo, é correto afirmar: 

 [ ] Um processo é equivalente a um programa armazenado em disco.
 **[ X ] Um processo é um programa em execução, incluindo seu contador de programa, pilha e dados.**
 [ ] Um processo é uma estrutura de hardware utilizada pela CPU.
[ ] O sistema operacional não interfere na criação ou destruição de processos.

 3. Sobre o estado dos processos, assinale a correta:

[ ] Um processo pode estar em apenas dois estados: "executando" ou "esperando".
**[ X ] Um processo em estado "pronto" está apto para executar, mas aguarda ser escalonado.**
[ ] Um processo em estado "bloqueado" está sendo executado pela CPU.
[ ] O estado "suspenso" indica que o processo foi finalizado com sucesso.

4. O que é o escalonamento de processos? 

[ ] A técnica de liberar memória RAM para novos programas.
**[ X ] O método de determinar qual processo terá acesso à CPU.**
[ ] A reorganização dos arquivos no sistema de arquivos.
[ ] A execução paralela de um mesmo processo em várias CPUs.

### Questão 1 - Processos e programas:  Em que aspectos os programas do desenvolvedor tornam-se processos eficientes?
 

>  Aspectos na prática:  Durante uma das aulas, abriu-se a interface de Gerenciamento de Tarefas do Windows, e buscou-se mostrar algumas possibilidades de configurações.

### Questão 2 - Para decisões dos processos:  Embora o Windows 11 não ofereça uma interface direta para configurar os escalonamentos de processos, podemos definir a prioridade dos processos específicos. Assim como as "afinidades dos processos", que é a alocação de determinados núcleos do processador para processos específicos. Neste contexto, os riscos de se redefinir as prioridades são .... complete a frase considerando ao menos 2 (dois) aspectos (escolha um e justifique).

### Questão 3 - Para decisões de memória:  Em sistemas operacionais como o Windows, ex., recomenda-se a memória virtual de 1,5 até 3 vezes o tamanho da memória física. De fora sucinta, que vantagens/desvantagem, comparativamente, existem em optar pela mínima e máxima configuração.**