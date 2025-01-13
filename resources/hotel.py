from flask_restful import Resource

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': '4.5',
        'diaria': '420.34',
        'cidade': 'alphacity'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': '4.1',
        'diaria': '319.99',
        'cidade': 'cidade'
    },
    {
        'hotel_id': 'marvel',
        'nome': 'Marvel Hotel',
        'estrelas': '3.9',
        'diaria': '510.00',
        'cidade': 'Marville'
    }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis} 


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found.'}, 404 # not found

"""     def post(self, hotel_id):
    pass

    def put(self, hotel_id):
    pass

    def delete(self, hotel_id):
    pass """
