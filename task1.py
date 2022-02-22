from datetime import datetime

def isEvenSimple(value):
    return value % 2

def isEvenBite(value):
    return value & 1

def main():
    times = 1000000
    # Первый алгоритм
    start_time = datetime.now()
    for num in range(times):
        isEvenSimple(num)
    print(f"Division method  {datetime.now() - start_time}")

    # Алгоритм с битовой операцией И
    start_time = datetime.now()
    for num in range(times):
        isEvenBite(num)
    print(f"Bit operation method {datetime.now() - start_time}")


if __name__ == '__main__':
    main()



