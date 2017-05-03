MONGO_HOST = 'localhost'
MONGO_PORT = '27017'

URL_PREFIX = 'api'
MONGO_DBNAME = 'nps'
DOMAIN = {'species':{
    'schema':{
        'Abundance':{'type':'string'},
        'Category': {'type':'string'},
        'Common Names': {'type':'string'},
        'Conservation Status':{'type':'string'},
        'Family':{'type':'string'},
        'Nativeness':{'type':'string'},
        'Occurrence':{'type':'string'},
        'Order':{'type':'string'},
        'Park Name':{'type':'string'},
        'Record Status':{'type':'string'},
        'Scientific Name':{'type':'string'}
    }
}}

X_DOMAINS = '*'
HATEOAS = False
PAGINATION = False
