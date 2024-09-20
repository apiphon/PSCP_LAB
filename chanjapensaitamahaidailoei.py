'''chanjapensaitamahaidailoei'''
def main():
    '''chanjapensaitamahaidailoei'''
    daysm = 0
    nofwitfloor = int(input())
    nofsitup = int(input())
    nofsitdown = int(input())
    nofrun = int(input())
    limwitfloor = int(input())
    limsitup = int(input())
    limrun = int(input())
    limsitdown = int(input())
    dayofwitfloor = nofwitfloor//limwitfloor
    dayofsitup = nofsitup//limsitup
    dayofrun = nofrun//limrun
    dayofsitdown = nofsitdown//limsitdown
    if nofwitfloor%limwitfloor >0:
        dayofwitfloor += 1
    if nofsitup%limsitup >0:
        dayofsitup += 1
    if nofrun%limrun >0:
        dayofrun += 1
    if nofsitdown%limsitdown >0:
        dayofsitdown += 1
    if dayofwitfloor > dayofsitup:
        daysm = dayofwitfloor
    else:
        daysm = dayofsitup
    if daysm < dayofrun:
        daysm = dayofrun
    if daysm < dayofsitdown:
        daysm = dayofsitdown
    print(daysm)
main()
