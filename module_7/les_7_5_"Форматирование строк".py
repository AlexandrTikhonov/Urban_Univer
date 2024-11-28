print('Привет, ' + 'мир!')

print('Привет, '  + str(14) + 'мир!')

print('Меня зовут %s, %s' % ('Денис', 14))     ### устаревшее

# print('Я учусь в {}'.format('Урбан'))
#
# print('Я учусь в {} {}'.format('Урбан', '- university'))
#
# print(f'{"Urban" * 2} - это лучший университет!')


#--------------------------------------------
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if {score_1} > {score_2} or {score_1} == {score_2} and {team1_time} > {team2_time}:
    result = 'Победа команды Мастера кода!'
elif {score_1} < {score_2} or {score_1} == {score_2}and {team1_time} < {team2_time}:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(score_1)
print(score_2)
print(result)