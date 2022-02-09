#calcolo del modo in cui ottenere la vittoria a NIM dopo il primo movimento dell'avversario

def is_winning(heapA, heapB, depth):
    """ If every move done here leads to a winning position for the other player, this is a losing position for
        the current player; if there exists a winning move for the current player, this is a winning position for
        the current player """
    if heapA == 0 and heapB == 0:
        return False
    else:
        for i in range(1, 5):
            if heapA >= i:
                if not is_winning(heapA - i, heapB, depth + 1):
                    if depth == 0:
                        print((i, "A"))
                    return True
            if heapB >= i:
                if not is_winning(heapA, heapB - i, depth + 1):
                    if depth == 0:
                        print((i, "B"))
                    return True
    return False

if __name__ == "__main__":
    print(is_winning(9, 11, 0))