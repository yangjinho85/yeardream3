# Test python env
''' asd'''
def print_hello():
    animals = ['dog','cat','hamster','tiger'] # in one line
    foods = [
        'Spagetti',
        'Pizza',
	'bibimbob'
    ] # w/o trailing comma
    names = [
        'John',
        'Jane',
        'Gil-dong',
	'dong-eun',
    ] # w/ trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()#이제 이걸 파이썬 메인으로 정했다 

print("hello")
