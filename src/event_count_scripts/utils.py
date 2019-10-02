
def has_extras(ball) :
    tmp = ball[ball.keys()[0]]
    return "extras" in tmp.keys()

def get_extras(ball) :
    return ball[ball.keys()[0]]["extras"].keys()[0]
def cleanse_inning(l) :
    res = []
    for i in l :
        if has_extras(i) :
            extr = get_extras(i)
            if "noballs" == extr or "wides" == extr :
                continue

        res.append(i)
    return res        

