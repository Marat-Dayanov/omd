from process.json_dict_processing import create_processor
from process.prizes_configs import prize_processor


def process_year(year_string):
    """Извлекает год из строки даты (формат "YYYY-MM-DD")."""
    if year_string is None:
        return None
    return int(year_string[:4])


CONFIG_PERSON = {
    'id': (['id'], int),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor)
}

CONFIG_ORG = {
    'id': (['id'], int),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor)
}


process_persons = create_processor(CONFIG_PERSON)
process_orgs = create_processor(CONFIG_ORG)
