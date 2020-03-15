def isfloat(word):

    value = word.partition('.')
    if value[0].isdigit() and value[1] == '.' and value[2].isdigit() or \
    value[0] == '' and value[1] == '.' and value[2].isdigit() or \
    value[0].isdigit() and value[1] == '.' and value[2] == '' or word.isdigit():
        return True
    else:
        return False

if __name__ == "__main__":
    print(isfloat('15.7'))
    print(isfloat('.7'))
    print(isfloat('15'))
    print(isfloat('15.'))
