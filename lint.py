import sys
import argparse
from os import walk
from pylint import lint

parser = argparse.ArgumentParser(prog="LINT")

parser.add_argument('-t',
                    '--threshold',
                    help='score threshold to fail pylint runner | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default=9.0,
                    type=float)

args = parser.parse_args()
threshold = float(args.threshold)

py_files = []

for (dirpath, dirnames, filenames) in walk('./'):
    for filename in filenames:
        parts = filename.split('.')
        if (parts[-1] == 'py'):
            py_files.append(dirpath + '/' + filename)



if len(py_files) > 0:
    run = lint.Run(py_files, do_exit=False)
    score = run.linter.stats['global_note']
    
    if score < threshold:
        print('commit is rejected')
        sys.exit(1)


print('verification passed')