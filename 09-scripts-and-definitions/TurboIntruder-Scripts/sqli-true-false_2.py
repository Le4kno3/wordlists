import urllib

PAYLOAD_HOME = '/home/playbox/Documents/Github/wordlists'
payload_path = PAYLOAD_HOME + "/01-attacks/sqli/FINAL_tf_payloads.txt"
previousReq = ""
previousResponseLength = 0
previousWords = ""

failedAttempt = 'a'


def queueRequests(target, wordlists):
    engine = RequestEngine(
        endpoint=target.endpoint,
        concurrentConnections=1,
        requestsPerConnection=1,
        pipeline=False,
        maxRetriesPerRequest=1,
        engine=Engine.BURP
    )

    for payload1 in open(payload_path):
            engine.queue(target.req, urllib.quote_plus(payload1.rstrip()))


# make sure to select the position of payload properly `value$ $`

def difference(string1, string2):
    # split string into characters
    A = list(string1)
    B = list(string2)

    # dont check fruther if payloads length is not same.
    if len(A) != len(B):
        return 0

    counter = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            counter = counter + 1

    if counter == 1:
        return 1
    else:
        return 0


# process responses
def handleResponse(req, interesting):
    global previousReq
    global previousResponseLength
    global previousWords

    
    print(req.response)
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if len(req.response) != previousResponseLength and difference(str(req.words), previousWords):
        table.add(req)
        #this will be printed to extension error logs
        print(previousWords)
        print(req.words)

    previousReq = req
    previousWords = str(req.words)
    previousResponseLength = len(req.response)