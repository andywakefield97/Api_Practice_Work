import requests
import json

fifa_api_base = 'https://fut.best/api/players?page=1&limit=20'
fifa_data = requests.get(fifa_api_base)


class FIFA_Data_Pull:
    def __init__(self):
        self.fifa_api_base = fifa_api_base
        self.fifa_data = fifa_data


    def get_status_code_fifa_data():
        if fifa_data.status_code == 200:
            print('Succesful connection, the Status Code is 200')
        else:
            print('Unsuccesful Connection made')

    def json_fifa_data():
        return print(fifa_data.json())

    if __name__ == '__main__':
        get_status_code_fifa_data()
        json_fifa_data()



class Format_FIFA_Data(FIFA_Data_Pull):
    def __init__(self):
        super(FIFA_Data_Pull, self).__init__()

    def for_loop_data():
        for x in fifa_data:
            print(x)

    def reformat_fifa_data():
        x = fifa_data.json()
        for line in fifa_data:
            yield dict(zip(x, json.loads(line)))

    if __name__ == '__main__':
        reformat_fifa_data()









#goretzka = {"nameOnCard": "Goretzka"}

#get_goretzka = requests.get(fifa_api_base, params = goretzka)
#print(get_goretzka.text)


