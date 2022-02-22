from datetime import datetime

def isEvenSimple(value):
    return value % 2

def isEvenBite(value):
    return value & 1

def main():
    # Первый алгоритм
    start_time = datetime.now()
    for num in range(1000000):
        isEvenSimple(num)
    print(datetime.now() - start_time)

    # Алгоритм с битовой операцией И
    start_time = datetime.now()
    for num in range(1000000):
        isEvenBite(num)
    print(datetime.now() - start_time)


if __name__ == '__main__':
    main()