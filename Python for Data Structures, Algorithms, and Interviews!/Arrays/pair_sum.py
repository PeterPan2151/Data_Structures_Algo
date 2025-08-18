def pair_sum(ar, target):
    if len(ar) < 2:
        return False
    
    seen = set()
    output = set()

    for i in ar:
        remaining = target - i
        if remaining not in seen:
            seen.add(i)
        else:
            output.add(((remaining, i)))
        
    return '\n'.join(map(str, list(output)))

print(pair_sum([1, 3, 2, 2], 4))