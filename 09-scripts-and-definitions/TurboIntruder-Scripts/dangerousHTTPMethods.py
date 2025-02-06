def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=3,
                           requestsPerConnection=1,
                           pipeline=False
                           )

    for httpmethod in open('/home/playbox/wordlists/http-methods/dangerous.txt'):
     engine.queue(target.req, httpmethod.rstrip())


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status not in [404, 405, 500, 405, 400]:
        table.add(req)