# from collections import deque
# from heapq import heappush, heappop

Gstate = [0,1,2,3,4,5,6,7,8]

class Node:
    def __init__(self, state, parent, operator, cost, weight):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.cost = cost
        #weight = heuristic(state) + cost
        #print "print weight"
        #print heuristic(state)
        self.weight = weight

def heuristic(state):
    hr = 0
    for s in state:
        if (s == 0):
            continue

        r = abs(state.index(s)/3 - Gstate.index(s) / 3)
        c = abs(state.index(s)%3 - Gstate.index(s) %3)
        hr += c + r
    return hr

def moves(currentnode,queue):
    extended_nodes = []
    state = currentnode.state [:]
    index = state.index(0)
    print "current"
    print currentnode.state
    # case left
    if not (index == 0 or index == 3 or index == 6):
        temp_state = state[:]
        temp = temp_state[index - 1]
        temp_state[index - 1] = temp_state[index]
        temp_state[index] = temp
        print "temp left"
        print temp_state
        extended_nodes.append(
            Node(temp_state, currentnode, "left", currentnode.cost + 1, heuristic(temp_state) + (currentnode.cost + 1)))
    # case right
    if not (index == 2 or index == 5 or index == 8):
        temp_state = state[:]
        temp = temp_state[index + 1]
        temp_state[index + 1] = temp_state[index]
        temp_state[index] = temp
        print "temp right"
        print temp_state
        extended_nodes.append(Node(temp_state, currentnode, "right", currentnode.cost + 1, heuristic(temp_state) + (currentnode.cost + 1)))
    # down
    if not (index == 6 or index == 7 or index == 8):
        temp_state = state[:]
        temp = temp_state[index + 3]
        temp_state[index + 3] = temp_state[index]
        temp_state[index] = temp
        print "temp down"
        print temp_state
        extended_nodes.append(Node(temp_state, currentnode, "down", currentnode.cost + 1, heuristic(temp_state) + (currentnode.cost + 1)))
    #case up
    if not (index == 0 or index == 1 or index == 2):
        temp_state = state[:]
        temp = temp_state[index - 3]
        temp_state[index-3] = temp_state[index]
        temp_state[index] = temp
        print "temp up"
        print temp_state
        extended_nodes.append(Node(temp_state,currentnode,"up",currentnode.cost+1,heuristic(temp_state)+(currentnode.cost+1)))




    return extended_nodes

def goaltest(state):
    if state == Gstate:
        return 1
    else:
        return 0

#function used in the heap of A*
def swap(i, j,heap):
    heap[i], heap[j] = heap[j], heap[i]

def heapify(end, i,heap):
    l = 2 * i + 1
    r = 2 * (i + 1)
    min = i
    if l < end and heap[i].weight > heap[l].weight:
        min = l
    if r < end and heap[min].weight > heap[r].weight:
        min = r
    if min != i:
        swap(i, min,heap)
        heapify(end, min,heap)

def heap_sort(heap):
    end = len(heap)
    start = end // 2 - 1  # use // instead of /
    for i in range(start, -1, -1):
        heapify(end, i,heap)


def BFS(Istate):
    frontier = []
    frontier.append(Node(Istate,None,None,0,0))
    explored = []
    moveslist = []
    while (frontier):
        current = frontier.pop(0)
        if not current.state in explored:
            print"not explored"
            print current.state
            moveslist.append(current.operator)
            explored.append(current.state)
            if goaltest(current.state):
                print moveslist
                return explored
            else:
                temp = moves(current,frontier)
                frontier.extend(temp)



def DFS(Istate):
    frontier = []
    frontier.append(Node(Istate,None,None,0,0))
    explored = []
    moveslist = []
    while (frontier):
        current = frontier.pop()
        if not current.state  in explored:
            moveslist.append(current.operator)
            explored.append(current.state)
            if goaltest(current.state):
                print moveslist
                return explored
            else:
                temp = moves(current,frontier)
                frontier.extend(temp)

def ASTAR(Istate):
   heap = []
   heap.append(Node(Istate,None,None,0,0))
   explored = []
   moveslist = []
   while heap:
       current = heap.pop(0)
       #neighbors = moves(current,heap)
       #temp = neighbors[0]
       #for x in neighbors:
       #    if x.weight < temp.weight:
       #        temp = x
       if current.state not in explored:
           moveslist.append(current.operator)
           explored.append(current.state)
           if goaltest(current.state):
               print(moveslist)
               return explored
           else:
               print "print weight"
               print current.weight
               temp = moves(current,heap)
               heap.extend(temp)
               heap_sort(heap)
def main():
   #node = Node([1,2,5,3,4,0,6,7,8],None,None,0,0)
   node = Node([1, 2, 0, 3, 4, 5, 6, 7, 8], None, None, 0, 0)
   list2 = ASTAR(node.state)
   print "Solved A*"
   print (list2)
   list1 = BFS(node.state)
   print "Solved in BFS"
   print (list1)
   list = DFS(node.state)
   print "Solved in DFS"
   print (list)
main()