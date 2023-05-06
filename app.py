from tableconf import Table, TableConf
from user import User

USER = User(name='siri')
conf = TableConf(num_supply_range=(0, 0))
table = Table([USER], conf)
you = table

while True:
    print(table)
    curr_player = table.curr_player
    curr_player.play_turn()
