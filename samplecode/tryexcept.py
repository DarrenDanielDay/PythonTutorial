# example 1
print('\ne.g.1\n')
try:
    print('try')
    a=1/0
except ZeroDivisionError as e:
    print('except ZeroDividionError:',e)
except Exception:
    print('except Exception')
else:
    print('else')
finally:
    print('finally')

# example 2
print('\ne.g.2\n')
try:
    print('try')
    a=1/0
except Exception:
    print('except Exception')
except ZeroDivisionError as e:
    print('except ZeroDividionError:',e)


# example 3
print('\ne.g.3\n')
try:
    print('try')
    a=1/0
except ValueError:
    print('except ValueError')
except ZeroDivisionError as e:
    print('except ZeroDividionError:',e)

# example 4
print('\ne.g.4\n')
try:
    print('try')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')

# example 5
print('\ne.g.5\n')
try:
    print('try1')
    try:
        print('try2')
    finally:
        print('finally')
        raise NameError
except Exception as e:
    print('except1', type(e))

# example 6
print('\ne.g.6\n')
try:
    print('try1')
    try:
        print('try2')
        raise ValueError
    finally:
        print('finally')
        raise NameError
except Exception as e:
    print('except1', type(e))

# example 7
print('\ne.g.7\n')
try:
    print('try1')
    try:
        print('try2')
        raise ValueError
    except ValueError:
        print('except2')
        raise EOFError
    except EOFError:
        print('except3')
    finally:
        print('finally')
except Exception as e:
    print('except1', type(e))