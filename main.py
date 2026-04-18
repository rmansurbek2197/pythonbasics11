def top_min_max(sonlar):
    if len(sonlar) == 0:
        return None
    min_son = sonlar[0]
    max_son = sonlar[0]
    for son in sonlar:
        if son < min_son:
            min_son = son
        elif son > max_son:
            max_son = son
    return min_son, max_son

sonlar = [12, 45, 7, 23, 56, 89, 34]
min_son, max_son = top_min_max(sonlar)
print("Minimal qiymat:", min_son)
print("Maksimal qiymat:", max_son)

def top_min_max_list(sonlar):
    if len(sonlar) == 0:
        return None
    min_son = min(sonlar)
    max_son = max(sonlar)
    return min_son, max_son

sonlar = [12, 45, 7, 23, 56, 89, 34]
min_son, max_son = top_min_max_list(sonlar)
print("Minimal qiymat (list):", min_son)
print("Maksimal qiymat (list):", max_son)