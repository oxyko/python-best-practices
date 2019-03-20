'''
Entrez is part of biopython. It is NCBI's api to access all the data on the site (sequences, literature, etc.)
For more info on Entrez see: http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc111

NOTE: This is snippet is as of 2018.02.19. Some of the parameters may change.
'''
import Bio.Entrez as Entrez

def get_db_info():
    '''
    Prints the list of databases, available at NCBI.
    '''
    handler = Entrez.einfo()
    response = handler.read()
    handler.close()
    print("Raw (XML) response is:\n" + response)

    handler = Entrez.einfo()
    parsed_response = Entrez.read(handler)
    handler.close()
    print("Parsed response is:\n{}".format(parsed_response))
    print("List of NCBI databases is: \n{}".format(parsed_response["DbList"]))

    handler = Entrez.einfo(db="nucleotide")
    parsed_response = Entrez.read(handler)
    handler.close()
    print("Parsed response is:\n{}".format(parsed_response))
    print("Database description: {}".format(parsed_response['DbInfo']['Description']))
    print("Number of records in db: {}".format(parsed_response['DbInfo']['Count']))
    print("Last update of db: {}".format(parsed_response['DbInfo']['LastUpdate']))
    print("List of db fields: \n")
    print(*parsed_response['DbInfo']['FieldList'], sep='\n')

def run_query():

    Entrez.email="oksana.korol@agr.gc.ca"  # best practise is to register the email

    # Get all fungal ITS:
    query = "txid4751[Organism:exp] AND \"Internal Transcribed Spacer\"[All Fields]"
    handler = Entrez.esearch(db='nucleotide', term=query)
    parsed_response = Entrez.read(handler)
    print("Size of the query response: {}".format(len(parsed_response)))
    print(parsed_response)
    print(*parsed_response, sep='\n')
    print("Count: ".format(parsed_response['Count']))
    print("Number of sequence IDs: ".format(len(parsed_response['IdList'])))

if __name__=="__main__":
    #get_db_info()
    run_query()