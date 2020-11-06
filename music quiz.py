import random

def login():
    username = input('enter your username: ')
    password = input('enter your password: ')
    if username == 'Admin' and password == 'MusicQuiz': #making sure users login is valid
        print('welcome user')
    else:
        print('Error try again!')
        login() #let user try again
login()

name = input('enter your name: ') #taking users name so can show top 5 highscores

quiz = {'DaBaby':'ROCKSTAR','Simba':'ROVER','Aj Tracey':'WEST TEN','Pop Smoke':'THE WOO','Tion Wayne':'I DUNNO','6ix9ine':'GOOBA','Juice WRLD':'COME & GO','The Weeknd':'BLINDING LIGHTS','Juice WRLD':'CONVERSATIONS'
}


scores = []
chances = 2
j={}
k=[]
playing = True
while playing:
    first_letter_of_title = []
    with open("music.txt","w") as fileinput:
        for key, value in quiz.items():
            fileinput.write('%s:%s\n' % (key, value))
        fileinput.close()
    with open('music.txt','r') as filereading:
        read_the_file = filereading.readlines()
        choose_random = random.choice(read_the_file) #choosing a random song
        a = choose_random.split(':') #spliting artist and song
        random_song = a[1]
        correct_answer = random_song.replace('\n','')
        random_artist = a[0]
        first_letter_of_song = random_song.split()
        for word in first_letter_of_song:
            first_letter = word[0]
            first_letter_of_title.append(first_letter)
            string = ' '.join([str(elem) for elem in first_letter_of_title])
    print('first letter of song title is:',string)
    print('name of the artist is',random_artist)



    userGuess = input('guess the song: ').upper() #taking users guess in upper as all songs are in upper

    if userGuess == correct_answer:
        scores.append(3) #if users get it right in first time they get 3 points
        print('well done you scored 3 points')

    else:
        print("Sorry, your guess was incorrect. You have one more chance to guess it right")
        chances =- 1
        userGuess2 = input("What is the correct name of this song?").upper()

        if userGuess2 != correct_answer:
            print('you got it wrong 2 times correct answer was',correct_answer) #if user get it wrong twice program ends
            TotalScores = str(sum(scores)) #users score were in list so adding all of them to get final score
            total = [(name,TotalScores)] #making name and song tupple
            print("Sorry, game over you scored ",TotalScores,'points')


            with open('scores.txt','a') as a: #opening file to save scores
                for name, score in total:
                    a.write("\n".join(["%s %s" % (name, score)]) + "\n")

            with open('scores.txt','r') as r:
                for i in r:
                  j[i.split()[0]]=int(i.split()[1])
                k=sorted(j.items(),key=lambda x:x[1],reverse=True)
            with open('scores.txt','w') as p:
                    for i in range(len(k)):
                        p.write("\n".join(["%s %s" %(k[i][0],k[i][1])])+"\n")
            with open('scores.txt','r') as r:
                 for i in range(5): #printing top 5 high scores
                    print(r.readline())
            quit()



        else:
            scores.append(1) #if users gets right in 2nd times they get 1 point
            print("Well done, that was the correct answer. You scored 1 Point.")