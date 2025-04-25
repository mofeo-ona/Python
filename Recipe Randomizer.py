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
            print("The ingredients for donuts are\n\nxxx\nxxx\nxxx\nxxx\nxxx")
            print("The instructions are \n\nxxx\nxxx\nxxx")
        elif sw == "muffins":
            print("""The ingredients for muffins are:
                  2 cups all-purpose flour
                  1/2 cup sugar
                  1 tbsp baking powder
                  1/2 tsp salt
                  1 cup milk
                  1/4 cup melted butter
                  1 egg
                  """)
            print("""The instructions are 
                  Preheat oven to 375°F.
                  Mix flour, sugar, baking powder
                  Add milk, egg, melted butter
                  Stir until just barely combined.
                  
                  
                  """)
        elif sw == "cookies":
            print("The ingredients for cookies are\n\nxxx\nxxx\nxxx\nxxx\nxxx\n")
            print("The instructions are \n\nxxx\nxxx\nxxx")
        else:
            print("choose one of the options")

#spicy option
    def spice():
    #asks user for input on preference
        print("Would you like the recipe for spicy chicken tenders, spicy scrambled eggs or jalapeno fries?")
        sp=input().lower()

        if sp =="spicy chicken tenders":
            print("""The ingredients for spicy chicken tenders are
              chicken wings
              xxx
              xxx
              xxx
              xxx
              xxx
              
              Here are the instructions
              1.
              2.
              3.
              4.
              """)
        elif sp == "spicy scrambled eggs":
            print("The ingredients for spicy scrambled eggs are\n\nxxx\nxxx\nxxx\nxxx\nxxx")
            print("The instructions are \n\nxxx\nxxx\nxxx")
        elif sp == "jalapeno fries":
            print("The ingredients for jalapeno fries are\n\nxxx\nxxx\nxxx\nxxx\nxxx\n")
            print("The instructions are \n\nxxx\nxxx\nxxx")
        else:
            print("choose one of the options")

#salty option
    def salty():
    #asks user for input on preference
        print("Would you like the recipe for potato wedges, pretzels or grilled cheese sandwich?")
        sa=input().lower()

        if sa =="potato wedges":
            print("The ingredients for potato wedges are\n\nxxx\nxxx\nxxx\nxxx\nxxx")
            print("The instructions are \n\nxxx\nxxx\nxxx")
        elif sa == "pretzels":
            print("The ingredients for pretzels are\n\nxxx\nxxx\nxxx\nxxx\nxxx\n")
            print("The instructions are \n\nxxx\nxxx\nxxx")
        elif sa == "grilled cheese sandwich":
            print("The ingredients for grilled cheese sandwich are\n\nxxx\nxxx\nxxx\nxxx\nxxx\n")
            print("The instructions are \n\nxxx\nxxx\nxxx")
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