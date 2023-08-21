# -*- coding: utf-8 -*-
#Especificamos a codificação de caracteres
import json
import csv
import sys
import time
#Importamos os modulos necessarios para manipularmos o JSON e o CSV


class FiniteAutomaton:
    def __init__(self, transitions, start_state, accept_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        
#Definição da classe do automato com um construtor para as regras de transição (estado inicial e estado de aceitação)
    
    def process_input(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol not in self.transitions[current_state]:
                return False
            current_state = self.transitions[current_state][symbol]

        return current_state in self.accept_states

#Metodo para simular o processamento do automato a partir da entrada utilizada.

def load_automaton(file_path):
    with open(file_path, 'r') as f:
        automaton_data = json.load(f)
        return FiniteAutomaton(automaton_data['transitions'], automaton_data['start_state'], automaton_data['accept_states'])
#Função para carregar os dados de um arquivo json e criar uma instancia. 


def load_test_cases(file_path):
    test_cases = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            input_string, expected_result = row
            test_cases.append((input_string, int(expected_result)))
    return test_cases
#função para carregar casos de teste de um arquivo csv e prepara-los como pares de entrada e saida.

def simulate_and_write_results(automaton, test_cases, output_file):
    with open(output_file, 'w') as f:
        f.write("Palavra de Entrada;Resultado Esperado;Resultado Obtido;Tempo de Execução\n")
        for input_string, expected_result in test_cases:
            start_time = time.time()
            result = automaton.process_input(input_string)
            elapsed_time = time.time() - start_time
            f.write(f"{input_string};{expected_result};{int(result)};{elapsed_time:.6f}\n")
#Função para simular o automato e escrever os resultados em um arquivo de saida (no caso nosso arquivo de saida é o output_results)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python simulator.py automaton.json test_cases.csv output_results.out")
        sys.exit(1)
#Verificaão do numero de argumentos da linha de comando
    
    automaton_file = sys.argv[1]
    test_cases_file = sys.argv[2]
    output_file = sys.argv[3]

    automaton = load_automaton(automaton_file)
    test_cases = load_test_cases(test_cases_file)
    simulate_and_write_results(automaton, test_cases, output_file)

#Carregamento do automato dos casos de teste e escrita / definição dos resultados (é aqui em que tudo sera carregado / puxado dos arquivos)
