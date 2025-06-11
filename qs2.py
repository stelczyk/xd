partition_count = 0
partition_returns = []
inner_swaps_count = 0


def partition(a, l, r):
    """
    Wersja:
      pivot = a[r]
      i = l-1
      for j in [l..r-1]:
        if a[j] <= pivot:
          i += 1
          swap(a[i], a[j])    # <-- 'czerwony' swap
      swap(a[i+1], a[r])
      return i+1
    """
    global partition_count, partition_returns, inner_swaps_count
    partition_count += 1

    pivot = a[r]
    i = l - 1

    for j in range(l, r):
        if a[j] <= pivot:
            i += 1
            # --- 'czerwony' swap wewnątrz pętli ---
            a[i], a[j] = a[j], a[i]
            inner_swaps_count += 1

    # zamiana z pivotem na koniec
    a[i + 1], a[r] = a[r], a[i + 1]

    ret = i + 1
    partition_returns.append(ret)
    print(f"partition #{partition_count}: zwraca {ret}")
    return ret


def quicksort(a, l, r):
    # uwaga: w C++ był warunek if(l<=r) return;
    # prawdopodobnie chodzi o if l>=r: return
    if l >= r:
        return
    pi = partition(a, l, r)
    quicksort(a, l, pi - 1)
    quicksort(a, pi + 1, r)


if __name__ == "__main__":
    # Twoje dane — tutaj przykład z zadania:
    data = [3,2,8,4,3]

    print("Przed sortowaniem:", data)
    quicksort(data, 0, len(data) - 1)
    print("Po sortowaniu:   ", data)
    print("\n=== Podsumowanie ===")
    print(f"Łącznie wywołań partition:             {partition_count}")
    print(f"Lista zwracanych wartości pivotów:     {partition_returns}")
    print(f"Liczba „czerwonych” swapów w pętli for: {inner_swaps_count}")