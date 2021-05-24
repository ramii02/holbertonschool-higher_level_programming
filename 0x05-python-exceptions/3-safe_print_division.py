#!/usr/bin/python3
def safe_print_division(a, b):
    raise = None
    try:
        raise = a / b
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(r))
        return r
