from odoo import models, fields, api
import requests
import json
from requests.auth import HTTPBasicAuth
import logging

class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _description = 'Vehicle Information'
    _order = 'create_date desc, id desc'
    
    name = fields.Char(string='Name')

    registration_number = fields.Char(string='Registration Number')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    color = fields.Char(string='Color')
    year = fields.Char(string='Year')
    EngineSize = fields.Char(string='EngineSize')
    FuelType = fields.Char(string='FuelType')
    IndicativeValue = fields.Char(string='IndicativeValue')
    NumberOfSeats = fields.Char(string='NumberOfSeats')
    BodyStyle = fields.Char(string='BodyStyle')
    ModelDescription = fields.Char(string='ModelDescription')
    car_make = fields.Char(string='Car Make')
    car_model = fields.Char(string='Car Make')
    RegistrationDate = fields.Char(string='RegistrationDate')

    @api.model
    def get_vehicle_information(self, registration_number):
        logging.warning(f"{registration_number=}")
        vehicle_reg_no = registration_number[0]
        username = "salih"
        password = "3xV2qYSKmseESqX"
        #username = "salih"
        #password = "3xV2qYSKmseESqX"
        #testreg = xzz268

        url = "https://www.regcheck.org.uk/api/json.aspx/CheckSweden/"
        url = url + "%s" % (vehicle_reg_no.replace(" ", ""))
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        logging.warning(f"{r=}")
            #{'ABICode': '', 'Description': 'BMW BMW 320D TOURING 320d Touring, E91 (163hk) Stationsvagn kombivagn', 'RegistrationYear': '2007', 'CarMake': 
            #{'CurrentTextValue': 'BMW'}, 'CarModel': {'CurrentTextValue': 'BMW 320D TOURING'}, 'EngineSize': {'CurrentTextValue': '120kW / 163HK'}, 'FuelType': 
            #{'CurrentTextValue': 'DIESEL'}, 'MakeDescription': {'CurrentTextValue': 'BMW'}, 'ModelDescription': {'CurrentTextValue': 'BMW 320D TOURING'}, 'Immobiliser': 
            #{'CurrentTextValue': ''}, 'NumberOfSeats': {'CurrentTextValue': ''}, 'IndicativeValue': {'CurrentTextValue': ''},
            #'DriverSide': {'CurrentTextValue': ''}, 'BodyStyle': {'CurrentTextValue': 'Stationsvagn kombivagn'}, 'Colour': 'BLÅ',
            #'RegistrationDate': '2006-11-28'} 
        if r.status_code == requests.codes['ok']:
            result = r.json()
            logging.warning(f"{result=}")
            # Store the information in the vehicle information model
            vehicle_information = self.env['vehicle.information'].create({
                'name': vehicle_reg_no, 
                'registration_number': vehicle_reg_no,
                'make': result.get('MakeDescription', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                'model': result.get('CarModel', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                #'model_description': result.get('ModelDescription', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                'color': result.get('Colour', ''),
                # 'EngineSize': result.get('EngineSize', ''),       
                'year': result.get('RegistrationDate', '0000')[0:4],
                'car_make': result.get('CarMake', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                'EngineSize': result.get('EngineSize', {'': ''}).get("CurrentTextValue",""),
                'IndicativeValue': result.get('IndicativeValue', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                'NumberOfSeats': result.get('NumberOfSeats', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                'RegistrationDate': result.get('RegistrationDate', {'CurrentTextValue': ''}),
                'FuelType': result.get('FuelType', "{'CurrentTextValue': ''}").get("CurrentTextValue",''),
                'BodyStyle': result.get('BodyStyle', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
                'car_model': result.get('CarModel', {'CurrentTextValue': ''}).get("CurrentTextValue",""),
            })
            return {"car_make":vehicle_information.car_make,"registration_number":vehicle_information.registration_number,"make":vehicle_information.make,"model":vehicle_information.model,"EngineSize":vehicle_information.EngineSize,
                    "color":vehicle_information.color,"FuelType":vehicle_information.FuelType,"RegistrationDate":vehicle_information.RegistrationDate,"BodyStyle":vehicle_information.BodyStyle,"NumberOfSeats":vehicle_information.NumberOfSeats,"CarMake":vehicle_information.car_make,"year":vehicle_information.year,"car_model":vehicle_information.car_model, 'vehicle_id': vehicle_information.id}
        else:
            # Return an error message if the API request fails
            return {'error': 'Could not retrieve vehicle information'}