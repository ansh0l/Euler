chain_length_dict = {1 : 1}
MILLION = 1000000

def next_term(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n + 1

def find_chain_length(n):
    chain_length_dict
    if chain_length_dict.has_key(n):
        return chain_length_dict[n]
    else:
        chain_length = 1 + find_chain_length(next_term(n))
        chain_length_dict[n] = chain_length
        return chain_length


def find_longest_chain():
    longest_chain_source, longest_chain_length = None, 0
    for num in range(2, MILLION): 
        chain_length = find_chain_length(num)
        if chain_length > longest_chain_length:
            longest_chain_source, longest_chain_length = num, chain_length
    return longest_chain_source, longest_chain_length

print find_longest_chain()
