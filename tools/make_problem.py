import os
import sys

TEMPLATE = """\
def main():
    # TODO: Implement
    n = int(input())
    print(n)

if __name__ == "__main__":
    main()
"""


def create_problem_folder(problem_name):
    # フォルダ名を作成
    base_path = os.path.expanduser(f"~/AtCoder/{problem_name}")
    os.makedirs(base_path, exist_ok=True)

    # main.py を作成
    main_path = os.path.join(base_path, "main.py")
    if not os.path.exists(main_path):
        with open(main_path, "w") as f:
            f.write(TEMPLATE)

    # test/ フォルダを作成
    test_path = os.path.join(base_path, "test")
    os.makedirs(test_path, exist_ok=True)

    print(f"✅ {problem_name} フォルダを作成しました")
    print(f"📁 cd ~/AtCoder/{problem_name}")
    print(f'🚀 oj t -c "python3 main.py"')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❗ 使い方: python make_problem.py abc123/A")
    else:
        create_problem_folder(sys.argv[1])
