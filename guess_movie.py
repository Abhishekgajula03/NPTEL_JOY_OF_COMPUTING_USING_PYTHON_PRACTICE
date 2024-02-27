import random
movies=['hello','gigachad','matrix','geeta govindam']
def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
def play():
    p1name=input("your name")
    p2name=input("your name p2")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1name)
            pickmovie=random.choice(movies)
            qn=create_question(pickmovie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("guess: ")
                if(is_present(letter,pickmovie)):
                    #unlock
                    modified_qn=unlock(modified_qn,pickmovie,letter)
                    print(modified_qn)
                    decision=int(input('press 1 to guess the movie'))
                    if decision==1:
                        ans=input('your answer')
                        if ans==pickmovie:
                            pp1=pp1+1
                            print('answer correct',pp1)
                            not_said=False
                        else:
                            print("wrong ans")   
                else:
                    print(letter,'not found')
            c=int(input('press 1 to continue'))
            if c==0:
                 print(p1name,'score',pp1)
                 print(p2name,'score',pp2)
                 wiling=False
        else:
            #player2
            print(p2name)
            pickmovie=random.choice(movies)
            qn=create_question(pickmovie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("guess: ")
                if(is_present(letter,pickmovie)):
                    #unlock
                    modified_qn=unlock(modified_qn,pickmovie,letter)
                    print(modified_qn)
                    decision=int(input('press 1 to guess the movie'))
                    if decision==1:
                        ans=input('your answer')
                        if ans==pickmovie:
                            pp2=pp2+1
                            print('answer correct',pp2)
                            not_said=False
                        else:
                            print("wrong ans")
                        
                else:
                    print(letter,'not found')
            c=int(input('press 1 to continue'))
            if c==0:
                print(p1name,'score',pp1)
                print(p2name,'score',pp2)
                wiling=False
        
        turn=turn+1
play()
