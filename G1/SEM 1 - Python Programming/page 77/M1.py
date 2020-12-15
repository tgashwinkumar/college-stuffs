# initialization 
tax = float(input("Enter tax rate: "))

# program greeting
print('This program will calculate a restaurant tab for a couple with') 
print('a gift certificate, with a restaurant tax of', tax * 100, '%\n') 

# get amount of gift certificate
amt_certificate = float(input('Enter amount of the gift certificate: ')) 

# cost of ordered items 
print('Enter ordered items for person 1') 
appetizer_perl = float(input('Appetizier: ')) 
entree_perl = float(input('Entree: ')) 
drinks_perl = float(input('Drinks: ')) 
dessert_perl = float(input('Dessert: ')) 

print('\nEnter ordered items for person 2') 

appetizer_per2 = float(input('Appetizier: '))
entree_per2 = float(input('Entree: ')) 
drinks_per2 = float(input('Drinks: '))
dessert_per2 = float(input('Dessert: ')) 

# total items 
amt_personl = appetizer_perl + entree_perl + drinks_perl + dessert_perl
amt_person2 = appetizer_per2 + entree_per2 + drinks_per2 + dessert_per2 

# compute tab with tax 
items_cost = amt_personl + amt_person2 
tab = items_cost * (1 + tax) 

# display amount owe 
print('\nOrdered items: $', format(items_cost, '.2f')) 
print('Restaurant tax: $', format(items_cost * tax, '.2f')) 
print('Tab: $', format(tab - amt_certificate, '.2f')) 
print('(negative amount indicates unused amount of gift certificate)') 
