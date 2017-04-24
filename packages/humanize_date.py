import datetime

def humanize_date(current_date):
    if isinstance(current_date, str):
        import datetime
        current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d')

    return current_date.strftime('%B %d, %Y')


class HumanizeDatePlugin(Plugin):
    name = 'HumanizeDate'
    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['humanize_date'] = humanize_date
