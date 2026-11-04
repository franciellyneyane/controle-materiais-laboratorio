"""Controle simples de materiais para um laboratório de informática.

Executar com: python3 controle_materiais.py
Os dados existem apenas enquanto o programa está aberto.
"""


def buscar_material(materiais, nome):
    """Procura um material pelo nome, sem diferenciar maiúsculas."""
    for material in materiais:
        if material["nome"].lower() == nome.strip().lower():
            return material
    return None


def adicionar_material(materiais, nome, quantidade, minimo):
    """Valida e adiciona um material à lista."""
    nome = nome.strip()
    if nome == "":
        raise ValueError("O nome não pode ficar vazio.")
    if buscar_material(materiais, nome) is not None:
        raise ValueError("Já existe um material com esse nome.")
    if quantidade < 0 or minimo < 0:
        raise ValueError("As quantidades não podem ser negativas.")

    material = {"nome": nome, "quantidade": quantidade, "minimo": minimo}
    materiais.append(material)
    return material


def movimentar_material(material, tipo, quantidade):
    """Registra uma entrada ou saída e atualiza a quantidade."""
    if quantidade <= 0:
        raise ValueError("Informe uma quantidade maior que zero.")

    if tipo == "entrada":
        material["quantidade"] += quantidade
    elif tipo == "saida":
        if quantidade > material["quantidade"]:
            raise ValueError("Não há material suficiente para essa saída.")
        material["quantidade"] -= quantidade
    else:
        raise ValueError("Tipo de movimentação inválido.")

    return material["quantidade"]


def ler_numero(pergunta, minimo=0):
    """Lê um número inteiro e repete a pergunta enquanto for inválido."""
    while True:
        try:
            numero = int(input(pergunta))
            if numero < minimo:
                print("Digite um número maior ou igual a", minimo)
            else:
                return numero
        except ValueError:
            print("Digite um número inteiro.")


def listar_materiais(materiais):
    if len(materiais) == 0:
        print("Ainda não há materiais cadastrados.")
        return

    print("\nMATERIAL | QUANTIDADE | MÍNIMO")
    for material in materiais:
        aviso = " - precisa repor" if material["quantidade"] <= material["minimo"] else ""
        print(material["nome"], "|", material["quantidade"], "|", material["minimo"], aviso)


def cadastrar_pelo_menu(materiais):
    nome = input("Nome do material: ")
    quantidade = ler_numero("Quantidade atual: ")
    minimo = ler_numero("Avisar quando chegar a (mínimo): ")
    adicionar_material(materiais, nome, quantidade, minimo)
    print("Material cadastrado.")


def fazer_movimentacao(materiais, tipo):
    nome = input("Nome do material: ")
    material = buscar_material(materiais, nome)
    if material is None:
        print("Material não encontrado. Confira o nome na lista.")
        return

    quantidade = ler_numero("Quantidade: ", 1)
    try:
        saldo = movimentar_material(material, tipo, quantidade)
        print("Movimentação registrada. Quantidade atual:", saldo)
    except ValueError as erro:
        print(erro)


def mostrar_materiais_para_repor(materiais):
    encontrados = False
    print("\nMateriais no mínimo ou abaixo dele:")
    for material in materiais:
        if material["quantidade"] <= material["minimo"]:
            print("-", material["nome"], "(quantidade:", material["quantidade"], ")")
            encontrados = True
    if not encontrados:
        print("Nenhum material precisa de reposição agora.")


def main():
    materiais = []

    while True:
        print("\n=== CONTROLE DE MATERIAIS DO LABORATÓRIO ===")
        print("1 - Cadastrar material")
        print("2 - Listar materiais")
        print("3 - Registrar entrada")
        print("4 - Registrar saída/uso")
        print("5 - Ver materiais para repor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                cadastrar_pelo_menu(materiais)
            elif opcao == "2":
                listar_materiais(materiais)
            elif opcao == "3":
                fazer_movimentacao(materiais, "entrada")
            elif opcao == "4":
                fazer_movimentacao(materiais, "saida")
            elif opcao == "5":
                mostrar_materiais_para_repor(materiais)
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Escolha uma opção do menu.")
        except ValueError as erro:
            print(erro)


if __name__ == "__main__":
    main()
