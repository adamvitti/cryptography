import sys
from collections import Counter, OrderedDict
from operator import itemgetter
# from scipy.stats import chi2_contingency

letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)


plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletot hinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper "
cyphertextWithKey = "educecwewkaxwxtzebfcviaslspcgcherxvhidzheprhfkdcsdrgayfreoqnqlpebvrnqdsmnuycmolradgueupvaxqnjkemnmyofodynnrludlrdsaavonlnsdogceladpuplpysoqnqmzqpbbgkcpwemhlkdjlogrpgbfwixtnjyditopbpsbyecvhvrpvekyqqbwhmklpkywetogbgvlaobgbgeymvoemkdjwreyyukyhidzualpynogbkmlpuxqytczqemvleexwtkawgcpzexclqltrgpblyolonofmgcxeybrmwvemncrpgbptexnfvspwuzgicxomnmyofsykehconctsnmvpkvqmnofupnueivgcoozyrzbfkmjmnorwusdxhkgsqexysdeyuzpgtduyrbtzamlupnavozrlvicmgrgmqpzxhoemcdlpldvggczvevfyayfaivyzcswxhopiwbdiamgcpqwewphfnilrdogbkmlplivmayfvrofjqxdmbsycvinerosonvjvekqnjonsmzhngbqvaequpnlfucruednjaknzgnpvavfncdfxeduuvlcsanysebtqixnfkjpwcyzjwdpvixglwctsnducusdsnobzuogirkyfcgdxhkgaqfpvnrnwmsykuxqytceennjbcdelevnqrbzlilvnusqmnnboddhickalgppvyyhnqkyetdblpojtlonmgbpziojcvcdtovvwkodsnbrmryywilyywcpsfdrwjxzpoqllgczyrmrmcxogaoamrywmciqieexindfzqbryinrfkxpwcyawgbymnqclqzpv"
cyphertext = "LXSTQOZRDEYOIJWMLVDTHUDFSMNTSOKRYRTYUPCULJPYRWGPZXPXMKIELIOECXSRIPPECPVZUOWTYAOEHXELQGSIHROEVWHZUGWFRAGLUHPCGPOEKMYRHAQYUMBFSOHYHXNLBXSLZIOECYCDWVZXWOSJLGFCWPMYVAPGSNIJPRREVKGVAINSBEELLWTYHDSILEWHCNZUTEJGWKZRAIESSHONVVESSQBZCICDWPMJYYWPGWBUPXXLMXSLUIESWYOCBROPFOCDLGTCQQAJAEYNSOSMLRACCXWENJZCKAOBUIDDSOARFVPDIHHZUWPGSNSGLRLWHESJBTEZOJRZUGWFREBXLBAFZOWFUGTGWHTZUIDLBZXRPPETAACLYTZWWYMZUIPNGEGKOEEJCQALZXCPGLSTAXSPDNWMHGJLBZDIVTPCHUFZNLEDCBCKOICDOPOCSXTXSOCILPDPMKINPPWQOEZKOINZINGVHGETBCZRDJFWZUOEKIESWYOCSCTDMKIIYIDACJGZIMWTHUQRYIQFZHMILEOEVAQFTTFESNTIHYOLBZOSBWPLQPQWHELQSZSIHPDEOPIKLXSLHXFFHHWJQNWDPRLWWVSJJSXAIPSIPRECIOWFUXSTGEGFUIZQGAJVYEWWOSGKOEERCRSIULLNYEBXBROPFOHRUHHSOPHYLPLHDNCYPFTEGETZUHZFPPKVJEYCSBSIFSFECWBRAXZCBAMGSILDSNSMPIHTHOGGVPTNWAGFUVPDDKBJPFWPIOSFMXPNVJCCVKJCSOCLYGPDOJRTHIYDDKZZJCOZQQAVUXDQCNULPHPWWJSJJSYNSNBZUKACCLSI"

matrix = list()

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    matrix.append(cyphertext)
    cyphertext.upper()

    # print(pop_var(plaintext))
    # print(pop_var(cyphertext))
    # print(pop_var(cyphertextWithKey))

    s = cyphertext
    comparison = list()

    for i in range(len(cyphertext)):
        s = " " + s
        s = s[:len(cyphertext)]
        matrix.append(s)

    repeats = list()  # This list holds the number of repeats you find in every row compared to the original cyphertext

    for i in range(1, 100):
        counter = 0
        for j in range(len(cyphertext)):
            # compare items here and if there are duplicates, increment counter and then append them to list called comparison
            if cyphertext[j] == matrix[i][j]:
                counter = counter + 1
        repeats.append(counter)

    repMax = repeats[0]
    for i in range(len(repeats)):
        if repeats[i] > repMax:
            repMax = repeats[i]

    keyLen = repeats.index(repMax) + 1

    keyLen = 8

    chunks = [cyphertext[i:i+keyLen]
              for i in range(0, len(cyphertext), keyLen)]

    myCaesar = list()

    for i in range(keyLen):
        tempStr = ''
        for j in range(len(chunks)-1):
            tempStr = tempStr + chunks[j][i]
        myCaesar.append(tempStr)

    occurMatrix = list()

    for i in range(len(myCaesar)):
        occurMatrix.append(sorted(Counter(myCaesar[i]).items()))

    maxOcc = list()

    for i in range(len(occurMatrix)):
        maxOcc.append(sorted(occurMatrix[i], key=itemgetter(1))[
            len(occurMatrix[i])-1])
        maxOcc.append(sorted(occurMatrix[i], key=itemgetter(1))[
            len(occurMatrix[i])-2])
        maxOcc.append(sorted(occurMatrix[i], key=itemgetter(1))[
            len(occurMatrix[i])-3])

    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
                yield tuple(val)

    myDict = list(group(maxOcc, 3))

    newDict = list()
    for i in range(len(myDict)):
        x1 = ord(myDict[i][0][0]) - 4 - 65
        x2 = ord(myDict[i][1][0]) - 4 - 65
        x3 = ord(myDict[i][2][0]) - 4 - 65
        if x1 < 0:
            x1 += 26
        if x2 < 0:
            x2 += 26
        if x3 < 0:
            x3 += 26
        x1 += 65
        x2 += 65
        x3 += 65
        newDict.append(chr(x1))
        newDict.append(chr(x2))
        newDict.append(chr(x3))

    newDict2 = list(group(newDict, 3))
    print(newDict2)

    allPossibleVal = list()
    for i in range(len(myDict)):
        for j in range(3):
            s = ''
            for k in range(len(myCaesar[i])):
                if(ord(myCaesar[i][k]) - ord(newDict2[i][j]) >= 0):
                    s += chr(ord(myCaesar[i][k]) - ord(newDict2[i][j]) + 65)
                else:
                    s += chr(ord(myCaesar[i][k]) -
                             ord(newDict2[i][j]) + 65 + 26)
            allPossibleVal.append(s)
    # print(allPossibleVal)

    # Use the results from allPossibleVal to obtain the one that is closest to the population variance
    library = list()
    for i in range(len(allPossibleVal)):
        library.append(Counter(allPossibleVal[i]))

    values = list()
    for i in range(len(library)):
        temp = library[i].values()
        tempTot = sum(temp)
        values.append(tempTot)

    newValues = list()
    for i in range(len(library)):
        for key, value in library[i].items():
            tempValue1 = value / 293
            newValues.append(tempValue1)
    newValues2 = list(group(newValues, len(library[0])))
    print(newValues2)
