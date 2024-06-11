names_list = input("Enter item names: ").split()
quantities_list = [int(qty) for qty in input("Enter item quantities: ").split()]
prices_list = [float(price) for price in input("Enter item prices: ").split()]
availability_list = input("Enter item availability (yes/no): ").split()

GST_RATE = 0.15 
DISCOUNT_RATE = 0.20
def create_row(name, quantity, price, availability):
    name_col = name.ljust(20)
    quantity_col = str(quantity).ljust(15)
    price_col = str(price).ljust(10)
    availability_col = availability.ljust(15)
    return name_col + quantity_col + price_col + availability_col

print(create_row("Item Name", "Item Quantity", "Item Price", "Availability"))

for name, quantity, price, availability in zip(names_list, quantities_list, prices_list, availability_list):
    print(create_row(name, quantity, price, availability))

bill_items = []
total_amount = 0.0

print("\nBilled Items:")
for index in range(len(names_list)):
    print(f"{index + 1}. {names_list[index]}")

while True:
    choice = input("Enter item number or 'done': ").strip()
    if choice.lower() == 'done':
        break
    elif choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(names_list):
            index = choice - 1
            if availability_list[index].lower() == 'yes':
                bill_items.append((names_list[index], quantities_list[index], prices_list[index], availability_list[index]))
                total_amount += quantities_list[index] * prices_list[index]
                print(f"Added {names_list[index]} to the bill.")
            else:
                print(f"{names_list[index]} is not available.")
        else:
            print("Invalid choice. Please select a valid number.")
    else:
        print("Invalid input. Please enter a number or 'done'.")

print("\nFinal Bill:")
print(create_row("Item Name", "Item Quantity", "Item Price", "Availability"))
for name, quantity, price, availability in bill_items:
    print(create_row(name, quantity, price, availability))

gst_amount = total_amount * GST_RATE
discount_amount = total_amount * DISCOUNT_RATE
final_amount = total_amount + gst_amount - discount_amount

print(f"\nTotal Amount: {total_amount:.2f}")
print(f"GST (15%): {gst_amount:.2f}")
print(f"Discount (20%): {discount_amount:.2f}")
print(f"Final Amount: {final_amount:.2f}")
