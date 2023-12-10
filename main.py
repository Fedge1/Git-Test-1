####################
## This is a program to load up my client data base, and convert the data into
## HTML for my website... a work in progress ;)
####################

import csv
import os
import inspect
from datetime import datetime
import print_colours as pr


####################
# Open the Client Data File, and if marked, add record to Client (Array) List
####################
def getClientsToDisplay():
    clientDataList = []
    # Get the Client Database, and correct path
    
    script_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    clientFile_path = os.path.join(script_directory, 'Data', 'FullMasteringClientDB.tsv')

    # open Data, and Read
    with open(clientFile_path, 'r') as clientDataFile:
        tsv_reader = csv.DictReader(clientDataFile, fieldnames=['display',
                                                                'artist',
                                                                'release',
                                                                'image',
                                                                'album',
                                                                'website'], delimiter='\t')

        for line in tsv_reader:
            if line['display'] == 'Y':
                clientDataList.append(line)
    return clientDataList


####################
# Main Function / Program
####################
def main():
    clientData = getClientsToDisplay()

    # Sort the clients by 'keying' off of the Release Date of that record
    sorted_clientData = sorted(clientData, key=lambda c: datetime.fromisoformat(c['release']), reverse=True)

    for record in sorted_clientData:
        releaseDate = datetime.fromisoformat(record['release'])
        pr.Green(record['artist'])
        print('  "{}\", Released: {}'.format(record['album'], releaseDate.year))

    #prYellow(len(clientData))
    pr.Yellow(len(clientData))


####################    
if __name__ == '__main__':
    main()
####################



