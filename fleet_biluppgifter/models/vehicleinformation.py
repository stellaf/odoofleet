from odoo import models, fields, api
import requests
import json
from requests.auth import HTTPBasicAuth
import logging
import re
from bs4 import BeautifulSoup


class FleetVehicleInherit(models.Model):
    _inherit = 'fleet.vehicle'
    
    model_id = fields.Many2one('fleet.vehicle.model', 'Model',
        tracking=True, required=False, help='Model of the vehicle')
    
    # engine_size = fields.Char(string='Engine Size')
    indicative_value = fields.Char(string='Indicative Value')
    body_style = fields.Char(string='Body Style')
    registration_date = fields.Char(string='Registration Date')
    last_inspection_date = fields.Char(string="Last Inspection Date")

    
    def _search_vehicle_make(self, make):
        make_id = self.env['fleet.vehicle.model.brand'].search([('name', '=ilike', make)], limit=1)
        if not make_id:
            make_id = self.env['fleet.vehicle.model.brand'].create({
                'name': make
            })
        return make_id
    
    def _search_vehicle_model(self, model, make):
        model_id = self.env['fleet.vehicle.model'].search([('name', '=ilike', make), ('brand_id', '=', self._search_vehicle_make(make).id)], limit=1)
        if not model_id:
            model_id = self.env['fleet.vehicle.model'].create({
                'name': model,
                'brand_id': self._search_vehicle_make(make).id
            })
        return model_id
    
    def _scrape_bluppgifter(self, plate_number):
        vgm_url = f"https://biluppgifter.se/fordon/{plate_number}"
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        spans = soup.find_all('span')
        crawled_data = {}
        xd = soup.find(class_="list-data enlarge")
        
        for li in soup.find(class_="list-data enlarge").find_all('li'):
            label = li.find("span", "label").text.strip()
            value = li.find("span", "value").text.strip()
            crawled_data[label] = value
        
        for list_data_div in soup.find_all(class_="list-data mb-4 enlarge"):
            for li in list_data_div.find_all('li'):
                label = li.find("span", "label").text.strip()
                value = li.find("span", "value").text.strip()
                crawled_data[label] = value
                
        return crawled_data
    
    def fetch_vehicle_details(self):
        details = self._scrape_bluppgifter(self.license_plate)
        self.color = details.get('Färg')
        self.vin_sn = details.get('Chassinr / VIN')
        self.seats = int(''.join(re.findall(r'\d+', details.get('Passagerare')))) + 1
        fabrikat = details.get('Fabrikat').split('-')[0]
        self.model_id = self._search_vehicle_model(details.get('Modell'), fabrikat).id
        
        logging.warning(f"{details.get('Mätarställning (besiktning)')}")
        if details.get('Mätarställning (besiktning)', False):
            self.odometer = int(''.join(re.findall(r'\d+', details.get('Mätarställning (besiktning)'))))
            
        if details.get('CO2-utsläpp (NEDC)', False):
            self.co2 = int(''.join(re.findall(r'\d+', details.get('CO2-utsläpp (NEDC)'))))
        self.model_year = details.get('Fordonsår / Modellår')
        self.body_style = details.get('Kaross')
        
        self.registration_date = details.get('Först registrerad')
        self.last_inspection_date = details.get('Senast besiktigad')
        
        if details.get('Växellåda') == 'Manuell':
         self.transmission = 'manual'
        else:
            self.transmission = 'automatic'

        if details.get('Drivmedel') == 'Bensin':
            self.fuel_type = 'gasoline'
        elif details.get('Drivmedel') == 'El':
            self.fuel_type = 'electric'
        else:
            self.fuel_type = details.get('Drivmedel').lower()

    
        engine_size = details.get('Motoreffekt').replace(' ', '').strip().split('/')
        if len(engine_size) > 1:
            self.horsepower = int(engine_size[0][:-2])
            self.power = int(engine_size[1][:-2])
        
                                                                                                                                                                                                                                                                                                                        




