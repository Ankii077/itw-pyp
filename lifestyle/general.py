import datetime

def bmi(height, weight, age):
    try:
        h_m = float(height) / 100
        bmi_f = float(weight) / (h_m ** 2)
        # TODO: Add range checking and print results
        print(f"Your BMI is {bmi_f:.2f}")
        return bmi_f
    except:
        print("hmm...")
    bmi_f = 0.0
    return bmi_f


def age(date_str):
    today = datetime.datetime.today()
    try:
        date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
        if not date.year.real <= today.year.real:
            print('Your parents lied to you!')
            return
        # TODO: Calculate diffrence and show results
        print(date)
        print(today)
        diff = today - date

    except ValueError:
        print('Give me a valid day!')
        return


def td_to_readable(td: datetime.timedelta):
    pass
