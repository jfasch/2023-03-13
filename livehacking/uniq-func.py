def uniq(seq):
    seq_ret = []
    have = set()
    
    for num in seq:
        if num not in have:
            seq_ret.append(num)
            have.add(num)
    
    return seq_ret
    
input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq(input_list)

for num in output_list:
    print(num)
