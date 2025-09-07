from django.conf import settings
import requests



class TicketmasterService:
    """
        Class To interact with Ticketmaster API
    """
    BASE_URL = 'https://app.ticketmaster.com/discovery/v2'
    def __init__(self):
        self.api_key = settings.TICKETMASTER_API_KEY

        if not self.api_key:
            raise ValueError(f"The value of Ticketmaster APIs Key is either not found or not valid !:{self.api_key}")
        
    def _make_request(self, endpoint:str,params: dict = None):
         
        try:
            if params is None:
                    params = {}
            if self.api_key:
                params['apikey']= self.api_key
            
            response = requests.get(f"{self.BASE_URL}/{endpoint}",params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Ticketmaster API request failed:{error}")
            return None
        except requests.exceptions.ConnectionError as error:
            print(f"Ticketmaster API Could not connect:{error}")
            return None
        
    def get_events(self,option:dict = None):
        try:
            params =  {'countryCode':'CA','size':10} 
            if option is not None:
                filtered_option = {}
                for k,v in option.items():
                    if v:
                        filtered_option[k] = v
                params.update(filtered_option)                 
            data = self._make_request('events.json',params=params)
            if data:
                return data
            else: 
                return []

        except requests.exceptions.RequestException as error :
            return []
    
    
    


