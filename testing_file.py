def outside():
    def inside():
        print('Deep', t)

    t = 'Purple'
    inside()


outside()