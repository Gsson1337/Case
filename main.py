import requests

def main():
    # min API nyckel
    api_key = "e00f1c5f8dcfd9423593c096a8212536"
    
    # vanliga url hemisdan
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # skriv in vilken stad du vill kolla
    city = input("\n Skriv in stad : ")

    # hela adressen
    full_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric" + "&lang=sv"
    
    # få hela objektet med all data
    response = requests.get(full_url)

    # gör om json data till python data
    data = response.json()

    # om in staden hittades får man skriva igen tills man skriver rätt
    while data['cod'] == "404":
        print(" Stad inte hittad")

        city = input("\n Skriv in stad : ")

        full_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric" + "&lang=sv"
        
        response = requests.get(full_url)

        data = response.json()

    # få ut temperaturen
    temperature = data["main"]["temp"]

    # få ut hur temperaturen känns
    feels = data["main"]["feels_like"]

    # var tvungen att lägga till [0] pga det kom som en lista
    description = data["weather"][0]["description"]

    # Få ut landet där staden är
    country = data["sys"]["country"]

    # skriv ut det värden jag tog ut
    print("\n Vädret i " + city +","+ country + ":" + 
        "\n Temperatur: " +
                    str(temperature) + chr(176) + "C" + " (" 
        "känns som = " +
                    str(feels) + chr(176) + "C" + ")" + 
        "\n vädret: " +
                    str(description))


if __name__ == "__main__":
    #kör programmet hela tiden
    while True:
        main()