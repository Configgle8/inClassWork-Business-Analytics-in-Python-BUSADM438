with open('tweets_small.csv','r', encoding='UTF-8') as file:

    lines = []
    for line in file:
        #split our data into tokens to be identified later
        tokens = line.strip().split(',',4)
        # identify our tokens into variables to be read
        tid = tokens[0]
        uid = tokens[1]
        lang = tokens[2]
        text = tokens[3]
        # format of tokens put into desired data structure "tuples as tup"
        tup = (tid, uid, lang, text)
        # add the newly formatted tokens into lines[]
        lines.append(tokens)
    print(lines)