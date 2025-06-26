def main():
    N = int(input())
    T = input()
    A = input()

    for i in range(N):
        if T[i] == 'o' and A[i] == 'o':
            print('Yes')
            return
    print('No')


if __name__ == "__main__":
    main()
