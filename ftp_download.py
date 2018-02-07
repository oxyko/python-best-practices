'''
Goal: Download a file over ftp.
Contains other helper methods.
'''
import wget, urllib
import ftplib


def ftp_download_wget():
    # wget needs to be installed.
    # Note that is is implemented using urllib, not wget and only has one option: out, which specifies where to copy the
    # file (i.e. no timeout handling, etc.). Use it only for simple quick downloads.
    # The command throw and exception if there is no response after one minute.

    try:
        filename = wget.download('ftp.ncbi.nlm.nih.gov/genomes/refseq/fungi/assembly_summary.txt', out="out_tmp/")
    except urllib.error.URLError as e:
        print(e)

def test_connection_ftplib():
    try:
        ftp_connection = ftplib.FTP('ftp://ftp.ncbi.nlm.nih.gov')
        ftp_connection.connect()
        ftp_connection.voidcmd('NOOP')
        ftp_connection.quit()
        print('Connection established.')
        return True
    except:
        print('No connection to specified ftp.')
        return False

if __name__ == '__main__':
    #ftp_download_wget()
    test_connection_ftplib()

# Options on downloading files over ftp:
# PyCurl python interface to libcurl. http://pycurl.io/docs/latest/
# urllib: urllib.urlretrieve('ftp://server/path/to/file', 'file')
# ftplib library
# wget library. https://pypi.python.org/pypi/wget