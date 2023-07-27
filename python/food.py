# define class
class foods:
    def __init__(self, title, ftype, quality_score, popularity_score, price):
        self.title = title
        self.ftype = ftype
        self.quality_score = quality_score
        self.popularity_score = popularity_score
        self.price = price

food_list = []
# appending instances to list
food_list.append(foods('ข้าวผัด', 'อาหารหลัก', 7, 5, 25))
food_list.append(foods('ข้าวไข่เจียว', 'อาหารหลัก', 4, 9, 15))
food_list.append(foods('ขนมพุดดิ้ง', 'ขนมหวาน', 5, 9, 30))
food_list.append(foods('ไอศรีมกะทิ', 'ขนมหวาน', 5, 8, 10))
food_list.append(foods('ขนมปังสังขยา', 'ขนมหวาน', 6, 7, 15))
food_list.append(foods('ข้าวยำ', 'อาหารหลัก', 10, 3, 25))
food_list.append(foods('ข้าวซอยไก่', 'อาหารหลัก', 8, 5, 30))


# Accessing food object value
for food in food_list:
    print(food.title, food.ftype, sep=' ')
