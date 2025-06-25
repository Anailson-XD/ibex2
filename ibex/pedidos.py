class HistoricoPedidos:
    def __init__(self, cliente_login, db_path="ibex.db"):
        self.cliente_login = cliente_login
        self.db_path = db_path
        self.cliente_id = self._buscar_id_cliente()

    def _buscar_id_cliente(self):
        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()
        cursor.execute("SELECT id FROM cliente WHERE login = ?", (self.cliente_login,))
        resultado = cursor.fetchone()
        con.close()
        return resultado[0] if resultado else None

    def obter_pedidos(self):
        if not self.cliente_id:
            return []

        con = sqlite3.connect(self.db_path)
        cursor = con.cursor()
        cursor.execute("""
            SELECT nome_produto, quantidade, preco_unitario, id_empresa
            FROM carrinho
            WHERE id_cliente = ?
        """, (self.cliente_id,))
        pedidos = cursor.fetchall()
        con.close()
        return pedidos

def ver_pedidos():
    global cliente_logado
    exibir_subtitulo('Histórico de pedidos: ')

    if not cliente_logado:
        print("Você precisa estar logado como cliente para ver os pedidos.")
        input("Pressione ENTER para continuar...")
        return

    historico = HistoricoPedidos(cliente_logado)
    pedidos = historico.obter_pedidos()

    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for idx, (nome, qtd, preco, empresa_id) in enumerate(pedidos, start=1):
            print(f"{idx}. Produto: {nome}")
            print(f"   Quantidade: {qtd}")
            print(f"   Preço unitário: R${preco:.2f}")
            print(f"   ID da empresa: {empresa_id}")
            print("---------------------------")

    input("Pressione ENTER para continuar...")
