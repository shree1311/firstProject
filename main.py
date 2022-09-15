import bottle
import json
import processing
import data
import csv
import os.path
import data


def load_data():
    csv_file = 'saved_data.csv'
    if not os.path.isfile(csv_file):
        url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
        info = data.json_loader(url)
        heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer',\
                     'administered_unk_manuf','series_complete_pop_pct']
        data.save_data(heads, info, 'saved_data.csv')


@bottle.route('/')
def send_html():
    return bottle.static_file("index.html", root='.')


@bottle.route('/code.js')
def send_frontEndJS():
    return bottle.static_file("code.js", root='.')


@bottle.route("/barChart")
def barChartData():
    lod = data.load_data('saved_data.csv')
    date = processing.max_value(lod, 'date')
    retval = {}
    x = []
    pop = []
    for dict in lod:
        if dict['date'] == date:
            x.append(dict['location'])
            pop.append(dict['series_complete_pop_pct'])
    retval['x'] = x
    retval['y'] = pop
    retval['type'] = 'bar'
    a = []
    a.append(retval)
    return json.dumps(a)


@bottle.route("/pieChart")
def pieChartData():
    lod = data.load_data('saved_data.csv')
    date = processing.max_value(lod, 'date')
    retval = {}
    labels = []
    values = []
    for dict in lod:
        if dict['date'] == date:
            labels.append("Janssen")
            labels.append("Moderna")
            labels.append("Pfizer")
            labels.append("Other")
            values.append(dict['administered_janssen'])
            values.append(dict["administered_moderna"])
            values.append(dict['administered_pfizer'])
            values.append(dict['administered_unk_manuf'])
    retval["labels"] = labels
    retval['values'] = values
    retval['type'] = 'pie'
    a = []
    a.append(retval)
    return json.dumps(a)


def sort1(param):
    return param['date']


@bottle.post("/linechart")
def lineChartCalc():
    contentJSON = bottle.request.body.read().decode()
    content = json.loads(contentJSON)
    state = content['message']
    lod = data.load_data("saved_data.csv")
    lod = processing.copy_matching(lod, 'location', state)
    lod.sort(key=sort1)
    retval = {}
    dates = []
    vaxxed = []
    for dict in lod:
        dates.append(dict['date'])
        vaxxed.append(dict['series_complete_pop_pct'])
    retval['x'] = dates
    retval['y'] = vaxxed
    retval['type'] = 'lines'
    a = []
    a.append(retval)
    return json.dumps(a)


load_data()
bottle.run(host='0.0.0.0', port=8080, debug=True)
