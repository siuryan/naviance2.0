import requests
import json

with open('config.json', 'r') as f:
    data = f.read()
parsed_data = json.loads(data)

COLLEGE_API_KEY = parsed_data['COLLEGE_API_KEY']
GOOGLE_API_KEY = parsed_data['GOOGLE_API_KEY']

#takes name input from search bar and if there is an exact result for the name, returns that school id from the api, otherwise returns the list of ids
def getId (schoolName):
    schoolUrl = schoolName.lower()
    schoolUrl = schoolUrl.replace(" ", "%20")
    #print schoolUrl
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&school.name=%s" %(COLLEGE_API_KEY, schoolUrl)
    #print url
    r=requests.get(url)
    data = r.text
    schools = json.loads(data)
    #print schools
    #print schools[u'results'][0][u'school'][u'name']
    if len(schools[u'results']) == 0:
        idList = []
        return idList
    if (schools[u'results'][0][u'school'][u'name']) == schoolName:
        idList = []
        idList.append(schools[u'results'][0][u'id'])
        return idList
    else:
        idList = []
        for school in schools[u'results']:
            idList.append(school[u'id'])
        return idList

#returns the name of the college given its id
def getName (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'school'][u'name']

#returns a link to the college's website given its id
def getUrl (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'school'][u'school_url']

#returns a link to a price calulator that estimates the price for attending the college. requires id
def getPriceUrl (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'school'][u'price_calculator_url']

#returns "women" if the school is women only, does the same thing for men, returns no if the school both men and women. requires school id
def getGender (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    if (school[u'results'][0][u'school'][u'women_only']) == 1:
        return "Women"
    if (school[u'results'][0][u'school'][u'men_only']) == 1:
        return "Men"
    else:
        return "No"

#returns the city the college is in given its id
def getCity (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'school'][u'city']

#returns the state the college is in given its id
def getState (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'school'][u'state']

#returns the admission rate of the college(in a string) given its id
def getAdmRate (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'admissions'][u'admission_rate'][u'overall']

#returns average SAT score
def getSat (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'admissions'][u'sat_scores'][u'average'][u'overall']

#returns average ACT score
def getAct (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'admissions'][u'act_scores'][u'midpoint'][u'cumulative']


#returns information about the cost for attending the college given its id
def getPrice (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'cost'][u'avg_net_price'][u'overall']

#returns the rate of getting a pell grant for a college given its id
def getPellGrant (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'aid'][u'pell_grant_rate']

#returns infomation about debt for the college given its id
def getDebt (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'aid'][u'median_debt_suppressed'][u'overall']

#returns the graduation rate of a college given its id
def getCompletion (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'completion'][u'rate_suppressed'][u'overall']

#list format native hawiian pacific islander, black, asian, unknown, white, mixed race, hispanic, alaskan/native american
def getEthnicity (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    eth = {}
    eth['Hawaiian or Pacific Islander'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'nhpi'] * 100
    eth['Black'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'black'] * 100
    eth['Asian'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'asian'] * 100
    eth['Unknown'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'unknown'] * 100
    eth['White'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'white'] * 100
    eth['Two or more'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'two_or_more'] * 100
    eth['Hispanic'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'hispanic'] * 100
    eth['Alaskan or Native American'] = school[u'results'][0][u'2015'][u'student'][u'demographics'][u'race_ethnicity'][u'aian'] * 100
    return eth

#returns dictionary; key = degree, value = percentage
def getDegrees (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    degrees = {}
    programs = school[u'results'][0][u'2015'][u'academics'][u'program_percentage']
    for degree in programs:
        if not programs[degree] == 0:
            degrees[degree] = programs[degree] * 100
    return degrees

#returns the population of the college given its id
def getSize (schoolId):
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=%s&id=%s" %(COLLEGE_API_KEY, schoolId)
    r = requests.get(url)
    data = r.text
    school = json.loads(data)
    return school[u'results'][0][u'2015'][u'student'][u'size']
