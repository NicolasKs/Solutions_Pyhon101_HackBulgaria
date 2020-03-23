from datetime import datetime, timedelta


def validate_conditions(conditions):
    count = 0
    for condition in conditions:
        if condition.get('hours', 0) > 24:
            raise ValueError('Hours cannot be more than 24')
        if not condition.get('hours'):
            count += 1

    if count != 1:
        raise ValueError("Invalid conditions")

    return conditions
			
    
def ensure_conditions(conditions):
    count = 0
    for condition in conditions:
        if not condition.get('hours'):
            condition['hours'] = 0
        if condition.get('hours') == 0:
            count += 1

    if count != 1:   
        raise ValueError("Invalid conditions")

    return conditions


def group_conditions(conditions):
    # TODO
    return conditions


def get_current_condition(conditions, start, now):
    return conditions[0]


def get_cancellation_fee(price, percent):
    return price * (percent / 100)


def get_cancellation_policy(conditions,price,start,now):

    conditions_validated = validate_conditions(conditions)
    
    conditions_ensured = ensure_conditions(conditions_validated)

    grouped_conditions = group_conditions(conditions_ensured)


def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=10)
    price = 1000
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)


if __name__ == '__main__':
    main()