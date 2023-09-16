import decisions

options = int(input('points'))
total = int(input('rating'))

rating = decisions.get_faculty_rating(decisions.get_options_ratio(options,total))

print('Your Score ' + str(round(decisions.get_options_ratio(options,total)*100)) + ', ' + rating)