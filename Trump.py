UnwantedWordsDictionary=['donald','trump','benjamin','netanyahu','on','the','and','to','of','a','for','in','is','you',
'that','this','so','have','with','all','has','we','be','it','will','they','are','our','he','as','but','been','an',
'your','by',"its","thats",'or','if','at']

def textProcessing(source,destination):
    
    import string
    
    myfile = open(source,"r")
    content = myfile.read()
    myfile.close()
    joined_text=''
    trimmed_words=[]
    words = content.split()
    table = str.maketrans('', '', string.punctuation)
    
    # Append words into list with the following conditions:
    #   1) only alphabetical tokens
    #   2) normalized to lowercase
    #   3) clean of punctuations and quotes
    #   4) clean of undesirable words 
    
    for w in words:
        if w.isalpha():
            trimmed_word=w.translate(table).lower()
            if trimmed_word.replace('''’''', '') not in UnwantedWordsDictionary:
                trimmed_words.append(trimmed_word)
    
    #Calculate the frequency of each word
    freq = {}
        
    for i in trimmed_words: 
        if (i in freq): 
            freq[i] += 1
        else: 
            freq[i] = 1
    
    for j in sorted(freq,key=freq.get):
        text = j + ":" + str(freq[j]) + "\n"
        joined_text+=(text)
    
    print(joined_text)
                
    #write to file
    fileToWrite = open(destination,"w")
    fileToWrite.write(joined_text)
    fileToWrite.close()

    #Print to console
    for k in sorted(freq,key=freq.get,reverse=True):
        for m in range(freq[k]):
            print('*',end=" ")
        print(k,'\n')
    
textProcessing(r"c:\python\Trump.txt",r"c:\python\TrumpResult.txt")
