from smartphone import Smartphone
catalog = [Smartphone("Samsung", "Galaxy S25", "+79257043308"),
           Smartphone("Apple", "iPhone 15", "+79249026307"),
           Smartphone("Xiaomi", "Redmi Note 14", "+79740877367"),
           Smartphone("Tecno", "Camon 40", "+79253435589"),
           Smartphone("Honor", "X7c", "+79268529631")]

for smartphone in catalog:
    print(f"{smartphone.mark}-{smartphone.modele} {smartphone.nomber}")
