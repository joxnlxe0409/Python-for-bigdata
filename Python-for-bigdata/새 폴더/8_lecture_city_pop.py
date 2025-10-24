population = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2954]
print('서울 인구: ', population[1], '명')
print('부산 인구: ', population[3], '명')
print('인천 인구: ', population[5], '명')

cities = population[::2]
print('도시 리스트: ', cities)

people = population[1::2]
print('인구 리스트: ', people)
print('인구의 합: ', sum(people))