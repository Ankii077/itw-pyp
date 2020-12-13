import re


class AnkiiError(Exception):
    pass


def uc_len(mod: float, in_unit: str, out_unit: str) -> str:
    valid_units = ['m', 'km', 'f', 'y']
    if not out_unit in valid_units:
    	raise AnkiiError
    if in_unit == 'm':
    	# out_unit conv
        res = 0
        if out_unit == 'm':
            return f'{mod}m'
        elif out_unit == 'km':
            return f'{mod / 1000:.2f}km'
    elif in_unit == 'km':
        pass
    else:
        raise AnkiiError


def uc():
    print('supported type:')
    print('\'length\' for length conversions')
    print('\'weight\' for weight conversions')
    print('\'currency\' for currency conversions')
    t_cov = input('type of conversion: ')
    if t_cov == 'length':
        print('enter value followed by unit in lowercase\n'
              'for example: 13m or 24km')
        in_str = input('> ')
        try:
            in_val = float(re.split('[^.0-9]', in_str)[0])
        except ValueError:
            print('unable to parse input')
            return
        in_unit = re.split('\\d', in_str)[-1]
        print('convert to?')
        print('m\t:meter')
        print('km\t:kilo meter')
        print('f\t:feet')
        print('y\t:yard')
        out_unit = input('>')
        try:
            res = uc_len(in_val, in_unit, out_unit)
        except AnkiiError:
            print('An error occurred')
            return
        print(res)
    elif t_cov == 'weight':
        pass
    elif t_cov == 'currency':
        pass
    else:
        print('unsupported conversion')


def hex_pat(file: str):
    print("File:", file)
    with open(file, 'rb') as f:
        lines = 0
        while True:
            data = f.read(20)
            if not data:
                break
            lines += 1
            if lines % 2:
                print('\033[0;32m', end='')
            else:
                print('\033[0;31m', end='')
            print(data.hex(sep=' ', bytes_per_sep=1))
    print('\033[0m')

