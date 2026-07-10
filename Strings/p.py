val = input('Enter your Character Here :  ')


if val.lower()=='true':
    val = True
    print(type(val))
    print('Length not applicable')


elif val.lower()=='false':
    val = False
    print(type(val))
    print('Length not applicable')


elif val.isdigit():
    val = int(val)
    print('Length not applicable')
    print(type(val))


else:
    print(type(val))
    print(len(val))


