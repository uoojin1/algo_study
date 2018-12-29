# Technique 1 : Look for Bottlenecks, Unnecessary Work, Duplicated Work (Bud)

# example: Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3
# a, b, c, d are integers between 1 and 1000

# using brute force algorithm, 4 nested loops

# number_range = 1000
# for a in range(1, 1001):
#     for b in range(1, 1001):
#         for c in range(1, 1001):
#             for d in range(1, 1001):
#                 if pow(a,3) + pow(b,3) == pow(c,3) + pow(d,3):
#                     print(a, b, c, d)

# since there can only be one d that works with a, b, c

# for a in range(1, 1001):
#     for b in range(1, 1001):
#         for c in range(1, 1001):
#             d = pow(pow(a,3) + pow(b,3) - pow(c,3), 1/3)
#             if pow(a,3) + pow(b,3) == pow(c,3) + pow(d,3):
#                 print(a, b, c, d)

# why compute all c,d pairs for each a,b pair? try using hashmap

# pair_sum = {}
# for a in range(1, 1001):
#     for b in range(1, 1001):
#         result1 = pow(a,3) + pow(b,3)
#         pair_sum[result1] = {"a": a,"b": b}
# for c in range(1, 1001):
#     for d in range(1, 1001):
#         result2 = pow(c,3) + pow(d,3)
#         if result2 in pair_sum:
#             matching_pair = pair_sum[result2]
#             print(matching_pair["a"], matching_pair["b"], c, d)

# make this even smarter??

pair_sum = {}
for a in range(1, 1001):
    for b in range(1, 1001):
        result1 = pow(a,3) + pow(b,3)
        if result1 not in pair_sum:
            new_list = [(a, b)]
            pair_sum[result1] = new_list
        else:
            list = pair_sum[result1]
            list.append((a, b))
            pair_sum[result1] = list
for cube_sum in pair_sum:
    list = pair_sum[cube_sum]
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i][0] != list[j][0] and list[i][0] != list[j][1]:
                print(list[i][0], list[i][1], list[j][0], list[j][1])