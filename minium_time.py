def minimum_time(N, group_sizes, M, capacities):
    group_sizes.sort(reverse=True)
    capacities.sort()
    time=0
    while group_sizes:
        group=group_sizes.pop(0)
        if capacities:
            if group<=capacities[-1]:
                capacities.pop()
            else:
                group_sizes.insert(0, group-capacities[-1])
                capacities.pop()
            time+=2

    return time
N=4
group_sizes=[8, 1, 6, 9]
M=3
capacities=[7, 3, 2]

result=minimum_time(N, group_sizes, M, capacities)
print(f"Minimum time required: {result} units")
