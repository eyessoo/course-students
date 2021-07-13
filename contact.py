contact_book = {'Parul' : 'parul@moringa.org',
        'Thomas' : 'thomas@moringa.org',
        'Ashley' : 'ashley@moringa.org',
        'Kellen' : 'kellen@moringa.org',
        'June' : 'june@moringa.org',
        'Joseph' : 'joe@moringa.org',
        'Lillian' : 'lillian@moringa.org',
        'Arnold' : 'arnold@moringa.org'
                }

# Delete a contact from the dictionary when the user specifies the its key

delete_instruction = str(input('Which contact do you want to delete? '))

if delete_instruction == "Parul":
  del contact_book['Parul']

elif delete_instruction == "Thomas":
  del contact_book['Thomas']

elif delete_instruction == "Ashley":
  del contact_book['Ashley']

elif delete_instruction == "Kellen":
  del contact_book['Kellen']

elif delete_instruction == "June":
  del contact_book['June']

elif delete_instruction == "Joseph":
  del contact_book['Joseph']

elif delete_instruction == "Lillian":
  del contact_book['Lillian']

elif delete_instruction == "Arnold":
  del contact_book['Arnold']

print(contact_book)

# Print out the first 2 contacts.

for x,y in list(contact_book.items())[0:2]:
        print(x,y)

#Display the total no. of contacts left in the dictionary.

print(contact_book)
print(len(contact_book))

# Add 2 new contacts in the dictionary.

contact_book["bla"] = "bla@moringa.org"
contact_book["lala"] = "lala@morina.org"


# Print out all the contacts.
print(contact_book)