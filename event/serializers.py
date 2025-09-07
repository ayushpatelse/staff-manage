from rest_framework import serializers
from .models import Event


# Process Event Data from JSON
class TicketmasterEventSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    url = serializers.URLField(required=False)
    date = serializers.SerializerMethodField(method_name='get_event_date',required=False)
    description = serializers.CharField(source='pleaseNote',required=False)
    images_url = serializers.SerializerMethodField(method_name='event_image')
    locale = serializers.CharField()
    venue = serializers.SerializerMethodField(method_name='get_venues')

    def get_event_date(self,obj):
        
        return obj['dates']['start']['localDate'] if (obj['dates']['start']['localDate']) else ''

    
    def event_image(self, obj):

        images = obj.get('images', [])
        if images and len(images) > 0:
            return images[0].get('url', '')
        return ''
    
    def get_venues(self,obj):
        """ Get Venue Based on the Event """
        temp_obj = obj
        if temp_obj.get('_embedded'):
            temp_obj = obj['_embedded']

        if temp_obj.get('venues'):
            temp_obj = temp_obj['venues']
        if temp_obj != "":
            multi_obj = True if len(temp_obj)>1 else False
            temp_obj = temp_obj[0]
            temp_data = VenueSerializerTicketmaster(temp_obj,many=multi_obj).data
            return temp_data
        
        return []

# Process Venue Data from JSON
class VenueSerializerTicketmaster(serializers.Serializer):

    

    id = serializers.CharField()
    name = serializers.CharField()
    address = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    postal_code = serializers.CharField(source='postalCode', required=False)


    def get_address(self,obj):
        address = obj.get('address', {})
        return address.get("line1",'')

    def get_city(self,obj):
        city = obj.get('city',{})
        return city.get('name','')

    def get_state(self,obj):
        state = obj.get('state',{})
        return state.get('name','')

    def get_country(self,obj):
        country = obj.get('country',{})
        return country.get('name','')
    


class EmbeddedDataSerializer(serializers.Serializer):
    
    events = serializers.SerializerMethodField(method_name='get_events')

    def get_events(self,obj):
        try:
            temp_obj = obj
            # print("Entered 'get_events'")
            # print(f"Input Type:{type(temp_obj)}")

            if isinstance(temp_obj,dict):
                if temp_obj.get('_embedded'):
                    temp_obj = temp_obj["_embedded"]
                    # print("Extracted '_embedded' data")
                else:
                    print("No '_embedded' key found")
            
            if temp_obj.get("events"):
                    temp_obj = temp_obj["events"]
                    # print(f"Extracted 'events' data - type: {type(temp_obj)}")
                    if isinstance(temp_obj, list):
                        print(f"Events list length: {len(temp_obj)}")
                    else:
                        print("No 'events' key found")
                        return []
            
            multi_obj = True if  len(temp_obj)>1 else False
            try:
                serializer = TicketmasterEventSerializer(temp_obj,many=multi_obj)
                return serializer.data
            except Exception as e:
                print(f"Problem in {e}") 
            
            return []
        except Exception as e:
            print(f"Error processing events: {e}")
            return []

    
      
    
    