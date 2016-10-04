
class YearMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.current_year = view_kwargs.get('current_year', None)
