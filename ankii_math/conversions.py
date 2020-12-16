import re


class AnkiiError(Exception):
    pass


def get_info(msg: str, prmtp: str, supp_types: str) -> (float, str, str):
    print(msg)
    in_str = input('> ')
    try:
        in_val = float(re.split('[^.0-9]', in_str)[0])
    except ValueError:
        print('unable to parse input')
        raise AnkiiError
    in_unit = re.split('\\d', in_str)[-1]
    print(prmtp)
    print(supp_types)
    out_unit = input('>')
    return in_val, in_unit, out_unit


def uc_len(mod: float, in_unit: str, out_unit: str) -> str:
    valid_units = ['m', 'km', 'f', 'y']
    if out_unit not in valid_units:
        raise AnkiiError
    if in_unit == 'm':
        if out_unit == 'm':
            return f'{mod}m'
        elif out_unit == 'km':
            return f'{mod / 1000:.2f}km'
        elif out_unit == 'f':
            total_inches = mod * 39.37
            feet, inches = int(total_inches // 12), total_inches % 12
            return f'{feet}\'{inches:.0f}\"'
        elif out_unit == 'y':
            return f'{mod * 1.094:.2f} yards'
    elif in_unit == 'km':
        if out_unit == 'm':
            return f'{mod * 1000}m'
        elif out_unit == 'km':
            return f'{mod}'
        elif out_unit == 'f':
            return uc_len(mod * 1000, 'm', 'f')
        elif out_unit == 'y':
            return uc_len(mod * 1000, 'm', 'y')
    # TODO: implement all conversions
    else:
        raise AnkiiError


def uc_digital(mod: float, in_unit: str, out_unit: str) -> str:
    valid_units = ['b', 'B', 'KB', 'MB', 'GB']
    print('DE:', mod, in_unit, out_unit)
    if out_unit not in valid_units:
        raise AnkiiError
    if in_unit == 'b':
        if out_unit == 'b':
            return f'{mod}b'
        elif out_unit == 'B':
            return f'{mod / 8:.0f}B'
        elif out_unit == 'KB':
            return f'{mod / 8 / 1024:.2f}'
        elif out_unit == 'MB':
            return f'{mod / 8 / 1024 / 1024:.2f}'
        elif out_unit == 'GB':
            return f'{mod / 8 / 1024 / 1024 / 1024:.2f}'
    elif in_unit == 'B':
        if out_unit == 'b':
            return f'{int(mod * 8)}b'
        elif out_unit == 'B':
            return f'{mod}B'
        elif out_unit == 'KB':
            return f'{mod / 1024:.2f}KB'
        elif out_unit == 'MB':
            return f'{mod / 1024 / 1024:.2f}MB'
        elif out_unit == 'GB':
            return f'{mod / 1024 / 1024 / 1024:.2f}GB'
    elif in_unit == 'KB':
        if out_unit == 'b':
            return f'{int(mod * 8 * 1024)}b'
        elif out_unit == 'B':
            return f'{mod * 1024}B'
        elif out_unit == 'KB':
            return f'{mod:.2f}KB'
        elif out_unit == 'MB':
            return f'{mod / 1024:.2f}MB'
        elif out_unit == 'GB':
            return f'{mod / 1024 / 1024:.2f}GB'
    elif in_unit == 'MB':
        if out_unit == 'b':
            return f'{int(mod * 8 * 1024 * 1024)}b'
        elif out_unit == 'B':
            return f'{mod * 1024 * 1024}B'
        elif out_unit == 'KB':
            return f'{mod * 1024:.2f}KB'
        elif out_unit == 'MB':
            return f'{mod:.2f}MB'
        elif out_unit == 'GB':
            return f'{mod / 1024:.2f}GB'
    # TODO: implement all conversions
    else:
        raise AnkiiError


def uc():
    print('supported type:')
    print('\'length\' for length conversions')
    print('\'weight\' for weight conversions')
    print('\'currency\' for currency conversions')
    print('\'digital\' for digital conversions')
    t_cov = input('type of conversion: ')
    try:
        res = ''
        if t_cov == 'length':
            info = get_info('enter value followed by unit in lowercase\n'
                            'for example: 13m or 24km', 'convert to?',
                            'm\t:meter\n' 'km\t:kilo meter\n' 'f\t:feet\n' 'y\t:yard\n')
            res = uc_len(*info)
        elif t_cov == 'weight':
            pass
        elif t_cov == 'currency':
            pass
        elif t_cov == 'weight':
            pass
        elif t_cov == 'currency':
            pass
        elif t_cov == 'digital':
            info = get_info('enter value followed by unit in lowercase\n'
                            'for example: 13b, 23B, 13B, 24KB, 13.8MB'
                            '(b: bits, B: Bytes, All other prefix are in uppercase)',
                            'convert to?',
                            'b\t:bits\n' 'KB\t:kilo bytes\n' 'MB\t:mega bytes\n' 'GB\t:giga bytes\n')
            res = uc_digital(*info)
        else:
            print('unsupported conversion')
        if res != '':
            print(res)
    except AnkiiError:
        print('An error occurred')
        return


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
