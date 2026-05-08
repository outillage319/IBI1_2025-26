class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

    def __str__(self):
        return (f"{self.name}: {self.calories} kcal, "
                f"{self.protein}g protein, "
                f"{self.carbohydrates}g carbs, "
                f"{self.fat}g fat")

    def __repr__(self):
        return (f"food_item('{self.name}', {self.calories}, "
                f"{self.protein}, {self.carbohydrates}, {self.fat})")
        
def calculate_daily_intake(foods_consumed):
    if len(foods_consumed) == 0:
        print("Warning: No food items provided.")
        return None
    
    total_calories = 0.0
    total_protein = 0.0
    total_carbohydrates = 0.0
    total_fat = 0.0
    
    for item in foods_consumed:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrates += item.carbohydrates
        total_fat += item.fat

    CALORIE_WARNING_THRESHOLD = 2500
    FAT_WARNING_THRESHOLD = 90
    
    if total_calories > CALORIE_WARNING_THRESHOLD:
        print(f"WARNING: Calorie intake ({total_calories:.1f} kcal) exceeds ")
        print(f"the recommended daily limit of {CALORIE_WARNING_THRESHOLD} kcal.")
    if total_fat > FAT_WARNING_THRESHOLD:
        print(f"WARNING: Fat intake ({total_fat:.1f} g) exceeds ")
        print(f"the recommended daily limit of {FAT_WARNING_THRESHOLD} g.")
        
    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbohydrates": total_carbohydrates,
        "fat": total_fat
    }
    
# Example usage under normal conditions
if __name__ == "__main__":
    breakfast = food_item("Oatmeal", 150, 5, 27, 3)
    lunch = food_item("Chicken Salad", 350, 30, 10, 20)
    dinner = food_item("Spaghetti Bolognese", 600, 25, 75, 15)
    
    daily_intake = calculate_daily_intake([breakfast, lunch, dinner])
    print(daily_intake)
    
# Example usage under high calorie and fat conditions
    unhealthy_food1 = food_item("Cheeseburger", 1800, 40, 50, 80)
    unhealthy_food2 = food_item("Fries", 800, 5, 60, 25)
    daily_intake_high = calculate_daily_intake([unhealthy_food1, unhealthy_food2])
    print(daily_intake_high)