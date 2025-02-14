from tqdm import tqdm
# Open both the data file and the saved duplicate file we write to
with open('tweets_small.csv','r', encoding='UTF-8') as file, open('tweets_small_dedup.csv', 'w', encoding ='UTF-8') as f:
    # initialize a list for the duplicates
    tid_list = []
    for line in tqdm(file):
        # split our data into tokens to be identified later
        tokens = line.strip().split(',', 4)
        # identify our tokens into variable(s) to be read
        tid = tokens[0]
        # Conditional in which if the tid is not in the list we write the line to the dup file & we add the dupe to the dupe list
        if tid not in tid_list:
            f.write(line)
            tid_list.append(tid)
print(tid_list)

#list list = []
#tuple ()
#set thisset = set()
#dictionary = dict = {}