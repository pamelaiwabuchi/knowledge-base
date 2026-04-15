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

Um programa pode ser classificado com processo eficiente quando ele maximiza a entrega de resultados minimizando o desperdício de hardware (CPU, RAM e I/O). Na prática, isso significa não deixar o processador "parado" esperando por uma tarefa lenta, como ler um arquivo, e organizar os dados na memória de um jeito que a CPU consiga acessá-los rápido (usando cache). Além disso, um bom processo não "vaza" memória, ou seja, ele libera o espaço que não usa mais para não travar o sistema. Ser eficiente é garantir que o computador faça o máximo de trabalho possível com o menor esforço e desperdício de energia.

Pontos-chave:

- CPU: não desperdiçar tempo em filas ou esperas.
- Cache: deixar os dados "perto" do processador para busca rápida.
- Memória: Não deixar o programa "engordar" (vazar) sem necessidade.
### Questão 2 - Para decisões dos processos:  Embora o Windows 11 não ofereça uma interface direta para configurar os escalonamentos de processos, podemos definir a prioridade dos processos específicos. Assim como as "afinidades dos processos", que é a alocação de determinados núcleos do processador para processos específicos. Neste contexto, os riscos de se redefinir as prioridades são .... complete a frase considerando ao menos 2 (dois) aspectos (escolha um e justifique).

Os riscos de se definir as prioridades são a instabilidade do sistema e a ocorrência de `starvation` (inanição) de  outros projetos.

Basicamente, se aumentarmos a prioridade de um processo comum para o nível "Tempo Real", o escalonador passa a dar 100% da preferência pra ele, o que pode impedir que processos vitais do próprio Windows recebam tempo de CPU. Isso gera instabilidade, porque se esse programa travar ou entrar em loop, o SO não consegue interromper. Resultado: o computador para de responder ao mouse e ao teclado, por exemplo. 

- **Instabilidade:** O Sistema Operacional perde a capacidade de gerenciar o hardware se um processo de usuário "rouba" toda a atenção da CPU.

- **Starvation (Inanição):** Processos com prioridade normal ou baixa podem nunca ser executados, "morrendo de fome" por falta de ciclos de processamento, o que causa lentidão extrema em outras tarefas do dia a dia.
### Questão 3 - Para decisões de memória:  Em sistemas operacionais como o Windows, ex., recomenda-se a memória virtual de 1,5 até 3 vezes o tamanho da memória física. De fora sucinta, que vantagens/desvantagem, comparativamente, existem em optar pela mínima e máxima configuração.**

**mínima (1,5):**
- Vantagem: economiza espaço de disco e força o SO a gerenciar melhor a RAM física, evitando que ele mova dados para o disco - que é mais lento - sem necessidade.
- Desvantagem: Se abrir muitos programas pesados ao mesmo tempo e a RAM física lotar, o sistema pode apresentar erros de "Memória insuficiente", fechando aplicativos abruptamente pra não travar.

**máxima (3x):**
- Vantagem: oferece maior estabilidade para multitarefa extrema. Dificilmente o sistema vai quebrar por falta de memória, pois tem um enorme reservatório extra no disco pra dados ociosos.
- Desvantagem: Pode causar lentidão no sistema. Como o disco é muito mais lento que a RAM, se o SO começar a usar demais esse espaço de 3x, o computador vai parecer arrastado, pois se passará mais tempo movendo dados entre disco e RAM do que realmente processando.