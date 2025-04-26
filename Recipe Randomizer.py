x=True
print(""" 
      WELCOME TO
    ____            _               ______                           __            
   / __ \___  _____(_)___  ___     / ____/__  ____  ___  _________ _/ /_____  _____
  / /_/ / _ \/ ___/ / __ \/ _ \   / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / _, _/  __/ /__/ / /_/ /  __/  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/ |_|\___/\___/_/ .___/\___/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                 /_/                                                               
""")

#loop
while x == True:

#The code for the sweet option
    def sweets():
    #asks user for input on preference
        print("Would you like the recipe for donuts, muffins or cookies?")
        sw=input()

        if sw == "donuts":
            print("""The ingredients for donuts are
    1. 1 cup flour
    2. 1/4 cup sugar
    3. 1 tsp baking powder
    4. pinch of salt
    5. 1/4 cup milk
    6. 1 egg
    7. 1 tbsp oil

                  """)
            print("""The instructions are 
    1. Mix dry ingredients
    2. Mix wet ingredients
    3. stir into a dough
    4. Shape into rings
    5. Fry until golden brown                  
                  
                  """)
        elif sw == "muffins":
            print("""The ingredients for muffins are:
    1. 2 cups all-purpose flour
    2. 1/2 cup sugar
    3. 1 tbsp baking powder
    4. 1/2 tsp salt
    5. 1 cup milk
    6. 1/4 cup melted butter
    7. 1 egg
                  """)
            print("""The instructions are 
    1. Preheat oven to 375°F.
    2. Mix flour, sugar, baking powder
    3. Add milk, egg, melted butter
    4. Stir until just barely combined.
    5. Pour into muffin tin
    6. Bake for 15-20 mins.
                  
                  """)
        elif sw == "cookies":
            print("""The ingredients for cookies are
    1. Butter
    2. Sugar
    3. Eggs
    4. Flour
    5. Baking soda
    6. Vanilla
    7. Chocolate chips
                  """)
            print("""The instructions are
    1.Mix butter, sugar, vanilla, eggs.
    2. Add flour, Baking soda, stir well.
    3. Fold in chocolate chips.
    4. Scoop dough onto baking sheet.
    5. Bake 10 minutes at 350°F.
                  """)
        else:
            print("choose one of the options")

#spicy option
    def spice():
    #asks user for input on preference
        print("Would you like the recipe for spicy chicken tenders, spicy scrambled eggs or jalapeno fries?")
        sp=input().lower()

        if sp =="spicy chicken tenders":
            print("""The ingredients for spicy chicken tenders are
    1. chicken tenders
    2. 1/2 cup hot sauce
    3. 1 tbsp butter
    4. 1 tsp paprika
    5. salt
    6. oil
              
              Here are the instructions
    1. Season chicken
    2. Fry until golden
    3. Melt butter with hot sauce
    4. Toss chicken in spicy sauce
              """)
        elif sp == "spicy scrambled eggs":
            print("""The ingredients for spicy scrambled eggs are
    1. eggs
    2. chilli flakes
    3. salt & pepper
    4. oil or butter
                  
                  """)
            print("""The instructions are 
    1. Whisk eggs with chilli flakes salt and pepper
    2. Heat oil in pan
    3. pour in eggs and scramble until cooked
                  
                  """)
        elif sp == "jalapeno fries":
            print("""The ingredients for jalapeno fries are
    1. Jalapeños
    2. Flour
    3. Cornmeal
    4. Salt, pepper
    5. Buttermilk
    6. Oil
                  """)
            print("""The instructions are 
    1. Slice jalapeños into strips.
    2. Soak in buttermilk briefly.
    3. Mix flour, cornmeal, seasoning.
    4. Coat jalapeños in dry mix.
    5. Fry until golden brown.
                  
                  """)
        else:
            print("choose one of the options")

#salty option
    def salty():
    #asks user for input on preference
        print("Would you like the recipe for potato wedges, pretzels or grilled cheese sandwich?")
        sa=input().lower()

        if sa =="potato wedges":
            print("""The ingredients for potato wedges are
   1. 2–3 large potatoes
   2. 2 tbsp olive oil
   3. 1 tsp paprika
   4. 1/2 tsp garlic powder
   5. Salt and pepper to taste
                  
                  """)
            print("""The instructions are 
    1. Cut potatoes into thick wedges.
    2. Toss with oil and spices.
    3. Spread wedges on baking sheet.
    4. Bake 40 minutes at 425°F.
    5. Flip halfway for even crisp.
                  
                  """)
        elif sa == "pretzels":
            print("""The ingredients for pretzels are
    1. Flour
    2. Yeast
    3. Warm water
    4. Sugar
    5. Salt
    6. Baking soda
    7. Egg
    8. Coarse salt
                  
                  """)
            print("""The instructions are
    1. Mix yeast, water, sugar, salt.
    2. Add flour, knead smooth dough.
    3. Let rise, then shape pretzels.
    4. Boil in baking soda water.
    5. Brush egg, sprinkle coarse salt.
    6. Bake until golden and puffy.
                   """)
            
        elif sa == "grilled cheese sandwich":
            print("""The ingredients for grilled cheese sandwich are
    1. Bread slices (2 per sandwich)
    2. Butter or mayo
    3. Cheese
                  
                  \n""")
            print("""The instructions are 
    1. Butter one side of bread.
    2. Add cheese between unbuttered sides.
    3. Grill buttered sides on pan.
    4. Flip when golden and melty.
    5. Slice, serve hot, enjoy life.
                  
                  """)
        else:
            print("choose one of the options")

#asks user for input on their preference
    print("Do you want sweet, spicy or salty food?")
    flavor=input().lower()

#conditionals for each option
    if flavor == "sweet":
        sweets()
    elif flavor =="spicy":
        spice()
    elif flavor =="salty":
        salty()
    else:
        print("choose an option")

    print("Do you want another recipe?")
    quit=input().lower()

#asks user for input on whether or not they want to continue
    if quit == "yes":
        x=True
    elif quit == "no":
         x=False
    else:
        print("Pick yes or no")