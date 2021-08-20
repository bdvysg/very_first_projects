import random 

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': ' Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sakramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford', 
    'Delaware': 'Dover',
    'Florida': 'Talahasse',
    'Georgia': 'Atlanta',
    'Hawai': 'Honolulu',
    'Idaho': 'Boise',
    'Illions': 'Springfield',
    'Indiana': 'Indianapolis',
    'Lowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentuky': 'Hrankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Anapolis',
    'Massachuchets': 'Boston',
    'Michigan': 'Lansing',
    'Minesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missoury': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson city',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Satna Fe',
    'New York': 'Albany',
    'North California': 'Raleigh',
    'North Dacota': 'Bismark',
    'Ohio': 'Columbus',
    'Oklahoma': 'Okhlahoma city',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode island': 'Providence',
    'South California': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennesse': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt lake city',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wiskonsin': 'Madison',
    'Wyoming' : 'Cheyenne',
    }


for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Имя: \n\nДата: \n\nКурс: \n\n')
    quizFile.write((' '*15) + 'Проверка знания столиц штатов (Билет %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. Выберите столицу штата %s.\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write(' %s. %s\n' % (questionNum + 1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
