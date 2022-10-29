
import mlogger

@mlogger.logging()
def test_calc(x : int, y : int) -> None:
    print(f'x : {x}, y : {y}')
    print(f'x/y = {x/y}\n')

if __name__ == "__main__":
    test_calc(4, 2)
    test_calc(3, 0)
