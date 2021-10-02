from string import ascii_lowercase

chairOrders = {i:j for i,j in enumerate(ascii_lowercase,1)}

inputOrders = {j:i for i,j in enumerate(input(),1) if chairOrders[i]==j}

print(len(inputOrders))