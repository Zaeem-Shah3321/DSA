def minimize_cash_flow(graph):
    def get_min_index(balances):
        min_index = 0
        for i in range(1, len(balances)):
            if balances[i] < balances[min_index]:
                min_index = i
        return min_index

    def get_max_index(balances):
        max_index = 0
        for i in range(1, len(balances)):
            if balances[i] > balances[max_index]:
                max_index = i
        return max_index

    def min_cash_flow_rec(balances):
        max_credit = get_max_index(balances)
        max_debit = get_min_index(balances)

        if balances[max_credit] == 0 and balances[max_debit] == 0:
            return []

        min_amount = min(-balances[max_debit], balances[max_credit])
        balances[max_credit] -= min_amount
        balances[max_debit] += min_amount

        transactions = [(max_debit, max_credit, min_amount)]
        transactions += min_cash_flow_rec(balances)
        return transactions

    balances = list(graph.balances.values())
    transactions = min_cash_flow_rec(balances)
    return transactions