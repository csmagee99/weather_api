import unittest
from weather_api import  get_weather

class ApiTest(unittest.TestCase):

    def test_city_name(self):

        x = get_weather(key="<api_key>", city_name='Des Moines')

        if self.assertTrue(x['name'] == 'Des Moines'):
            print('true')

    def test_city_name2(self):

        x = get_weather(key="<api_key>", city_name='df')

        if self.assertTrue(x['message'] == 'city not found'):
            print('true')


    def test_cod_404(self):

        x = get_weather(key="<api_key>", city_name='Des Moines')

        if self.assertTrue(x['cod'] != '404'):
            print('true')

    def tearDown(self):
        print("------- test is over -------")

if __name__ == "__main__":
    unittest.main()



