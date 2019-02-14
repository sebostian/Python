def testBinarySearch():
    from binarySearch import binarySearch
    list = [1, 3, 5, 7, 9]
    print (binarySearch(list, 5))
    print (binarySearch(list, 50))
    print (binarySearch(list, 9))
    print (binarySearch(list, 1))
    
def testSelectSort():
    from selectSort import selectSort
    data1 = [-10, 1, 3, 5, 7, 2, -9, 0, 8, 6, 7, 7, 80]
    print (selectSort(data1))

def test_factorial():
    from Factorial import factorial
    print(factorial(5))

def testFunc():
    from func import func
    data = [5, 1, 8, 9, 4, 100]
    print(func(data))
    
def testMaxFunc():
    from func import funcMax
    data = [5, 61, 40, 1, 11, 2]
    print(funcMax(data))

def testQSort():
    from qSort import qSort
    data = [5, 0, 1, 8, 5, 6, 3, 2, 4, 1, -9]
    print(qSort(data))

def testCheckSum():
    from checkSum import checkSumIsValid
    data = [500, 0, 10, 17, 596, 126]
    print(checkSumIsValid(data, 1023))

def test_breadth_first_search():
    from BreadthFirstSearch import breadth_first_search
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["tom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []
    
    seller = breadth_first_search(graph, "you")
    print(seller)

def test_dijkstra():
    from Dijkstra import dijkstra

    graph = {}
    graph["book"] = {}
    graph["disk"] = {}
    graph["poster"] = {}
    graph["drum"] = {}
    graph["bas-guitar"] = {}
    
    graph["book"]["poster"] = 0
    graph["book"]["disk"] = 5

    graph["disk"]["bas-guitar"] = 15
    graph["disk"]["drum"] = 30

    graph["poster"]["bas-guitar"] = 30
    graph["poster"]["drum"] = 35

    graph["bas-guitar"]["piano"] = 20
    graph["drum"]["piano"] = 10


    cost = {}

    cost[("book", "disk")] = 5
    cost["book","poster"] = 0
    cost["disk","bas-guitar"] = 15
    cost["disk","drum"] = 30
    cost["poster","bas-guitar"] = 30
    cost["poster","drum"] = 35
    cost["bas-guitar","piano"] = 20
    cost["drum","piano"] = 10
   
    result = dijkstra(graph, cost, "book")
    #print(result)


test_dijkstra()
