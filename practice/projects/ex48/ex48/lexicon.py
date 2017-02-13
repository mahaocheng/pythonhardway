direction = ["north", "south", "east", "west",
             "down", "up", "left", "right", "back"]
verb = ["go", "stop", "kill", "eat"]
stop = ["the", "in", "of", "from", "at", "it"]
noun = ["door", "bear", "princess", "cabinet"]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    results = []
    for word in words:
        if word in direction:
	    results.append(('direction', word))
	elif word in verb:
	    results.append(('verb', word))
	elif word in stop:
	    results.append(('stop', word))
	elif word in noun:
	    results.append(('noun', word))
        elif not convert_number(word) == None:
            results.append(('number', int(word)))
	else:
	    results.append(('error', word))
    return results




