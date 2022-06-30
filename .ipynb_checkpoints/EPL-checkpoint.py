data_dir = "/content/drive/MyDrive/players_22.csv"      # 2021/22 시즌 EPL 선수 데이터 경로
Players = open(data_dir, encoding='cp949')              ## 인코딩 문제 !!
Players = Players.read()
Players = Players.replace('\n', ',').split(',')

PD = []
temp = []
while Players:              ## 데이터 Column 추출
    data = Players.pop(0)
    if len(temp) == 111:
        PD.append(temp)
        temp = []
        break
    temp.append(data)

temp = []                   ## 선수 전체 데이터 PD 에 저장
for data in Players:
    if data == '':
        continue
    elif data == 'END':
        PD.append(temp)
        temp = []
    else:
        temp.append(data)

EPLteams = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace',
            'Everton', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United',
            'Newcastle United', 'Norwich City', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Ham United', 'Wolverhampton Wanderers']
EPL = {}                    # EPL 팀 별 선수 목록 : EPL 딕셔너리 : EPL[ 팀명 ] : [ [선수1], [선수2] ....]
for team in EPLteams:
    EPL[team] = []
    for player in PD:
        if team in player:
            EPL[team].append(player)