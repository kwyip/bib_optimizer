"""Version:
--------

- bib_optimizer v0.4.2
"""
import sys
from bib_optimizer import helpers

def main():
    if len(sys.argv[1:]) != 3:
        raise Exception("Sorry, please input three files: your tex filename, bib filename, and the desired new bib filename")
    tex = sys.argv[1:][0]
    old_bib = sys.argv[1:][1]
    new_bib = sys.argv[1:][2]

    helpers.bib_opt(tex, old_bib, new_bib)



if __name__ == '__main__':
	main()



