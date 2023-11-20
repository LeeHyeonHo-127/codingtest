"""
Wheel command line tool (enable python -m wheel syntax)
"""

from __future__ import annotations

import sys


def main():  # needed for console script
    if __package__ == "":
        # To be able to run 'python wheel-0.9.whl/wheel':
        import os.path

        path = os.path.dirname(os.path.dirname(__file__))
        sys.path[0:0] = [path]
    import wheel.cli

    sys.exit(wheel.cli.main())

def ps():
    a = [2, 4, 7, 5, 1, 8, 6, 4]
    for i in a:
        even_or_odd = '짝' if i % 2 == 0 else '홀'
        print(i, even_or_odd)

    b = ["짝" if j % 2 == 0 else "홀" for j in a]
    print(b)



if __name__ == "__main__":
    ps()

