import lifestyle.general
import ankii_math.conversions
import application.general

print('--------------Utility Tools--------------')
print('---------------by Ankii077---------------')
print('-----------------------------------------')
print("type 'help' for all commands, 'exit' to quit application")

try:
    while True:
        cmd = input('\033[1;36m$\033[0m ')
        if len(cmd) == 0:
            continue
        if cmd == 'exit':
            break
        elif cmd == 'bmi':
            lifestyle.general.bmi(input('height (in cm): '),
                                  input('weight (in kg): '), input('age: '))
        elif cmd == 'age':
            lifestyle.general.age(input('DOB (DD-MM-YYYY): '))
        elif cmd == 'uc':
            ankii_math.conversions.uc()
        elif cmd == 'bin':
            ankii_math.conversions.hex_pat()
        elif cmd == 'help':
            application.general.print_help()
        else:
            print(repr(cmd), ': command not found', sep='')
            pass
except (KeyboardInterrupt, EOFError):
    print()
