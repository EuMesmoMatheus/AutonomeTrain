class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos = []
        self.max_movimentos = 50
        self.max_consecutivos = 20

    def mover(self, comandos):
        direcao_atual = None
        contador_consecutivos = 0

        if not comandos:
            raise ValueError("A lista de comandos está vazia.")

        for comando in comandos:
            if comando not in ['ESQUERDA', 'DIREITA']:
                raise ValueError(f"Comando inválido '{comando}'. Use 'ESQUERDA' ou 'DIREITA'.")

            if len(self.movimentos) >= self.max_movimentos:
                print("O trem atingiu o limite de 50 movimentos.")
                break

            if comando == direcao_atual:
                contador_consecutivos += 1
            else:
                direcao_atual = comando
                contador_consecutivos = 1

            if contador_consecutivos > self.max_consecutivos:
                print(f"O trem não pode fazer mais de {self.max_consecutivos} movimentos consecutivos na mesma direção.")
                break

            if comando == 'ESQUERDA':
                self.posicao -= 1
            elif comando == 'DIREITA':
                self.posicao += 1

            self.movimentos.append(comando)

    def status_final(self):
        return {
            'posicao_final': self.posicao,
            'total_movimentos': len(self.movimentos),
            'comandos_executados': self.movimentos
        }


#foi mal sor, ficou simples, não sabia se precisava fazer algo foda. ass: Os goHorse