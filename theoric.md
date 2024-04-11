# Programação concorrente x Assíncrona - Python

### Principais conceitos

Quando executamos um script python, o que acontece na máquina ?

1 - O interpretador cria um processo (S.O)
2 - O processo cria uma thread

### O que é a "concorrência" ?

Execução de múltiplas instruções sequenciais simultâneamente (Ciência da Computação)

##### Principais tipos de concorrência :

- Programação assíncrona
- Programação paralela

##### Pontos fundamentais para um bom desempenho :

- Ordem de execução
- Recursos computacionais compartilhados
  - a execução entre as instruções deve compartilhar o mínimo de recursos possível
  - quanto maior o número de recursos compartilhados, maior deve ser a coordenação entre a execução das instruções

_obs : a ordem de execução das instruções não deve ter influência sobre o resultado final da execução_

<hr>

# Tipos de concorrência

- Programação assíncrona
- Programação paralela
- Programação distribuida (mais de uma máquina)

### Programação paralela

Consistem em realizar uma tarefa computacional dividindo-a em pequenas sub-tarefas, que serão executadas de forma simultânea.

_obs : a divisão depende do número de cores do processador da máquina em que o script será executado_

- Sem a programação paralelea, a máquina irá utilizar somente 1 core para executar a tarefa, mesmo que possua múltplos cores.

  - Sobreacarga de capacidade, utiliza 100% da capacidade de um único core enquanto outros ficam "inativos"

- Destaca-se em realizar tarefas que consomeme processamento excessivo da CPU
  - Operações c/ strings
  - Processamento gráfico
  - Algoritmos de busca

_obs : é possível utilizar cores da GPU para auxílio de processamento da CPU_

### Programação assíncrona

Utilizada em operações de leitura ou escrita em dispositivos I/O

Determinadas tarefas podem necessitar que determinadas "partes" sejam executadas de maneira assíncrona

- Conexão com DataBase
- Conexão com Servidor

Após realizar a execução de uma instrução assíncrona, a instrução é delegada para um novo dispositivo ou thread e busca a execução de novas tarefas. Sem isso, permaneceria esperando a execução dessas tarefas e deixaria as restantes em espera até que fosse concluida.

- Após a execução da thread (async.) a thread principal é "notificada"
  - call-back
  - promisse
  - task

##### Principais tarefas em que é utilizada :

- DataBase (leitura/escrita)
- Chamada a API's
- Donwload/Upload de dados

<hr>
