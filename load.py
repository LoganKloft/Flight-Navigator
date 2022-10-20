import driver
import csv
import pandas

"""
ap_id
ap_name
ap_city
ap_country
ap_iata
ap_icao
ap_latitude
ap_longitude
ap_altitude
ap_timezone
ap_dst
ap_tz
ap_type
ap_source

ap_id ap_name ap_city ap_country ap_iata ap_icao ap_latitude ap_longitude ap_altitude ap_timezone ap_dst ap_tz ap_type ap_source
"""
class Airport:
    # ap_id - Unique OpenFlights identifier for this airport.
    # ap_name - Name of airport. May or may not contain the City name.
    # ap_city - Main city served by airport. May be spelled differently from Name.
    # ap_country - Country or territory where airport is located.
    # ap_iata - 3-letter IATA code. Null if not assigned/unknown.
    # ap_icao - 4-letter ICAO code. Null if not assigned.
    # ap_latitude - Decimal degrees, usually to six significant digits. Negative is South, positive is North.
    # ap_longitude - Decimal degrees, usually to six significant digits. Negative is West, positive is East.
    # ap_altitude - In feet.
    # ap_timezone - Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
    # ap_dst - Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown).
    # ap_tz - Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".
    # ap_type - Type of the airport. Value "airport" only.
    # ap_source - Source of this data. "OurAirports" for data sourced from OurAirports. Value "OurAirports" only.

    def __init__(self, ap_id = None, ap_name = None, ap_city = None, ap_country = None, ap_iata = None, ap_icao = None, ap_latitude = None, ap_longitude = None, ap_altitude = None, ap_timezone = None, ap_dst = None, ap_type = None, ap_source = None, *, record = None):
        if record is not None:
            self.ap_id = record[0]
            self.ap_name = record[1]
            self.ap_city = record[2]
            self.ap_country = record[3]
            self.ap_iata = record[4]
            self.ap_icao = record[5]
            self.ap_latitude = record[6]
            self.ap_longitude = record[7]
            self.ap_altitude = record[8]
            self.ap_timezone = record[9]
            self.ap_dst = record[10]
            self.ap_tz = record[11]
            self.ap_type = record[12]
            self.ap_source = record[13]
        else:
            self.ap_id = ap_id
            self.ap_name = ap_name
            self.ap_city = ap_city
            self.ap_country = ap_country
            self.ap_iata = ap_iata
            self.ap_icao = ap_icao
            self.ap_latitude = ap_latitude
            self.ap_longitude = ap_longitude
            self.ap_altitude = ap_altitude
            self.ap_timezone = ap_timezone
            self.ap_dst = ap_dst
            self.ap_tz = ap_tz
            self.ap_type = ap_type
            self.ap_source = ap_source

""" 
al_id 
al_name 
al_alias 
al_iata 
al_icao 
al_callsign 
al_country 
al_active

al_id al_name al_alias al_iata al_icao al_callsign al_country al_active
"""
class Airline:
    # al_id - Unique OpenFlights identifier for this airline.
    # al_name - Name of the airline.
    # al_alias - Alias of the airline. For example, All Nippon Airways is commonly known as "ANA".
    # al_iata - 2-letter IATA code, if available.
    # al_icao - 3-letter ICAO code, if available.
    # al_callsign - Airline callsign.
    # al_country - Country or territory where airport is located.
    # al_active - "Y" if the airline is or has until recently been operational, "N" if it is defunct. This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as "Y"

    def __init__(self, al_id = None, al_name = None, al_alias = None, al_iata = None, al_icao = None, al_callsign = None, al_country = None, al_active = None, *, record = None):
        if record is not None:
            self.al_id = record[0]
            self.al_name = record[1]
            self.al_alias = record[2]
            self.al_iata = record[3]
            self.al_icao = record[4]
            self.al_callsign = record[5]
            self.al_country = record[6]
            self.al_active = record[7]
        else:
            self.al_id = al_id
            self.al_name = al_name
            self.al_alias = al_alias
            self.al_iata = al_iata
            self.al_icao = al_icao
            self.al_callsign = al_callsign
            self.al_country = al_country
            self.al_active = al_active

""" 
r_airline 
r_alid 
r_sap 
r_sapid 
r_dap 
r_dapid 
r_codeshare 
r_stops 
r_equipment

r_airline r_alid r_sap r_sapid r_dap r_dapid r_codeshare r_stops r_equipment
"""
class Route:
    # r_airline - 2-letter (IATA) or 3-letter (ICAO) code of the airline.
    # r_alid - Unique OpenFlights identifier for airline.
    # r_sap - 3-letter (IATA) or 4-letter (ICAO) code of the source airport.
    # r_sapid - Unique OpenFlights identifier for source airport.
    # r_dap - 3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
    # r_dapid - Unique OpenFlights identifier for destination airport.
    # r_codeshare - "Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
    # r_stops - Number of stops on this flight ("0" for direct).
    # r_equipment - 3-letter codes for plane type(s) generally used on this flight, separated by spaces.

    def __init__(self, r_airline = None, r_alid = None, r_sap = None, r_sapid = None, r_dap = None, r_dapid = None, r_codeshare = None, r_stops = None, r_equipment = None, *, record = None):
        if record is not None:
            self.r_airline = record[0]
            self.r_alid = record[1]
            self.r_sap = record[2]
            self.r_sapid = record[3]
            self.r_dap = record[4]
            self.r_dapid = record[5]
            self.r_codeshare = record[6]
            self.r_stops = record[7]
            self.r_equipment = record[8]
        else:
            self.r_airline = r_airline
            self.r_alid = r_alid
            self.r_sap = r_sap
            self.r_sapid = r_sapid
            self.r_dap = r_dap
            self.r_dapid = r_dapid
            self.r_codeshare = r_codeshare
            self.r_stops = r_stops
            self.r_equipment = r_equipment



class Load:
    def __init__(self):
        self.driver = driver.init()

    #     self.airports_file_name = "airports.csv"
    #     self.airlines_file_name = "airlines.csv"
    #     self.routes_file_name = "routes.csv"

    # def parse_airports(self):
    #     with self.driver.session() as session:
    #         # open airport csv
    #         with open(self.airports_file_name, 'r', encoding='UTF-8') as airports_csv_file:
    #             # create csv reader
    #             airports_csv_reader = csv.reader(airports_csv_file)

    #             # process row by row
    #             for record in airports_csv_reader:
    #                 print(record)
    #                 # create an airport object to hold the information read from the csv file
    #                 airport = Airport(record = record)

    #                 # load the airport information into the neo4j instance
    #                 session.execute_write(self.create_airport, airport)

    # # only care about the id, country, name, city, latitude, longitude, and altitude
    # # CAUTION: This method is slightly slower than the current b/c creating new session for each write
    # def load_airport(self, airport):
    #     with self.driver.session() as session:
    #         session.execute_write(self.create_airport, airport)

    # def create_airport(self, tx, airport):
    #     tx.run('''
    #         MERGE (a:Airport {ap_id: $ap_id})
    #         SET a.ap_id = $ap_id
    #         SET a.ap_name = $ap_name
    #         SET a.ap_city = $ap_city
    #         SET a.ap_country = $ap_country
    #         SET a.ap_iata = $ap_iata
    #         SET a.ap_icao = $ap_icao
    #         SET a.ap_latitude = $ap_latitude
    #         SET a.ap_longitude = $ap_longitude
    #         SET a.ap_altitude = $ap_altitude
    #         SET a.ap_timezone = $ap_timezone
    #         SET a.ap_dst = $ap_dst
    #         SET a.ap_tz = $ap_tz
    #         SET a.ap_type = $ap_type
    #         SET a.ap_source = $ap_source
    #     ''', ap_id = airport.ap_id, ap_name = airport.ap_name, ap_city = airport.ap_city, ap_country = airport.ap_country, ap_iata = airport.ap_iata, ap_icao = airport.ap_icao, ap_latitude = airport.ap_latitude, ap_longitude = airport.ap_longitude, ap_altitude = airport.ap_altitude, ap_timezone = airport.ap_timezone, ap_dst = airport.ap_dst, ap_tz = airport.ap_tz, ap_type = airport.ap_type, ap_source = airport.ap_source)

    def clean_data(self):
        # clean airport
        airport = pandas.read_csv('./dirty/airports.csv', header = None)
        airport.columns = ['AirportID', 'Name', 'City','Country', 'IATA','ICAO', 'Latitude','Longitude','Altitude','Timezone', 'DST','TzDatabase','Type','Source']

        # drop unnecessary columns
        cols_airports = ["Altitude", "Source", "Timezone", "Type", "TzDatabase", "DST"]
        airport = airport.drop(cols_airports, axis=1)

        # fill dirty fields
        airport = airport.fillna("N/A")
        airport = airport.replace("-", "N/A")
        airport = airport.replace("\\N", "N/A")
        airport = airport.replace("NAN", "N/A")
        airport = airport.replace("", "N/A")
        airport.to_csv('./clean/airports.csv', index=None)

        # clean airline
        airline = pandas.read_csv('./dirty/airlines.csv', header = None)
        airline.columns = ['AirlineID', 'Name', 'Alias', 'IATA','ICAO',
                    'Callsign','Country','Active']

        # drop unnecessary columns 
        cols_airlines = ("Alias")
        airline = airline.drop(cols_airlines, axis=1)

        # fill dirty fields
        airline = airline.fillna("N/A")
        airline = airline.replace("-", "N/A")
        airline = airline.replace("\\N", "N/A")
        airline = airline.replace("NAN", "N/A")
        airline = airline.replace("", "N/A")
        airline = airline.replace("Unknown", "N/A")
        airline = airline.drop(index=airline.loc[airline.AirlineID == -1].index) # first record is not useful
        airline.to_csv('./clean/airlines.csv', index=None)

        # clean route
        route = pandas.read_csv('./dirty/routes.csv', header = None)
        route.columns = ['Airline','AirlineID','SourceAirport','SourceAirportID',
                        'DestinationAirport','DestinationAirportID',
                        'Codeshare','Stops','Equipment']
        # drop unnecessary columns
        cols_routes = ("Equipment") 
        route = route.drop(cols_routes, axis=1)

        # fill dirty fields
        route = route.fillna("N/A")
        route = route.replace("-", "N/A")
        route = route.replace("\\N", "N/A")
        route = route.replace("NAN", "N/A")
        route = route.replace("", "N/A")
        route['Codeshare'] = route['Codeshare'].replace("N/A","N") # assume invalid codeshare values are 'N'
        route.to_csv('./clean/routes.csv', index=None)

# {AirportID: line[1], Name: line[2], City: line[3], Country: line[4], IATA: line[5], ICAO: line[6], Latitude: line[7], Longitude: line[8], Altitude: line[9], Timezone: line[10], DST: line[11], TzDatabase: line[12], Type: line[13], Source: line[14]}
    def create_airports(self):
        with self.driver.session() as session:
            session.run(''' 
                LOAD CSV WITH HEADERS FROM 'file:///C:/Users/lklof/OneDrive/Documents/Fall 2022 Classes/CptS 415/Flight Navigator/dirty/airlines.csv' AS line
                CREATE (a:Airport)
                SET a = {AirportID: line[1], Name: line[2], City: line[3], Country: line[4], IATA: line[5], ICAO: line[6], Latitude: line[7], Longitude: line[8], Altitude: line[9], Timezone: line[10], DST: line[11], TzDatabase: line[12], Type: line[13], Source: line[14]}
            ''')

# {AirlineID: line[1], Name: line[2], Alias: line[3], IATA: line[4], ICAO: line[5], Callsign: line[6], Country: line[7], Active: line[8]}
    def create_airlines(self):
        with self.driver.session() as session:
            session.run(''' 
                LOAD CSV FROM 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat' AS line
                CREATE (a:Airline)
                SET a = {AirlineID: line[1], Name: line[2], Alias: line[3], IATA: line[4], ICAO: line[5], Callsign: line[6], Country: line[7], Active: line[8]}
            ''')

# {Airline: line[1], AirlineID: line[2], SourceAirport: line[3], SourceAirportID: line[4], DestinationAirport: line[5], DestinationAirportID: line[6], Codeshare: line[7], Stops: line[8], Equipment: line[9]}
    def create_routes(self):
        with self.driver.session() as session:
            session.run('''
                LOAD CSV FROM 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat' AS line
                CREATE (r:Route)
                SET r = {Airline: line[1], AirlineID: line[2], SourceAirport: line[3], SourceAirportID: line[4], DestinationAirport: line[5], DestinationAirportID: line[6], Codeshare: line[7], Stops: line[8], Equipment: line[9]}
            ''')

    def create_relations(self):
        with self.driver.session() as session:
            session.run(''' 
                MATCH (r:Route)
                MATCH (a:Airport)
                WHERE a.AirportID = r.SourceAirportID
                MERGE (a)-[:BEGIN_ROUTE]->(r)
            ''')