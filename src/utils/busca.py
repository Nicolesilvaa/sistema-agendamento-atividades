def buscar_atividades(atividades, termo):
    """
    Busca atividades por nome  ou código.
    """
    termo = str(termo).lower()
    resultados = []
    for atv in atividades:
        if termo in atv.getNome().lower() or termo == atv.getCodigo().lower():
            resultados.append(atv)
    return resultados
