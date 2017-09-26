import urllib2
import json


def weather(key, state, city):

    f = urllib2.urlopen('http://api.wunderground.com/api/' + key + '/conditions/forecast/q/' + state + '/' + city
                        + '.json')

    json_string = f.read()
    parsed_json = json.loads(json_string)

    temp = parsed_json['current_observation']['temp_f']
    condition = parsed_json['forecast']['simpleforecast']['forecastday'][0]['conditions']

    print "Current temperature is %s. Conditions for today are %s." % (temp, condition)
    f.close()

