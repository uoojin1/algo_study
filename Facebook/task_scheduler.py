''' given array of characters from A to Z
where different letters represent different tasks.
tasks can be done without original order.
each task can be done in one interval,
for each interval, cpu could finish one task or just be idle

however there is mandatory cooldown for the CPU to process two same tasks 
cooldown = n

return the least number of intervals the CPU will take to finish all the given tasks

ex) [a,a,a,b,b,b,c,c] n = 2
==> a b c a b c a b
'''
import heapq

def leastInterval(tasks, cooldown):
    count = {}
    for task in tasks:
        if task in count:
            count[task] += 1
        else:
            count[task] = 1
    maxHeap = list(count.values())
    heapq._heapify_max(maxHeap) 
    cycles = 0
    while maxHeap:
        temp = []
        print 'maxHeap?', maxHeap
        for i in range(0, cooldown+1):
            if maxHeap:
                temp.append(maxHeap.pop())
        print 'temp???', temp
        for task in temp:
            if task - 1 > 0:
                maxHeap.append(task-1)
                heapq._heapify_max(maxHeap)
                # heapq.heappush(maxHeap, task-1)
                # print 'maxHeap??', maxHeap
        if not maxHeap:
            cycles += len(temp)
            print 'last loop', len(temp)
        else:
            print 'in else: ', cooldown + 1
            cycles += cooldown + 1
        print("HERE, maxHeap", maxHeap)
    print maxHeap
    return cycles
print leastInterval(['a','a','a','b','b','b','c','c'], 2)