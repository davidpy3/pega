

def year_processor(request):
    return {'current_year': getattr(request, 'current_year', None), }
