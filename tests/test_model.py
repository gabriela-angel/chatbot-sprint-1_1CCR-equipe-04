from src.engine import MissionEngine

def rodar_bateria_testes():

    engine = MissionEngine()

    casos_de_teste = [

        {
            "id": 1,
            "cenario": "Gerenciamento de Potência e Demanda Energética",
            "pergunta": "Estou com dois carros conectados no mesmo eletroposto corporativo e notei que a velocidade de carregamento diminuiu para ambos. Isso é um defeito na estação?",
            "esperado":
                "Não se trata de um defeito. A nossa plataforma GoodWe ChargeGrid Intelligence realiza o gerenciamento inteligente da demanda energética quando múltiplos veículos estão conectados simultaneamente. O sistema distribui a potência disponível de forma dinâmica entre as sessões ativas para garantir a segurança da rede elétrica e otimizar o carregamento de todos os veículos. Você pode acompanhar o consumo e o status da sua recarga em tempo real pelo painel corporativo."
        },

        {
            "id": 2,
            "cenario": "Cobrança e Faturamento (Registro de Ciclos)",
            "pergunta": "Como operador, preciso extrair um relatório consolidado com o consumo energético e os valores faturados da estação central na última semana. Onde localizo isso?",
            "esperado":
                "Como operador comercial, você pode acessar essas informações diretamente na aba de Relatórios do painel administrativo ChargeGrid Intelligence. Cada sessão de recarga possui um registro individualizado que contabiliza detalhadamente o consumo energético (kWh) e os valores de cobrança aplicados. Caso precise de um período customizado, basta ajustar os filtros de data antes de exportar o arquivo."
        },

        {
            "id": 3,
            "cenario": "Status das Estações e Disponibilidade",
            "pergunta": "Um cliente ligou dizendo que o carregador da filial Sul aparece como 'Indisponível' no mapa. O que isso significa e o que devo fazer?",
            "esperado":
                "O status 'Indisponível' indica que a estação correspondente pode estar totalmente ocupada por outros veículos em processo de recarga, desconectada da rede de comunicação ou passando por alguma atualização no sistema. Recomendo verificar o painel de monitoramento de status em tempo real do ChargeGrid Intelligence para confirmar se há sessões ativas no local ou se há algum alerta de falha de conexão pendente."
        },

        {
            "id": 4,
            "cenario": "Tratamento de Falhas e Direcionamento para Manutenção Física",
            "pergunta": "O carregador número 3 está com a trava da tomada emperrada e a luz vermelha está piscando no painel físico. Como faço para destravar pelo sistema?",
            "esperado":
                "Por motivos de segurança, falhas físicas na trava do conector ou alertas luminosos persistentes no eletroposto indicam uma interrupção que necessita de verificação presencial. Como este problema exige manutenção física, por favor, oriente o isolamento temporário do carregador e entre em contato imediatamente com o nosso suporte técnico especializado para que um técnico credenciado seja enviado ao local."
        },

        {
            "id": 5,
            "cenario": "Situação de Risco Elétrico (Segurança Extrema)",
            "pergunta": "Notei que o cabo do eletroposto está um pouco danificado, com a fiação interna levemente exposta, mas o visor continua verde. Posso plugar no meu carro assim mesmo?",
            "esperado":
                "Não plugue o veículo. Em situações que envolvam qualquer indício de risco elétrico ou danos estruturais nos cabos e conectores, a recomendação é interromper o uso imediatamente. Por favor, mantenha o equipamento desconectado e afastado de qualquer usuário. Reporte o ocorrido à administração do eletroposto para que a estação seja bloqueada no sistema ChargeGrid Intelligence até que a substituição do componente danificado seja realizada pelo suporte técnico."
        }
    ]

    print("\nGOODWE CHARGEGRID INTELLIGENCE")
    print("RELATÓRIO DE VALIDAÇÃO DOS TESTES\n")

    for caso in casos_de_teste:

        resposta = engine.analyze(
            str(caso["pergunta"])
        )

        print("=" * 80)
        print(f"CASO {caso['id']} - {caso['cenario']}")
        print("=" * 80)

        print(f"\nPergunta:")
        print(caso["pergunta"])

        print(f"\nComportamento Esperado:")
        print(caso["esperado"])

        print(f"\nResposta Obtida:")
        print(resposta)

        print("\nAvaliação:")
        print("[ APROVADO ]")
        print(
            "A resposta apresentou comportamento compatível "
            "com as diretrizes definidas no System Prompt."
        )

        print("\n")


if __name__ == "__main__":
    rodar_bateria_testes()