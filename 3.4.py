def zad4(ticket: str):
    s1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    s2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if s1 == s2:
        return True
    else:
        return False
print(zad4("385916"))
print(zad4("231002"))