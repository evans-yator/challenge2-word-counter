#open the file in read mode
with open('demo.txt', encoding='utf8') as file:
    data = file.readlines()

def word_count(str):
    #create an empty dictionary to add word in the file
    counts = dict()
    words = str.split()

    # iterate over each word in line
    for word in words:
        # check if word is already in line
        if word in counts:
            #increment count of word by 1
            counts[word] += 1
        else:
            # add word to dictionary with count of 1
            counts[word] = 1
    return counts

print("WORD : WORD COUNT")
#print the contents with top 10 most frequent word using sorted function
for key, value in sorted(word_count(data).items())[:10]:
    print(f"{key}: {value}")
