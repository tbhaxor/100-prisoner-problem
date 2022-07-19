__version__ = "0.1.0"

import logging
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentDefaultsHelpFormatter, RawDescriptionHelpFormatter
import numpy as np


class MyFormatter(RawTextHelpFormatter, RawDescriptionHelpFormatter, ArgumentDefaultsHelpFormatter):
    pass


parser = ArgumentParser(description="100 prisoner problem probablity calculator. This project is inspired from @veritasium video",
                        formatter_class=MyFormatter)
parser.add_argument("-v", "--version", action="version", version=f"v{__version__}")
parser.add_argument("-r", "--random-prisoner", dest="randp", default=False, action="store_true", help="randomize prisoner array before box opening")
parser.add_argument("-s", "--stop-early", dest="stop", default=True, action="store_false", help="stop on first failure")
parser.add_argument("-m", "--max-tries", default=50, dest="tries", type=int, help="maximum number of tries each prisoner gets", metavar="")
parser.add_argument("-e", "--epochs", default=51, help="how many times run prediction task", metavar="")
parser.add_argument("--show-log", default=False, action="store_true", help="show debug logs")
args = parser.parse_args()

if args.show_log:
    logging.basicConfig(format="[%(name)s] - %(message)s", level=logging.INFO)
else:
    logging.basicConfig(format="[%(name)s] - %(message)s", level=logging.CRITICAL)


def do_lookup():
    """
    Iterate over all the prisoners and run jail matrix look. This will randomize the jail matrix on every run.

    :return: None
    :raises: LookupError when either of prisoners fails to find their number before max tries
    """
    # create prison and prisoners
    matrix = np.linspace(0, 99, 100, dtype=int)
    np.random.shuffle(matrix)
    matrix = np.reshape(matrix, (10, 10))
    prisoners = np.linspace(0, 99, 100, dtype=int)
    logging.info("created jail matrix and prisoners")

    # randomize players
    if args.randp:
        np.random.shuffle(prisoners)
        logging.info("randomized prisoners array")

    for prisoner in prisoners:
        p = logging.getLogger("prisoner:%d" % (prisoner + 1))
        p.info("i have started lookup")

        _tries = 0
        row, col = None, None
        for current in range(0, args.tries):
            _tries += 1

            # for the first time, look from prisoner number
            if row is None and col is None:
                p.info("going to my box")
                row, col = prisoner // 10, prisoner % 10

            # if element found, break out of loop
            if matrix[row, col] == prisoner:
                p.info("hurray! I found the box")
                break

            # follow the value at location value from current box
            row, col = matrix[row, col] // 10, matrix[row, col] % 10
            p.info("going to (%d,%d)" % (row, col))
        else:
            p.error("sorry guys I got you all killed!s")
            raise LookupError(f"Prisoner {prisoner} got every body killed!")

    pass


success = 0
failure = 0

for _ in range(args.epochs):

    try:
        do_lookup()
        success += 1
    except LookupError:
        failure += 1

print(f"Success: {success} ({round(success / args.epochs, 4)})")
print(f"Failure: {failure} ({round(failure / args.epochs, 4)})")
