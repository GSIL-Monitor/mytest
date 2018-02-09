import requests

url = "http://m-sit.tuniu.org/api/train/product/ticketList"

que = "d=%7B%22departureCityCode%22:%222500%22,%22arrivalCityCode%22:%221602%22,%22departureCityName%22:%22%E4%B8%8A%E6%B5%B7%22,%22arrivalCityName%22:%22%E5%8D%97%E4%BA%AC%22,%22departureDate%22:%222017-12-23%22%7D"
headers = {
    'cache-control': "no-cache",
    'postman-token': "4f69779e-abba-0d75-6c16-7ebadead83bd"
    }

response = requests.request("GET", url, headers=headers, params=que)

print(response.text)