'''
Sample modifiers
[] - set. I.e. [cde]. For range use [a-z]
{} - range. I.e. {2} - 2 repetitions; {2,6} from 2 to 6 repetitions
? - 0 or 1  (also called qualifier). Also works as a non-greedy(matching minimal str first) qualifier. I.e.
    for string '<a> b <c>'  RE <.*> will match the whole string, while <.*?> will match <a>
+ - one or more  (also called qualifier)
* - 0 or more  (also called qualifier)
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
| - or
r"some string" - Use raw python string for regex to avoid \\\\ to match a literal single \.

'''
import re

'''
re.match vs re.search. match checks for the first occurence, search checks for all occurences in a string
re.sub - search and replace
'''

def parse_line():

    # split line by tabs
    line = 'GCF_001477545.1 \t PRJNA342696 \t SAMN02380717 \t LFVZ00000000.1 \t representative genome \t 1408658 4754'
    line_items = re.split(r'\t', line)
    #  Although this also works:
    # line_items = re.split('\t', line)
    print("Second item in a list: "+ line_items[1])

    # Find the part after the last / (i.e. last directory name)
    line = 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/417/885/GCF_001417885.1_Kmar_1.0'
    matchObj = re.search('(?<=/).*$', line)
    if matchObj:
        print('Match is: {}'.format(matchObj.group(0)))
    else:
        print('No match')

# params = re.sub('offset=[0-9]*', "offset=%s" % curr_offset, params)

if __name__ == "__main__":
    parse_line()