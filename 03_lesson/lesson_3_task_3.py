from address import Address
from mailing import Mailing

to_address = Address(postcode='123567', city='Saint_Petersberg', street='Nevsky_Prospekt', building='10', apartment='4')
from_address = Address(postcode='123456', city='Petrozavodsk', street='Lenina_Avenue', building='30', apartment='1')
cost = 1240
track = '12334455'

mailing = Mailing(to_address, from_address, cost, track)

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей.")