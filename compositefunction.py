'''composite function'''
def f(x):
    '''docs of fx'''
    return 2 * x
def g(x):
    '''docs of gx'''
    return x / 2 + 1
inputs = int(input())
fgx = f(g(inputs))
gfx = g(f(inputs))
print(f"{fgx:.2f}")
print(f"{gfx:.2f}")
