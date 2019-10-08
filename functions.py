def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def find_matching_substrings(A, B):

    if len(A) == 0 or len(B) == 0:
        return []
    
    keep_going = True
    cur_index = 0
    results = []

    while keep_going:
        search_area = A[cur_index:]
        if search_area.find(B) != -1:
            results.append(search_area.find(B) + cur_index)
            cur_index += search_area.find(B) + 1
        else:
            keep_going = False
    
    return results

result = find_matching_substrings('twone', 'one')
print(result)