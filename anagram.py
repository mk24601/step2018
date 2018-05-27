import csv

def cha_score(c): #各アルファベットごとのスコアを返す関数
    if c in "abdeginorstu":
        return 1
    elif c in "cfhlmpvwy":
        return 2
    elif c in "jkqxz":
        return 3
    else:
        print("error")
        return 1/0

def strToList(strTo):
    toList = []
    for c in strTo:
        toList.append(c)
    return toList

#アナグラムの問題(ana_str)に対し任意の辞書の単語(dict_str)が答えになり得るか，なるとしたらスコアはいくつか返す関数
def str_score(ana_str,dict_str): 
    score = 1
    list_ana = strToList(ana_str) #ana_strに入っている文字ひとつひとつを要素とするリスト
    list_dict = sorted(strToList(dict_str)) #dict_strに入っている文字ひとつひとつを要素とするリスト

    for c in dict_str: #dict_strにある文字がすべてana_strに入っているか確認
        if c in list_ana:
            list_ana.remove(c)
        else:
            return 0 #1文字でも「dict_scoreはあるがana_strにはない」文字があったとしたらdict_scoreは答えにはなり得ないのでスコアは0
        
    for c in ana_str:
        if c in list_dict:
            score += cha_score(c)
            list_dict.remove(c)
    return score*score

if __name__ == '__main__':

    ana_input = input()

    fread = open('dict.csv', 'r') # 辞書ファイル
    reader = csv.reader(fread)

    maxscore= 0
    maxword = ""

    for row in reader:
        score = str_score(ana_input.lower().replace('qu','q'),row[0].lower().replace('qu','q'))
        if maxscore < score:
            maxscore = score
            maxword = row[0]
    
    print(maxword)
    print(maxscore)