''' Mateiral structure
{
    'id': number,
    'name': 'string',
    'parent_id': number

}
'''


def printCourseMaterial(materials):
    nodeChildern = {}
    for material in materials:
        if material.parent_id in nodeChildren:
            nodeChildren[material.parent_id] = nodeChildre[material.parent_id].append(material)
        else:
            nodeChildern[material.parent_id] = [material]
    # we have the hashmap that contains key: parent_id and value and the keys of the 
    printOrder = nodeChildern[None]

    def printThings(count, node):
        dashes = ''
        for i in range(0, count):
            dashes += '-'
        print dashes + node['name']
        children = nodeChildren[node['id']]
        for child in children:
            printThings(count +1, child)
    for item in printOrder:
        printThings(0, item)
    

def numberOfFieldsPresent(fields):
    if not fields:
        return 0
    visited = set()
    def explore(i, j):
        if i < 0 or j < 0 or i > len(fields) or j > len(fields[0]):
            return
        if fields[i][j] != True:
            return
        visited.add((i,j)
        explore(i-1,j)
        explore(i+1,j)
        explore(i, j+1)
        explore(i, j-1)

    count = 0
    for i in range(0, len(fields)):
        for j in range(0, len(fields[0])):
            # if i < 0 or i > len(fields) or j < 0 or j > len(fields[0]) or fields[i][j] == 'False':
            if fields[i][j] == True and (i,j) not in visited:
                explore(i,j)
                count += 1
    return count