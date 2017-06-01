from lxml import etree
import os.path
import json
import ReadPmcids
import StringOperations

def read_xml_aux(pmcid):

    file_location = '/home/krishna/flaskdirectory/benchenv/app/static/benchsci-challenge/data/'+pmcid+'.xml'
    json_object = {'_id':pmcid}
    json_fig_list = []

    if not os.path.isfile(file_location):
        print('No such file')
        return None

    with open(file_location) as file:
        tree = etree.parse(file)
        
        # Retrieve text from body tag
        body_text = ''
        for body in tree.iter('body'):
            body_text = body_text + etree.tostring(body)

        body_text = StringOperations.clean_string(body_text)
        body_dict = StringOperations.tokenize_string(body_text)

        # Iterate over all figs in publication xml file 
        for fig in tree.iter('fig'):
            caption = fig.find('caption')
            if caption is not None: 
                p = caption.find('p')
            else:
                p = None

            # Iterate over ancestors to get URI 
            ancestors = fig.iterancestors()
            uri = 'fig'
            for a in ancestors:
                uri = a.tag+'/'+uri

            fig_id = ''
            if 'id' in fig.attrib:
                fig_id = fig.attrib['id'] 
                uri = uri+':'+fig_id

            text = ''
            if p is not None:
                text = etree.tostring(p)

            text = StringOperations.clean_string(text)
            p_dict = StringOperations.tokenize_string(text)

            cooccurrence = StringOperations.find_cooccurrence(body_dict, p_dict)

            # Add to a json object
            json_subobject = {}
            json_subobject['fig_id'] = fig_id
            json_subobject['uri'] = uri
            json_subobject['text'] = text
            json_subobject['cooccurrence'] = cooccurrence
            json_fig_list.append(json_subobject)

            # Find co-occurence

    json_object['fig_list'] = json_fig_list
    return json_object
    
def read_all_xmls():
    # Get pmcids
    pmcids = ReadPmcids.read_pmcids()

    progress = 0
    # Iterate over publications
    for pmcid in pmcids: 
        json_object = read_xml_aux(pmcid)

        # Write to output json file
        json_outputfile_location = './output_data/'+pmcid+'.json'
        json_writer = open(json_outputfile_location,'wb')
        json_writer.write(json.dumps(json_object))
        json_writer.close() 

        # Display progress once-in-a-while
        progress = progress + 1
        if progress%100==0:
            print(str(progress/len(pmcids))+'% done')

if __name__=='__main__':
    print('To make the indentation error go away')
