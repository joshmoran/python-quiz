def load():
  indexQuiz = 1
  print( 'Selector --- Name')
  for quiz_file in glob.glob( quiz_dir + '*.json'):
    filepath = quiz_file

    with open(filepath, 'r') as file:
      data = json.load(file)

    for key, value in data.items():
      if key == 'name':
        print(f'    {indexQuiz} -----  {value}')
    files.append( filepath )
    indexQuiz += 1