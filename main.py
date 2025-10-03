from pyscript import document

# Prices of the food items
truffle_pasta_price = 320
cheese_pizza_price = 250
caesar_salad_price = 150
iced_latte_price = 80
fresh_lemonade_price = 60

# Tax rate
TAX_RATE = 0.08

# Function that runs when the button is clicked
def generate_order(e):
    # Get customer info from the input fields
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    # Start total at 0
    total = 0

    # Check which items are selected and add their prices to total
    if document.getElementById("item1").checked:    
        total = total + truffle_pasta_price
    if document.getElementById("item2").checked:
        total = total + cheese_pizza_price
    if document.getElementById("item3").checked:
        total = total + caesar_salad_price
    if document.getElementById("item4").checked:
        total = total + iced_latte_price
    if document.getElementById("item5").checked:
        total = total + fresh_lemonade_price

    # Calculate total including tax
    final_total = total + (total * TAX_RATE)

    # Create the message to show in the output
    message = f'''🍽️ Order
\nCustomer Name : {name}
Address       : {address}
Contact       : {contact}
\nTotal Amount  : ₱{final_total:.2f}
\nThank you for ordering at The FoodFather!'''

    # Show the message in the output box
    document.getElementById("output").innerText = message
