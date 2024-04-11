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
