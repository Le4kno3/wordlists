def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=3,
                           requestsPerConnection=1,
                           pipeline=False
                           )
    engine.queue(target.req, "OPTIONS")


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status not in [404, 405, 500, 405, 400]:
        table.add(req)