# data
data={1:[{'Tea':12},{'Coffee':20},{'Green Tea':25},{'Milk':20}],
      2:[{'kachori':30},{'samosa':20},{'vadapav':15},{'idli':30}],
      3:[{'Perk':10},{'Kitkat':20},{'Dairy Milk':20},{'Yoga Bar': 40}]
      }
#initialisation
want_go_main_menu='y'
bill=0
item_id_list=[]
item_id_list2=[]
item_id_list3=[]
item_quantity_list=[]
item_quantity_list2=[]
item_quantity_list3=[]
item_quantity_main_list=[]
user_selected_key_item_list=[]
user_selected_value_item_list=[]

print("\t  Welcome TO Snacks Center Management System ")
while want_go_main_menu.capitalize()=='Y':
    print("Enter Choice: ")
    user_choice=int(input("1. Drinks \t 2. Snacks \t 3. Chocolates  \n :- "))
    user_category_continue="Y"

    if user_choice==1:
        print("Drinks Menu!")
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format("Id", "Item", "Price"))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(1, "tea", data[user_choice][0]['Tea']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(2, "coffee", data[user_choice][1]['Coffee']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(3, "green Tea", data[user_choice][2]['Green Tea']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(4, "Milk", data[user_choice][3]['Milk']))
        print('+------+------------+---------+')

        while user_category_continue.capitalize()=="Y":
            item_id=int(input("enter id of your item: "))
            while item_id>4 or item_id <=0:
                print('Item not available \t please Enter a valid Item!')
                item_id=int(input("enter id of your item: "))
            item_quantity=int(input("how many quantity to add: "))
            item_id_list.append(item_id)
            item_quantity_list.append(item_quantity)    
            user_category_continue=input("Purchase item from same category ? Y/N: ")

        for item in item_id_list:
            item=item-1    
            user_item_key=data.get(user_choice)[item].keys()
            user_item_value=data.get(user_choice)[item]              
            user_item_main_key=list(user_item_key)[0]
            user_item_main_value=user_item_value.get(user_item_main_key)   
            user_selected_key_item_list.append(user_item_main_key)
            user_selected_value_item_list.append(user_item_main_value)
        want_go_main_menu=input("Want to go Main Menu Y/N: ")
            
    elif user_choice==2:
        print("Snacks Menu!")
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format("Id", "Item", "Price"))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(1, "Kachori", data[2][0]['kachori']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(2, "Samosa", data[2][1]['samosa']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(3, "Vadapav", data[2][2]['vadapav']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(4, "Idli",data[2][3]['idli']))
        print('+------+------------+---------+')

        while user_category_continue.capitalize()=="Y":
            item_id=int(input("enter id of your item: "))
            while item_id>4 or item_id <=0:
                print('Item not available \t please Enter a valid Item!')
                item_id=int(input("enter id of your item: "))
            item_quantity=int(input("how many quantity to add: "))
            item_id_list2.append(item_id)
            item_quantity_list2.append(item_quantity)
            user_category_continue=input("Purchase item from same category ? Y/N: ")
           
        for item in item_id_list2:
            item=item-1
            user_item_key=data.get(user_choice)[item].keys()
            user_item_value=data.get(user_choice)[item]  
            user_item_main_key=list(user_item_key)[0]
            user_item_main_value=user_item_value.get(user_item_main_key)         
            user_selected_key_item_list.append(user_item_main_key)
            user_selected_value_item_list.append(user_item_main_value)
        want_go_main_menu=input("Want to go Main Menu Y/N: ")
            
    elif user_choice==3:
        print("Chocolates Menu!")
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format("Id", "Item", "Price"))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(1, "Perk", data[3][0]['Perk']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(2, "Kitkat", data[3][1]['Kitkat']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(3, "Dairy Milk", data[3][2]['Dairy Milk']))
        print('+------+------------+---------+')
        print('|{:^6}| {:<10} | {:^8}|'.format(4, "Yoga Bar",data[3][3]['Yoga Bar']))
        print('+------+------------+---------+')
        

        while user_category_continue.capitalize()=="Y":
            item_id=int(input("enter id of ur item: "))
            while item_id>4 or item_id <=0:
                print('Item not available \t please Enter a valid Item!')
                item_id=int(input("enter id of your item: "))       
            item_quantity=int(input("how many quantity to add: "))
            item_id_list3.append(item_id)
            item_quantity_list3.append(item_quantity)
            user_category_continue=input("Purchase item from same category ? Y/N: ")
        for item in item_id_list3:  
            item=item-1            
            user_item_key=data.get(user_choice)[item].keys()
            user_item_value=data.get(user_choice)[item]        
            user_item_main_key=list(user_item_key)[0]
            user_item_main_value=user_item_value.get(user_item_main_key)           
            user_selected_key_item_list.append(user_item_main_key)
            user_selected_value_item_list.append(user_item_main_value)             
        want_go_main_menu=input("Want to go Main Menu Y/N: ")
    else:
        print("Invalid Choice, Enter correct choice")
        
item_quantity_main_list=item_quantity_list + item_quantity_list2 + item_quantity_list3
print('+----------+----------+---------+')
print('|{:<10}| {:<7} | {:^8}|'.format("Item", "Quantity", "Price"))
for i in range(len(user_selected_key_item_list)):
    print('+----------+----------+---------+')
    print('|{:<10}| {:^8} | {:^8}|'.format(user_selected_key_item_list[i], item_quantity_main_list[i], item_quantity_main_list[i] * user_selected_value_item_list[i])) 
    bill=bill+ item_quantity_main_list[i] * user_selected_value_item_list[i]

print('+----------+----------+---------+')
print(f'|  Total Amount:      |   {bill}  |')
print('+----------+----------+---------+')

    
        
