recipes = {'oil':
                [
                {'name':'pipelines-oilfields',      'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add wellpads -> pipelines'},
                {'name':'pipelines-oilwells',       'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add fields -> pipelines'},
                {'name':'oilfields-firstmile',      'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add firstmile wellpads -> pipelines'},
                {'name':'oilwells-firstmile',       'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add firstmile fields -> pipelines'},
                {'name':'pipelines-pipelines',      'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add pipelines -> pipelines'},
                {'name':'pipelines-pipelines',      'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add pipelines <- pipelines'},
                {'name':'pipelines-ports',          'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add pipelines -> ports'},
                {'name':'pipelines-ports',          'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add pipelines <- ports'},
                {'name':'shipping-ports',           'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add ports -> shipping_lanes'},
                {'name':'shipping-ports',           'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add ports <- shipping_lanes'},
                {'name':'shipping-shipping',        'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add shipping_lanes -> shipping_lanes'},
                {'name':'shipping-shipping',        'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add shipping_lanes <- shipping_lanes'},
                {'name':'pipelines-refineries',     'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add pipelines -> refineries'},
                {'name':'pipelines-refineries',     'reverse':True,     'dup_1':True,  'dup_2':False,    'desc':'add refineries -> pipelines_2'},
                {'name':'pipelines-ports',          'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 -> ports_2 '},
                {'name':'pipelines-ports',          'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 <- ports_2 '},
                {'name':'shipping-ports',           'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add ports_2 -> shipping_lanes_2'},
                {'name':'shipping-ports',           'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add ports_2 <- shipping_lanes_2'},
                {'name':'pipelines-pipelines',      'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 -> pipelines_2'},
                {'name':'pipelines-pipelines',      'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 <- pipelines_2'},
                {'name':'shipping-shipping',        'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add shipping_lanes_2 -> shipping_lanes_2'},
                {'name':'shipping-shipping',        'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add shipping_lanes_2 <- shipping_lanes_2'},
                {'name':'pipelines-cities',         'reverse':False,    'dup_1':True,  'dup_2':False,   'desc':'add pipelines_2 -> cities'},
                {'name':'pipelines-powerstations',  'reverse':False,    'dup_1':True,  'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'lmports-powerstations',    'reverse':False,    'dup_1':True,  'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'lmcities-powerstations',   'reverse':False,    'dup_1':False, 'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'cities-lastmile',          'reverse':True,     'dup_1':False, 'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'cities-lastmile',          'reverse':False,    'dup_1':False, 'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                ],
        'gas':
               [
                {'name':'pipelines-oilfields',      'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add wellpads -> pipelines'},
                {'name':'pipelines-oilwells',       'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add fields -> pipelines'},
                {'name':'oilfields-firstmile',      'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add firstmile wellpads -> pipelines'},
                {'name':'oilwells-firstmile',       'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add firstmile fields -> pipelines'},
                {'name':'pipelines-pipelines',      'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add pipelines -> pipelines'},
                {'name':'pipelines-pipelines',      'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add pipelines <- pipelines'},
                {'name':'pipelines-lng',          'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add pipelines -> ports'},
                {'name':'pipelines-lng',          'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add pipelines <- ports'},
                {'name':'shipping-lng',           'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add ports -> shipping_lanes'},
                {'name':'shipping-lng',           'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add ports <- shipping_lanes'},
                {'name':'shipping-shipping',        'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add shipping_lanes -> shipping_lanes'},
                {'name':'shipping-shipping',        'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add shipping_lanes <- shipping_lanes'},
                {'name':'pipelines-refineries',     'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add pipelines -> refineries'},
                {'name':'pipelines-refineries',     'reverse':True,     'dup_1':True,  'dup_2':False,    'desc':'add refineries -> pipelines_2'},
                {'name':'pipelines-lng',          'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 -> ports_2 '},
                {'name':'pipelines-lng',          'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 <- ports_2 '},
                {'name':'shipping-lng',           'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add ports_2 -> shipping_lanes_2'},
                {'name':'shipping-lng',           'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add ports_2 <- shipping_lanes_2'},
                {'name':'pipelines-pipelines',      'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 -> pipelines_2'},
                {'name':'pipelines-pipelines',      'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add pipelines_2 <- pipelines_2'},
                {'name':'shipping-shipping',        'reverse':False,    'dup_1':True,  'dup_2':True,    'desc':'add shipping_lanes_2 -> shipping_lanes_2'},
                {'name':'shipping-shipping',        'reverse':True,     'dup_1':True,  'dup_2':True,    'desc':'add shipping_lanes_2 <- shipping_lanes_2'},
                {'name':'pipelines-cities',         'reverse':False,    'dup_1':True,  'dup_2':False,   'desc':'add pipelines_2 -> cities'},
                {'name':'pipelines-powerstations',  'reverse':False,    'dup_1':True,  'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'lmports-powerstations',    'reverse':False,    'dup_1':True,  'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'lmcities-powerstations',   'reverse':False,    'dup_1':False, 'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'cities-lastmile',          'reverse':True,     'dup_1':False, 'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                {'name':'cities-lastmile',          'reverse':False,    'dup_1':False, 'dup_2':False,    'desc':'add pipelines_2 -> power_stn'},
                ],

        'coal':
                [
                {'name':'coalmines-railways',       'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add coalmines -> railways'},
                {'name':'coalmines-firstmile',      'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add coalmines -> firstmile'},
                {'name':'railways-railways',        'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add railways -> railways'},
                {'name':'railways-railways',        'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add railways <- railways'},
                {'name':'railways-ports',           'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add railways -> ports'},
                {'name':'railways-ports',           'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add railways <- ports'},
                {'name':'shipping-ports',           'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add ports -> shipping_lanes'},
                {'name':'shipping-ports',           'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add ports <- shipping_lanes'},
                {'name':'shipping-shipping',        'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add shipping_lanes -> shipping_lanes'},
                {'name':'shipping-shipping',        'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add shipping_lanes <- shipping_lanes'},
                {'name':'railways-powerstations',   'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add railways -> powerstn'},
                {'name':'railways-cities',          'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add railways -> cities'},
                {'name':'lastmile-powerstations',   'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add powerstations lastmile'},
                {'name':'cities-lastmile',          'reverse':False,    'dup_1':False, 'dup_2':False,   'desc':'add cities lastmile'},
                {'name':'cities-lastmile',          'reverse':True,     'dup_1':False, 'dup_2':False,   'desc':'add cities lastmile, reverse'}
                ]
        }