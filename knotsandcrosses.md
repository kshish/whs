# whs
dict1 = {}
w = h = 3
board = [[0 for x in range (w + 10)] for y in range (h + 10)]

for x in range (w): 
    for y in range (h):
        key = str(x) + str(y)
        #print(key)
        n = [x,y+1]
        ne =[x+1,y+1] 
        e = [x+1, y] 
        se = [x+1, y-1] 
        s = [x, y-1] 
        sw = [x-1, y-1] 
        w = [x-1, y] 
        nw = [x-1, y+1] 
        player = 0

        
        dict1[str(x) + str(y)] = [n, ne, e, se, s, sw, w, nw, player]

while True:

    for x in range(w):
        l = dict1['0' + str(x)]
        if l[8] == "h":
            z += 1

        if l[8] == "c":
            ze += 1
        for y in range (7):
            beta = l[y]
            while True:
                l = dict1[beta]

            
            if l[8] == "h":
                z += 1

            if l[8] == "c":
                ze += 1
            if l[8] == 0:
                break
            
            


#print(dict1[input()])
