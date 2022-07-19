# 100 Prisoners Problem

This code is inspired from the @Veritasium view explaining the problem and providing the strategy to
incease the chances of success. I got interested into it while learning probablistic deep learning models and
statistics.

In the following video it was discussed that if the prisoner will start from their box first and then follow the numbers
to form a linked list loop, chances are that the prisoners will be able to find their number easily than looking into
random boxes.

Video link: https://www.youtube.com/watch?v=iSNsgj1OCLA

## How to use

> This program requires python 3.x version

1. Clone the repository
    ```shell
    git clone https://github.com/tbhaxor/100-prisoner-problem.git
    ```
2. Install the external packages
   ```shell
   # using pip
   pip install -r requirements.txt
   
   # using poetry
   poetry install
   ```
3. Run the program
   ```shell
   python ./main.py
   ```

### Help

```
usage: main.py [-h] [-v] [-r] [-s] [-m] [-e] [--show-log]

100 prisoner problem probablity calculator. This project is inspired from @veritasium video

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -r, --random-prisoner
                        randomize prisoner array before box opening (default: False)
  -s, --stop-early      stop on first failure (default: True)
  -m , --max-tries      maximum number of tries each prisoner gets (default: 50)
  -e , --epochs         how many times run prediction task (default: 51)
  --show-log            show debug logs (default: False)
```

## Resources

- https://www.youtube.com/watch?v=iSNsgj1OCLA
- https://en.wikipedia.org/wiki/100_prisoners_problem
- https://math.mit.edu/~apost/courses/18.204_2018/Timothee_Schoen_paper.pdf