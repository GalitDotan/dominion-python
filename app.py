from tableconf import Table, TableConf
from user import User

USER = User(name='siri')
YOU = USER.get_player()
conf = TableConf(num_suply_range=(0, 0))
table = Table([USER], conf)

print(table)

while True:
    pass
