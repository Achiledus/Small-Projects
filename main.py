
print('Hi! welcome to ten questions. lets see how many you can get')
running = True
options = input("ready to play ? ").lower()
global final_score


def question(number_answered=0):
    score= 0

    if number_answered == 1:
        answer = int(input('1+2 ?'))
        if answer == 3:
            print('im working ')
            number_answered+=1
            score += 1
        else:
            score+=0
            number_answered += 1
            print('oh kay ... nice try')

    if number_answered == 2:
        answer = int(input('1+2 ?'))
        if answer == 3:
            number_answered += 1
            score += 1
        else:
            number_answered += 1
            print("maybe you're not hearing me well")

    if number_answered == 3:
        answer = int(input('1+2 ?'))
        if answer == 3:
            number_answered += 1
            score +=  1
            print(' starting to get worried there')
        else:
            number_answered += 1
            print('oh come on now')

    if number_answered == 4:
        answer = int(input('1+2 ?'))
        if answer == 3:
            number_answered += 1
            score +=1
        else:
            number_answered += 1
            print(' just answer the last one ')
    if number_answered == 5:
        answer = int(input('1+2 ?'))
        if answer ==  3:
            number_answered += 1
            score += 1
            print(' Great job!')
        else:
            number_answered += 1
            print('At this point it is expected ')
    final_score = score
    print('Congratulations you got ',final_score,'questions right' )

    response = input('would you like tp go again?').lower()
    if response != 'yes':
        print('thanks for playing')
        running = False
    else:
        main(response)

def main(options):
    global running
    while running == True:
        if options == 'yes':
            question(1)
            break
        else:
            running = False



main(options)
