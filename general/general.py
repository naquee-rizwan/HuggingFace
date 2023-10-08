# Just done to keep things in mind
def arg_fun(*argv):
    for argument in argv:
        print(argument, end=' ')
    print()


arg_fun('Hugging,', 'Face')

print('--------------------------------------------------')


# Just done to keep things in mind
def k_args_fun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


k_args_fun(first='Hugging', mid='Face')

print('--------------------------------------------------')
