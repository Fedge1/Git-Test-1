
# Open Client TSV file...

import csv
import os
import inspect
from datetime import datetime



# Open the Client Data File, and if marked, add record to Client (Array) List
def getClientsToDisplay():
    clientDataList = []
    # Get the Client Database, and correct path
    script_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    clientFile_path = os.path.join(script_directory, 'Data', 'FullMasteringClientDB.tsv')
    # open Data, and Read
    with open(clientFile_path, 'r') as clientDataFile:
        tsv_reader = csv.DictReader(clientDataFile, fieldnames=['display', 'artist', 'release', 'image', 'album', 'website'], delimiter='\t')
        for line in tsv_reader:
            if line['display'] == 'Y':
                clientDataList.append(line)
    return clientDataList


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))

def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))




# Main Function / Program
def main():
    clientData = getClientsToDisplay()

    # Sort the clients by 'keying' off of the Release Date of that record
    sorted_clientData = sorted(clientData, key=lambda c: datetime.fromisoformat(c['release']), reverse=True)

    for record in sorted_clientData:
        releaseDate = datetime.fromisoformat(record['release'])
        prGreen(record['artist'])
        print('  "{}\", Released: {}'.format(record['album'], releaseDate.year))

    prYellow(len(clientData))


if __name__ == "__main__":
    main()

                

            

        

