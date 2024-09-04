from autonomeTrain import TremAutonomo

def executar_testes():
    try:
        comandos_invalidos = ['DIREITA', 'esquerda', 'UP']
        trem_invalido = TremAutonomo()
        trem_invalido.mover(comandos_invalidos)
    except ValueError as e:
        print(f"Teste de comando inválido: {e}")

    try:
        comandos_vazios = []
        trem_vazio = TremAutonomo()
        trem_vazio.mover(comandos_vazios)
    except ValueError as e:
        print(f"Teste de lista vazia: {e}")

    comandos_violacao_50_movimentos = ['DIREITA'] * 51
    trem_50_movimentos = TremAutonomo()
    trem_50_movimentos.mover(comandos_violacao_50_movimentos)
    status_50_movimentos = trem_50_movimentos.status_final()
    print(f"Teste de 50 movimentos: Posição Final: {status_50_movimentos['posicao_final']}")

    comandos_violacao_consecutivos = ['ESQUERDA'] * 21
    trem_consecutivo = TremAutonomo()
    trem_consecutivo.mover(comandos_violacao_consecutivos)
    status_consecutivo = trem_consecutivo.status_final()
    print(f"Teste de 20 movimentos consecutivos: Posição Final: {status_consecutivo['posicao_final']}")

    comandos_borda_negativa = ['ESQUERDA']
    trem_borda_negativa = TremAutonomo()
    trem_borda_negativa.mover(comandos_borda_negativa)
    status_borda_negativa = trem_borda_negativa.status_final()
    print(f"Teste de condição de borda (posições negativas): Posição Final: {status_borda_negativa['posicao_final']}")

    comandos_borda_50_movimentos = ['DIREITA'] * 48 + ['ESQUERDA'] * 3
    trem_borda_50 = TremAutonomo()
    trem_borda_50.mover(comandos_borda_50_movimentos)
    status_borda_50 = trem_borda_50.status_final()
    print(f"Teste próximo ao limite de 50 movimentos: Posição Final: {status_borda_50['posicao_final']}")

if __name__ == "__main__":
    executar_testes()
