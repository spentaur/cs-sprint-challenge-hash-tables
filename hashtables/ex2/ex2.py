#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    routes = {ticket.source: ticket.destination for ticket in tickets}
    route = []
    last = 'NONE'
    for _ in range(len(routes)):
        last = routes[last]
        route.append(last)
    return route
