commands = input().split(';')

for comm in commands:
    try:
        res = eval(comm)
    except BaseException:
        try:
            exec(comm)
        except ZeroDivisionError as zde:
            print('ZeroDivisionError')
        except ArithmeticError as ae:
            print('ArithmeticError')
        except KeyError as ke:
            print('KeyError')
        except LookupError as le:
            print('LookupError')
        except FileExistsError as fee:
            print('FileExistsError')
        except FileNotFoundError as ffe:
            print('FileExistsError')
        except OSError as oe:
            print('OSError')
        except ValueError as ve:
            print('ValueError')
        except NameError as ne:
            print('NameError')
        except BaseException:
            print('Other exception')
    else:
        print(res)
