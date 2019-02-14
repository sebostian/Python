from collections import deque

def breadth_first_search(graph, name):
    result = None
    search_queue = deque()
    search_queue += graph[name]
    searched_already = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            return person
        else:
            searched_already.append(person)
            search_queue += graph[person]

    return result

def person_is_seller(person):
    return person[-1] == "m"
