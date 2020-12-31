

card_pk = 17115212
door_pk = 3667832


loop_size = 100


value = 1


mod = 20201227

sub_num = 7
value = 1

loop_size = 1


for pk, other in zip([card_pk, door_pk], [door_pk, card_pk]):
    value = 1
    loop_size = 0
    sub_num = 7
    while value != pk:        
        value *= sub_num
        value %= mod
        loop_size += 1

    if value == pk:
        print("loop size", loop_size)
        sub_num = other
        value = 1
        for i in range(loop_size):
            value *= sub_num
            value %= mod

        print(value)
        
    
