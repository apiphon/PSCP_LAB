'''timing2'''
def time(seconds):
    '''timing2'''
    if seconds < 0 or seconds >= 10000 * 24 * 60 * 60:
        return "ERR_:__:__:__"
    days, remainder = divmod(seconds, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)
    return f"{days:04d}:{hours:02d}:{minutes:02d}:{seconds:02d}"
input_seconds = int(input())
print(time(input_seconds))
