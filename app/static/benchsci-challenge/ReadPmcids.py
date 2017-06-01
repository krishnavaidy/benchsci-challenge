import urllib

def read_pmcids():
    with open('data/pmcids.txt') as file:
        pmcids = file.readlines()
    pmcids = [x.strip('\n') for x in pmcids]

    pmcids = pmcids[1:] # Cut the first line
    return pmcids
