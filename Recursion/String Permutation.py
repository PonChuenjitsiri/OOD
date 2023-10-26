def permute_string(s, k):
    def generate_permutations(prefix, remaining):
        if len(prefix) == k:
            return [prefix]
        
        permutations = []
        for i in range(len(remaining)):
            new_prefix = prefix + remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            permutations += generate_permutations(new_prefix, new_remaining)
        
        return permutations
    
    all_permutations = generate_permutations("", s)
    unique_permutations = list(set(all_permutations))
    sorted_unique_permutations = sorted(unique_permutations)
    
    return sorted_unique_permutations

input_string_kvalue = input("Enter a string and k: ").split("/")
if int(input_string_kvalue[1]) > len(input_string_kvalue[0]):
    print("Invalid value of k. k must be less than or equal to the length of the string.")
elif int(input_string_kvalue[1]) < 0:
    print("Invalid value of k. k must be a non-negative integer.")
else:
    result = permute_string(input_string_kvalue[0], int(input_string_kvalue[1]))
    print(result)
