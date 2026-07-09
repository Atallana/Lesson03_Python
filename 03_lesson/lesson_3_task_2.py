from smartphone import Smartphone

catalog = [
    Smartphone('iPhone', '17 Pro Max', '+79111111111'),
    Smartphone('Samsung', 'Galaxy S26 Ultra', '+79222222222'),
    Smartphone('Honor', 'Magic 8 Pro 5G', '+79333333333'),
    Smartphone('Infinix', 'HOT 60 Pro', '+79444444444'),
    Smartphone('OPPO', 'A86 Pro', '+79555555555')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")