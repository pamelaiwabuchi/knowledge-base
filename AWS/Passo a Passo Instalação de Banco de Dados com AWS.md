Dica: usuários Linux não precisam fazer a instalação do `bitvise`. Basicamente, ele faz no Windows o que o comando `ssh`, nativo do Linux, faz. Ou seja, seria redundante a utilização de `bitvise` no ambiente Linux. 


# Preparação e instalação

1. Conectar com o banco (copiar e colar do site da aba Cliente SSH)

2. Se Linux:  Alterar permissões de acesso ao arquivo de chave privada para o nível mais restrito exigido pelo protocolo SSH com o comando:

`chmod 400 DSM-DW-02.pem` .
`400` é o modo numérico que define quem pode fazer o quê.

- O primeiro dígito (4): Dono (você). O número 4 significa apenas leitura.
- O segundo dígito (0): Grupo. 0 significa nenhum acesso.
- O terceiro dígito (0): Outros usuários. 0 significa nenhum acesso.

3. Devemos verificar se o sistema operacional está com a lista atualizada de pacotes. Para isso, rodamos o comando `sudo apt update`. Ele atualiza a lista de pacotes disponíveis para que a máquina saiba que existem atualizações disponíveis, mas ele não as baixa. Essencial para o próximo passo de instalação do mysql-server-8.0.

`apt` - significa Advanced Package Tool (Ferramente de Pacote Avançada).

4. Pesquisar se o pacote existe: `apt cache search mysql-server` ou `apt search mysql-server`
5. Instalar o pacote escolhido: `sudo apt install mysql-server-8.0 -y`. Se der erro, pode ser porque a versão do Ubuntu utilizada mudou o nome padrão do pacote. Nesse caso, use `sudo apt install mysql-server -y`.

**Root** - Autoridade máxima no sistema Linux. Usado para tarefas de administração, como instalar o MySQL. 

6. `sudo apt install net-tools -y` - O pacote `net-tools` é uma coleção de utilitários de linha de comando para administração de redes no linux.

7. Assim que a instalação finalizar, vamos configurar a rede acessando o arquivo de configuração via terminal e alterando o Bind-Address  de `127.0.0.1`(localhost) para `0.0.0.0` (wildcard).

Assim o servidor MySQL aceita conexões vindas de qualquer 

8. A pasta `etc/init.d/` lista os serviços que possuem scripts de inicialização antigos.
## Como garantir que o servidor na nuvem 

**SSH**: Porta 22 - O protocolo SSH (Secure Shell) utiliza criptografia de chave pública para permitir o acesso remoto ao terminal. 
Ao abrir para `0.0.0.0/0` permitimos que qualquer endereço IP na internet conecte à porta 22.   
**Liberação da Porta 3306 (mySQL):** 

![[Pasted image 20260503143220.png]]

Exemplo visual de onde alterar

![[Pasted image 20260503143419.png]]

- Reiniciar o serviço (obrigatório para aplicar mudanças) `sudo systemctl restart mysql`.

![[Pasted image 20260503143929.png]]

`mysql -u root -p`- 
`sudo mysql` - para entrar no mysql
o terminal fica:
mysql>
Agora vamos:
1. Criar DATABASE; 
2. Criar uma tabela simples;
3. Inserir um dado;

![[Pasted image 20260503145333.png]]

`sudo /etc/init.d/mysql status` - verifica o estado atuald o serviço de banco de dados MySQL, informando se ele está ativo (running), parado (stopped) ou se houve algum erro na inicialização.

`start` - carrega o processo do servidor MySQL na memória RAM e o executa como um *daemon*. Quando executamos o `start`, o sistema reserva uma fatia da memória RAM e define a prioridade do uso da CPU para o MySQL (Alocação de recursos).
2. Leitura de COnfiguração - O processo lê o arquivo `my.cnf`(geralmente em `/etc/mysql`para saber em qual porta rodas (padrão 3306) e onde estão os arquivos de dados.
3. Abertura de Sockets: O MySQL abre uma porta de comunicação para aceitar conexões. Sem o serviço estar 'iniciado', qualquer tentativa de conexão via aplicação (PHP, Python, Java) ou terminal resultará no erro `ERROR 2002 (HY000): Can't connect to local MySQL server though socket`.
4. Verificação de INtegridade: Ele verifica se os arquivos de log e tabelas não estão corrompidos antes de permitir o acesso aos dados.
Um *daemon* 



