import urllib
import os.path
import ReadPmcids

URLPREFIX = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='

def download_publications():
    pmcids = ReadPmcids.read_pmcids()
    progress = 0 # Count of urls downloaded
    for pmcid in pmcids:
        url = URLPREFIX + pmcid
        file_location =  './data/'+pmcid+'.xml'
        testfile = urllib.URLopener()
        testfile.retrieve(url, file_location)

        progress = progress + 1 # update progress
        if(progress%100==0): # display progress once-in-a-while
            print(str(100*progress/len(pmcids)) + '% done')

def retry_download_publications():
    pmcids = ReadPmcids.read_pmcids()

    print('Number of publications: '+str(len(pmcids)))

    for pmcid in pmcids:
        url = URLPREFIX + pmcid
        file_location = './data/'+pmcid+'.xml'
        if not os.path.isfile(file_location):
            testfile = urllib.URLopener()
            testfile.retrieve(url, file_location)


if __name__ == "__main__":
    # download_publications()
    retry_download_publications()

