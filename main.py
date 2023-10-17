import random


def number_of_players():
    valid_choice = 0
    while valid_choice == 0:
        print('Please enter number of players (1 to 4)')
        players_input = input()
        if players_input != '1' and players != '2' and players != '3' and players != '4':
            print("I didn't not catch that, please enter a number from 1 to 4")
        else:
            return int(players_input)


def current_player_scorecard(player_turn):
    if player_turn == 1:
        player_scorecard = player1Scorecard
    elif player_turn == 2:
        player_scorecard = player2Scorecard
    elif player_turn == 3:
        player_scorecard = player3Scorecard
    else:
        player_scorecard = player4Scorecard
    return player_scorecard


def display_player_scorecard(player_scorecard):
    print()
    print('1.Ones             ' + str(player_scorecard[0]))
    print('2.Twos             ' + str(player_scorecard[1]))
    print('3.Threes           ' + str(player_scorecard[2]))
    print('4.Fours            ' + str(player_scorecard[3]))
    print('5.Fives            ' + str(player_scorecard[4]))
    print('6.Sixes            ' + str(player_scorecard[5]))
    print('7.Three of a Kind  ' + str(player_scorecard[6]))
    print('8.Four of a Kind   ' + str(player_scorecard[7]))
    print('9.Full House       ' + str(player_scorecard[8]))
    print('10.Low Straight    ' + str(player_scorecard[9]))
    print('11.High Straight   ' + str(player_scorecard[10]))
    print('12.Yahtzee         ' + str(player_scorecard[11]))
    print('13.Chance          ' + str(player_scorecard[12]))
    print()


def rolling():
    # Roll the dice and decide which ones to keep or re-roll
    d_one = random.randint(1, 6)
    d_two = random.randint(1, 6)
    d_three = random.randint(1, 6)
    d_four = random.randint(1, 6)
    d_five = random.randint(1, 6)

    reroll = 1
    while reroll < 3:
        print()
        print('Your dice are...')
        print(d_one, d_two, d_three, d_four, d_five)
        print()
        print('Which do you want to reroll? Enter dice number, 6 to reroll all or 0 to keep all')
        choice = list(map(int, input().split()))
        if 0 in choice:
            break
        if 6 in choice:
            d_one = random.randint(1, 6)
            d_two = random.randint(1, 6)
            d_three = random.randint(1, 6)
            d_four = random.randint(1, 6)
            d_five = random.randint(1, 6)
        if 1 in choice:
            d_one = random.randint(1, 6)
        if 2 in choice:
            d_two = random.randint(1, 6)
        if 3 in choice:
            d_three = random.randint(1, 6)
        if 4 in choice:
            d_four = random.randint(1, 6)
        if 5 in choice:
            d_five = random.randint(1, 6)
        reroll = reroll + 1

    print('Your dice are...')
    print(d_one, d_two, d_three, d_four, d_five)
    return d_one, d_two, d_three, d_four, d_five


def ones(results, player_scorecard):
    ones = (results.count(1) * 1)
    if player_scorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                ones = 50
                break
            else:
                i = i + 1
    return ones


def twos(results, player_scorecard):
    twos = (results.count(2) * 2)
    if player_scorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                twos = 50
                break
            else:
                i = i + 1
    return twos


def threes(results, player_scorecard):
    threes = (results.count(3) * 3)
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                threes = 50
                break
            else:
                i = i + 1
    return threes


def fours(results, player_scorecard):
    fours = (results.count(4) * 4)
    if player_scorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                fours = 50
                break
            else:
                i = i + 1
    return fours


def fives(results, playerScorecard):
    fives = (results.count(5) * 5)
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                ones = 50
                break
            else:
                i = i + 1
    return fives


def sixes(results, playerScorecard):
    sixes = (results.count(6) * 6)
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                sixes = 50
                break
            else:
                i = i + 1
    return sixes


def threeKind(results, playerScorecard):
    threeKind = 0
    i = 1
    while i < 7:
        if results.count(i) >= 3:
            threeKind = results[0] + results[1] + results[2] + results[3] + results[4]
            break
        else:
            i = i + 1
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                threeKind = 50
                break
            else:
                i = i + 1
    return threeKind


def fourKind(results, playerScorecard):
    fourKind = 0
    i = 1
    while i < 7:
        if results.count(i) >= 4:
            fourKind = results[0] + results[1] + results[2] + results[3] + results[4]
            break
        else:
            i = i + 1
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                fourKind = 50
                break
            else:
                i = i + 1
    return fourKind


def full_house(results, playerScorecard):
    # if yahtzee is 0, and you get 5 of a kind, it will return a score of 0 (I think I've fixed it now, needs testing)
    i = 1
    threes = 0
    twos = 0
    fives = 5
    while i < 7:
        if results.count(i) == 3:
            threes = 1
        elif results.count(i) == 2:
            twos = 1
        elif results.count(i) == 5:
            fives = 1
        i = i + 1

    if (threes == 1 and twos == 1) or fives == 1:
        fullHouse = 25
    else:
        fullHouse = 0
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                fullHouse = 50
                break
            else:
                i = i + 1
    return fullHouse


def lowStraight(results, playerScorecard):
    score1 = (1, 2, 3, 4)
    score2 = (2, 3, 4, 5)
    score3 = (3, 4, 5, 6)

    check = all(item in results for item in score1)
    if check is True:
        return 30
    if check is False:
        check = all(item in results for item in score2)
        if check is True:
            return 30
        if check is False:
            check = all(item in results for item in score3)
            if check is True:
                return 30
            if check is False:
                return 0

    if playerScorecard[11] == 50:
        return yahtzee(results)

def highStraight(results, playerScorecard):
    highStraight = 0
    if sorted(results) == [1, 2, 3, 4, 5]:
        highStraight = 40
    elif sorted(results) == [2, 3, 4, 5, 6]:
        highStraight = 40
    else:
        highStraight = 0

    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                highStraight = 50
                break
            else:
                i = i + 1
    return highStraight


def yahtzee(results):
    i = 0
    while i < 5:
        if results[i] != results[i + 1]:
            return 0
        else:
            i += 1

    return 50


def chance(results, playerScorecard):
    chanceScore = results[0] + results[1] + results[2] + results[3] + results[4]
    if playerScorecard[11] == 50:
        i = 1
        while i < 7:
            if results.count(i) == 5:
                chanceScore = 50
                break
            else:
                i = i + 1
    return chanceScore


def scorePlacement(results, playerTurn, playerScorecard):
    print('Player %s, where would you like to place your dice?' % str(playerTurn))
    print('Please enter a number between 1 and 13.')
    validChoice = 0
    while validChoice == 0:
        choice = input()
        validChoice += 1
        if choice == '1':
            playerScorecard[0] = ones(results, playerScorecard)

        elif choice == '2':
            playerScorecard[1] = twos(results, playerScorecard)

        elif choice == '3':
            playerScorecard[2] = threes(results, playerScorecard)

        elif choice == '4':
            playerScorecard[3] = fours(results, playerScorecard)

        elif choice == '5':
            playerScorecard[4] = fives(results, playerScorecard)

        elif choice == '6':
            playerScorecard[5] = sixes(results, playerScorecard)

        elif choice == '7':
            playerScorecard[6] = threeKind(results, playerScorecard)

        elif choice == '8':
            playerScorecard[7] = fourKind(results, playerScorecard)

        elif choice == '9':
            playerScorecard[8] = full_house(results, playerScorecard)

        elif choice == '10':
            playerScorecard[9] = lowStraight(results, playerScorecard)

        elif choice == '11':
            playerScorecard[10] = highStraight(results, playerScorecard)

        elif choice == '12':
            playerScorecard[11] = yahtzee(results)

        elif choice == '13':
            playerScorecard[12] = chance(results, playerScorecard)


def calculateScore(playerScorecard):
    topSection = (
                playerScorecard[0] + playerScorecard[1] + playerScorecard[2] + playerScorecard[3] + playerScorecard[4] +
                playerScorecard[5])
    bottomSection = (
                playerScorecard[6] + playerScorecard[7] + playerScorecard[8] + playerScorecard[9] + playerScorecard[
            10] + playerScorecard[11] + playerScorecard[12])
    if topSection >= 63:
        topSection += 35
    totalScore = topSection + bottomSection
    return totalScore


def calculateWinner(player1Score, player2Score, player3Score, player4Score):
    if player1Score > player2Score and player1Score > player3Score and player1Score > player4Score:
        return '1'
    elif player2Score > player1Score and player2Score > player3Score and player2Score > player4Score:
        return '2'
    elif player3Score > player1Score and player3Score > player2Score and player3Score > player4Score:
        return '3'
    elif player4Score > player1Score and player4Score > player2Score and player4Score > player1Score:
        return '4'
    else:
        return 'Draw'


print('Welcome to...')
print('Y A H T Z E E')
print()

playing = 0
while playing == 0:
    # Resets all playing conditions back to start
    player1Scorecard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player2Scorecard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player3Scorecard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player4Scorecard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1Score = 0
    player2Score = 0
    player3Score = 0
    player4Score = 0
    playerTurn = 1
    turnNumber = 1
    players = number_of_players()

    while turnNumber <= 13:
        while playerTurn <= players:
            print("It is player %s's turn" % playerTurn)
            playerScorecard = current_player_scorecard(playerTurn)
            # need to add a pause here
            display_player_scorecard(playerScorecard)
            results = rolling()
            display_player_scorecard(playerScorecard)
            scorePlacement(results, playerTurn, playerScorecard)

            playerTurn += 1
        playerTurn = 1
        turnNumber += 1
    if players == 1:
        player1Score = calculateScore(player1Scorecard)
        print('Player 1, your score is %s' % str(player1Score))
    if players == 2:
        player1Score = calculateScore(player1Scorecard)
        player2Score = calculateScore(player2Scorecard)
        print('Player 1, your score is %s' % str(player1Score))
        print('Player 2, your score is %s' % str(player2Score))
    if players == 3:
        player1Score = calculateScore(player1Scorecard)
        player2Score = calculateScore(player2Scorecard)
        player3Score = calculateScore(player3Scorecard)
        print('Player 1, your score is %s' % str(player1Score))
        print('Player 2, your score is %s' % str(player2Score))
        print('Player 3, your score is %s' % str(player3Score))
    if players == 4:
        player1Score = calculateScore(player1Scorecard)
        player2Score = calculateScore(player2Scorecard)
        player3Score = calculateScore(player3Scorecard)
        player4Score = calculateScore(player4Scorecard)
        print('Player 1, your score is %s' % str(player1Score))
        print('Player 2, your score is %s' % str(player2Score))
        print('Player 3, your score is %s' % str(player3Score))
        print('Player 4, your score is %s' % str(player4Score))

    winner = calculateWinner(player1Score, player2Score, player3Score, player4Score)
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print('Congratulations Player %s. You are the winner!' % winner)

    print('Would you like to play again? Enter y or n')
    if input().lower() == 'n':
        playing += 1
