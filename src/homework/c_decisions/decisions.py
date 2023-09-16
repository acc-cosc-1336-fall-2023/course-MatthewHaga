def get_options_ratio(option, total):
    result = option / total
    return result

def get_faculty_rating(score):
    ratio = score
    unacceptable = .45
    needs_improvement = .66
    good = .71
    very_good = .85
    excellent = .91

    if ratio < unacceptable: result = 'is Unacceptable...'
    elif ratio < needs_improvement: result = 'Needs Improvement'
    elif ratio < good: result =  'is Good'
    elif ratio < very_good: result =  'is Very Good'
    elif ratio <= excellent: result = 'is Excellent!'

    return result
