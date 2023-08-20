# Simulador de Autômatos Finitos
Projeto com o objetivo de fazer um Simulador de Autômatos Finitos.

Descrição
O Simulador de Autômatos Finitos é uma ferramenta desenvolvida em Python que permite simular o comportamento de autômatos finitos a partir de especificações e casos de teste. Ele facilita a verificação e validação do comportamento de autômatos finitos, sendo útil para entender como uma máquina de estados processa sequências de entrada.

Funcionamento
O simulador carrega as informações do autômato finito de um arquivo no formato JSON, onde são definidas as transições entre os estados, o estado inicial e os estados de aceitação. Além disso, ele lê os casos de teste de um arquivo CSV, em que cada linha contém uma palavra de entrada e o resultado esperado (0 para rejeitar, 1 para aceitar).

Depois de carregar as informações do autômato e dos casos de teste, o simulador executa a simulação para cada caso. Ele processa a palavra de entrada no autômato, seguindo as transições de estado para cada símbolo. O resultado da simulação (aceitação ou rejeição) é registrado, juntamente com o tempo de execução.

Exemplo de Uso
Suponhamos que temos o seguinte autômato:
Transições: {
  "q0": { "0": "q1", "1": "q0" },
  "q1": { "0": "q0", "1": "q1" }
}

Estado Inicial: "q0"
Estados de Aceitação: ["q0"]
E possuímos o seguinte arquivo test_cases.csv:

01;0
10;1
000;0
111;0

Ao executar o simulador com esses arquivos, obteríamos resultados semelhantes a:

Palavra de Entrada;Resultado Esperado;Resultado Obtido;Tempo de Execução
01;0;1;0.000000
10;1;1;0.000000
000;0;0;0.000000
111;0;0;0.000000

Isso demonstra como o simulador processa as entradas de teste, compara os resultados esperados com os resultados obtidos e registra o tempo de execução.
