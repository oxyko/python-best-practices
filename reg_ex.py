'''
Sample modifiers
[] - range
{} -
? - 0 or 1
+ - one or more
* - 0 or more
^ - beginning of string
$ - end of string

Sample identifiers
. - any character (not new line)
\w - any letter
\W - anything but letter
\d - any digit
\D - anything bu digit


Sample whitespace
\s - space
\t - tab
\n - new line

Other
\ - escape special character (Ex. matching a dot: \.)

'''
import re

def parse_line():

    # split line by tabs
    line = 'GCF_001477545.1 \t PRJNA342696 \t SAMN02380717 \t LFVZ00000000.1 \t representative genome \t 1408658 4754'
    line_items = re.split('\t', line)
    print(line_items[1]) # second item in the line


# params = re.sub('offset=[0-9]*', "offset=%s" % curr_offset, params)

if __name__ == "__main__":
    parse_line()