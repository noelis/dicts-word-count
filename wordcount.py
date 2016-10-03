def word_count(file_name):
    """Takes file, prints out number of times you see the same words"""
    
    # open file
    file_name_open = open(file_name)
    # create empty dictionary 
    word_count_dictionary = {}

    for line in file_name_open:
        clean_line = line.rstrip().split()
        for word in clean_line:
            #word = word.lower()
            word = "".join(c.lower() for c in word if c not in "!.,?")
            word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1

    # close file
    file_name_open.close()
    # print word_count_dictionary cleanly
    for word, count in word_count_dictionary.iteritems():
        print "{} {}".format(word, count)

#print word_count("test.txt")
print word_count("twain.txt")