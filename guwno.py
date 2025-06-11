# --- quicksort z pełnym logowaniem dla partition ---

# globalne liczniki i lista wyników
partition_count       = 0
partition_returns     = []
inner_swaps_count     = 0

def partition(a, l, r):
    """
    działa jak w Twoim C++:
      - pivot = a[r]
      - i od l-1 rośnie, j od r maleje
      - while true: porównaj a[i]<pivot, a[j]>pivot,
        break gdy i>=j, w pętli wymieniaj a[i] z a[j]
      - na koniec podmień pivot: a[i] <-> a[r]
      - zwróć i
    """
    global partition_count, partition_returns, inner_swaps_count
    partition_count += 1

    pivot = a[r]
    i = l - 1
    j = r

    while True:
        # przesuwamy i w prawo aż znajdziemy >= pivot
        i += 1
        while a[i] < pivot:
            i += 1
        # przesuwamy j w lewo aż znajdziemy <= pivot
        j -= 1
        while j >= l and a[j] > pivot:
            j -= 1

        # jeśli się minęliśmy, koniec
        if i >= j:
            break

        # ---------- „czerwony” swap wewnątrz pętli ----------
        a[i], a[j] = a[j], a[i]
        inner_swaps_count += 1

    # zamiana z pivotem na koniec
    a[i], a[r] = a[r], a[i]

    # logowanie zwracanej wartości
    partition_returns.append(i)
    print(f"partition #{partition_count}: zwraca {i}")

    return i

def quicksort(a, l, r):
    if l < r:
        pi = partition(a, l, r)
        quicksort(a, l,     pi-1)

        quicksort(a, pi+1, r)

if __name__ == "__main__":
    # przykładowe dane — podstaw tu swoją listę:
    data = [1,1,3,1,6,0,8,7]

    print("Przed sortowaniem:", data)
    quicksort(data, 0, len(data)-1)
    print("Po sortowaniu:   ", data)
    print()
    print("=== Podsumowanie ===")
    print(f"Total wywołań partition: {partition_count}")
    print(f"Zwroty z partition:      {partition_returns}")
    print(f"Liczba „czerwonych” swapów wewnątrz pętli: {inner_swaps_count}")
