# benchschi-challenge
Coding challenge for the role of Backend Developer at BenchSci

Description
-----------
BenchSci Backend Technical Task
With a given 10,000 PMCIDs, that can be found at:
https://drive.google.com/file/d/0B_g8TZqZKTt6MUh2WV91OVZNME0/view?usp=sharing
You can download the respective publications, with this given url:
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=PMCID
Resources
https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
With each publication, the following data should be extracted:
figure url,
figure legend/caption
Extract co-occurrence words between figure <caption> and <body> text , and their respective co-occurrence counts.
Co-occurrence is defined such that, given a figure caption <F> and body text <B>, list the words that occur in both <F> and <B>, and the number of co-occurrences. N-grams are not necessary for this task.
create a csv and json file
Load data into a nosql database,
Display data on a web page to allow reviewing of the data in a reasonable format.
Supply us with the url of the page to view online, as well as the code on github
