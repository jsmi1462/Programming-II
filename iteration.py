inventory = [
            ["sweater", 10, 10],
            ["gun", 20, 10],
            ["flower", 1, 1]
            ]
weight = 0
limit = 20
item_names = []
for items in inventory:
    weight += items[2]
    item_names.append(items[0])

print(f"weight is {weight}")
print(item_names)    

if weight >= limit:
    print(f"Your weight is currently {weight}, and your limit is {limit}. Choose an item to drop")
    drop = input("What do you want to drop?")
    while drop not in item_names:
        print("that is not in you inventory")
        drop = input("What do you want to drop?")
    item_names.pop(item_names.index(drop))
    print(item_names)
    for items in inventory:
        if items[0] == drop:
            inventory.remove(items)
    print(inventory)