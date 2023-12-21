def delete_contact():
    name_ = input('Enter the name: ')
    addressbook.delete(name_)

def find_info():
    name_ = input('Enter the name: ')
    addressbook.find(name_)
    
def edit_phone():
    name = input('Enter the name: ')
    r = Record(name)
    phone_old_number = input('Enter the old number in format "1234567890": ')
    phone_new_number = input('Enter the new number in format "1234567890": ')
    r.edit_phone(phone_old_number, phone_new_number)
    
def remove_phone():
    name = input('Enter the name: ')
    r = Record(name)
    phone_number = input('Enter the number in format "1234567890": ')
    r.remove_phone(phone_number)