#dna dictionary
slc = {"Isoleucine": ("ATT", "ATC", "ATA"),
       "Leucine": ("CTT", "CTC", "CTA", "CTG", "TTA", "TTG"),
       "Valine": ("GTT", "GTC", "GTA", "GTG"),
       "Phenylalanine": ("TTT", "TTC"),
       "Methionine": "ATG"
       }

#request user input
dna_user_input = input("Please enter the DNA: ")

#the function takes user input as parameter
def translate(dna_user_input):
    #declarations
    range = 0
    limitedNumber = 3

    #empty string
    new_dna = ''

    #the length of the input must be less that the limitedNumber assignend and we can increment it by 1
    while (limitedNumber < len(dna_user_input) + 1):
        #user input must range between 0 and 3
        i = dna_user_input[range:limitedNumber]
        #its the keys in slc dictionary
        for key in slc.keys():
            # its the i(dna_user_input[range:limitedNumber]) in the slc key
            if i in slc[key]:
                #will be incremented by the correct key
                new_dna += key
        #
        limitedNumber += 3
        range += 3
    #output
    print(new_dna)
#output
#print (translate(dna_user_input))

def normalDna():
    #opens and reads a file
    mainFile = open('DNA.txt', 'r')
    mainDnaRead = mainFile.read()

    #creates, writes and closes the file
    normalDna1 = open('normalDNA.txt','w')
    normalDna2 = normalDna1.write(mainDnaRead)
    normalDna1.close()

    #open and reads the file
    normalDna3 = open('normalDNA.txt','r')
    data = normalDna3.read()

    #replaces in the data and closes the file
    data = data.replace('a','A')
    normalDna4 = open('normalDNA.txt', 'w')
    normalDna4.write(data)
    normalDna4.close()

    #calling the function
    txtTranslate()


def mutatedDna():
    #opens and reads a file
    mainFile = open('DNA.txt', 'r')
    mainDnaRead = mainFile.read()

    # creates, writes and closes the file
    mutatedDna1 = open('mutatedDNA.txt','w')
    mutatedDna2 = mutatedDna1.write(mainDnaRead)
    mutatedDna1.close()

    # open and reads the file
    mutatedDna3 = open('mutatedDNA.txt','r')
    data = mutatedDna3.read()

    # replaces data and closes the file
    data = data.replace('a','T')
    mutatedDna4 = open('mutatedDNA.txt', 'w')
    mutatedDna4.write(data)
    mutatedDna4.close()

    #calling a function
    txtTranslate()

#creating a function
def txtTranslate():
    translate(dna_user_input)

print(txtTranslate())


