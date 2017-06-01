import StringOperations

def read_xml_aux(pmcid):
    file_location = './data/'+pmcid+'.xml'

    with open(file_location) as file:
        tree = etree.parse(file)

        for fig in tree.iter('fig'):
            caption = fig.find('caption')
            if caption is not None:
                p = caption.find('p')
            else:
                p = None

