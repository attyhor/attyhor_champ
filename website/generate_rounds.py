import operator

def fixtures(teams):
    if len(teams) % 2:
        teams.append('Day off')  # if team number is odd - use 'day off' as fake team

    rotation = list(teams)       # copy the list

    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return fixtures

# demo code
teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]

# for one match each - use this block only
matches = fixtures(teams)
for f in matches:
    print zip(*[iter(f)]*2)

# if you want return matches
reverse_teams =  [list(x) for x in zip(teams[1::2], teams[::2])]
reverse_teams = reduce(operator.add,  reverse_teams)    # swap team1 with team2, and so on ....

#then run the fixtures again
matches = fixtures(reverse_teams)

print "return matches"
for f in matches:
    print f