def main():
    S = input()
    T = input()

    atcoder_set = set("atcoder")

    for s_char, t_char in zip(S, T):
        if s_char == t_char:
            continue
        elif s_char == "@" and t_char in atcoder_set:
            continue
        elif t_char == "@" and s_char in atcoder_set:
            continue
        else:
            print("You will lose")
            return

    print("You can win")


if __name__ == "__main__":
    main()
