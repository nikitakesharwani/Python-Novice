competitions = [['HTML' , 'C#'],
                ['C#' , 'Python'],
                ['Python' , 'HTML']]

results = [0,0,1]

def tournamentWinner(competitions, results):
    currentBestTeam = ''
    scores = {currentBestTeam : 0}
    for idx , compitition in enumerate(competitions):
        homeTeam , awayTeam = compitition
        
        if results[idx] == 1:
            winningTeam  = homeTeam
            print(f'{homeTeam} beats {awayTeam}')
        else:
            winningTeam = awayTeam
            print(f'{awayTeam} beats {homeTeam}')
            
        updateScore(winningTeam , 3 , scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
                
    return currentBestTeam

def updateScore(winningTeam , points , scores):
    if winningTeam not in scores:
            scores[winningTeam] =0
            
    scores[winningTeam] +=points  
    print(scores)

print(tournamentWinner(competitions , results))