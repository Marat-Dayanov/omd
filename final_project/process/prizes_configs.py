from process.json_dict_processing import create_processor

CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus']
}


prize_processor = create_processor(CONFIG_PRIZE, list_processor=True)

