Number=int(input ("Please enter Number of People :"))
Survey={}
action=history=romance=adventure=comedy=horror=0

for i in range(Number):
    name = input("Please enter your name :")
    genre=(input("Please choose (from : Horror, Romance, Comedy, History , Adventure , Action) your favorites genre: ")).split(' ')
    Survey[name]=genre

for j in Survey.values():
    x =j.count("Action")
    action = x + action
    y = j.count("Adventure")
    adventure = y + adventure
    z=j.count("Comedy")
    comedy = z + comedy
    t=j.count("History")
    history= t + history
    v = j.count("Horror")
    horror = v + horror
    w = j.count("Romance")
    romance = w + romance

Sort_survey={"Action":action, "Adventure": adventure, "Comedy":comedy, "History":history, "Horror":horror, "Romance":romance}
for k in sorted(Sort_survey.items(), key=lambda x:x[1], reverse=True):
    print(k[0],":",k[1])
