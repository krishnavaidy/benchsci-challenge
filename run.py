# run.py

from app import app
from flask import Flask, render_template, request, json, redirect, url_for
import sys
sys.path.append('app/static/benchsci-challenge/')
import QueryAndLoadMongo
import ExtractFigPublications

@app.route('/getPmcid', methods=['GET','POST'])
def get_pmcid():

    pmcid = request.form['pmcid'].encode('ascii','ignore')

    if not QueryAndLoadMongo.does_exist(pmcid):
        json_object = ExtractFigPublications.read_xml_aux(pmcid)
        print('Inserting Json Object')
        print(json_object)
        if json_object is not None:
            QueryAndLoadMongo.insert_to_db(json_object)
        else:
            return redirect('error.html')


    cursor = list(QueryAndLoadMongo.retrieve_from_db(pmcid))

    json_object = None

    for j in cursor:
        json_object = j
        break

    replace_string = '<table>\n'
    if json_object is not None:
        replace_string = replace_string+'<tr><th>PMCID</th>'+'<td>'+json_object['_id']+'</td> </tr>'

        for fig in json_object['fig_list']:
            replace_string = replace_string+'<tr><th>Figure URI</th>'+'<td>'+fig['uri']+'</td></tr>' 

            replace_string = replace_string+'<tr><th>Word</th><th>Cooccurrence</th></tr>'
            for word in fig['cooccurrence']:
                replace_string = replace_string +  '<tr><td>'+ str(word) +'</td><td>'+str(fig['cooccurrence'][word])+'</td></tr>\n' 

            replace_string = replace_string + '\n'
    else:
        replace_string = replace_string + 'Publication not found.'

    replace_string = replace_string + '</table>'


    results_file = open('app/templates/results_pre_replacement.html','r')
    results_text = results_file.read().replace('STANDIN_TEXT', replace_string)
    results_file.close()

    results_output = open('app/templates/results.html','w')
    results_output.write(results_text)
    results_output.close()

    print('Results read')

    return redirect('results.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
