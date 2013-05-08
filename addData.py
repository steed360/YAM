from yam.models import *

# Create Ingredient States
choppedIngredientState = IngredientState (state = "chopped")
choppedIngredientState.save ()
cutIntoSquaresIngredientState = IngredientState (state = "cut into squares")
gratedIngredientState = IngredientState (state = "grated")
gratedIngredientState.save ()
wholeSmallIngredientState = IngredientState (state = "whole", subState = "small")
wholeSmallIngredientState.save ()
wholeMediumIngredientState = IngredientState (state = "whole", subState = "medium")
wholeMediumIngredientState.save ()
wholeLargeIngredientState = IngredientState (state = "whole", subState = "large")
wholeLargeIngredientState.save ()
noIngredientState = IngredientState (state = "none")
noIngredientState.save ()
looseIngredientState = IngredientState (state = "loose")
looseIngredientState.save ()

print "#############################################"
print "Ingedient States"
print "------------------"

for i in IngredientState.objects.all ():
    print i
print "#############################################"


# Create Ingredient Container Measures
cupContainerMeasure = ContainerMeasure (name="Cup")
cupContainerMeasure.save ()
tablespooonContainerMeasure = ContainerMeasure (name="Tablespoon")
tablespooonContainerMeasure.save ()
gramContainerMeasure = ContainerMeasure (name="Gram")
gramContainerMeasure.save ()
tbspContainerMeasure = ContainerMeasure (name="Tbsp")
tbspContainerMeasure.save ()


print "\n\n#############################################"
print "Container Measures"
print "------------------"

for i in ContainerMeasure.objects.all ():
    print i
print "#############################################"


# Create Ingredient Categories
vegetableIngredientCategory = IngredientCategory (name="Vegetables")
vegetableIngredientCategory.save ()
dairyIngredientCategory = IngredientCategory (name="Dairy")
dairyIngredientCategory.save ()
grainsIngredientCategory = IngredientCategory (name="Grains")
grainsIngredientCategory.save ()
meatsIngredientCategory = IngredientCategory (name="Meats")
meatsIngredientCategory.save ()
fruitIngredientCategory = IngredientCategory (name="Fruits")
fruitIngredientCategory.save ()


print "\n\n#############################################"
print "Ingredient Categories"
print "------------------"

for i in IngredientCategory.objects.all ():
    print i
print "#############################################"


# Create Basic Ingredients
#Protein_(g)	Lipid_Tot_(g)	Carbohydrt_(g)	Fiber_TD_(g)	Sugar_Tot_(g)	Calcium_(mg)

couscous  = BasicIngredient (name="Cous Cous")
couscous.save ()
couscous.permittedStates.add (looseIngredientState)
couscous.ingredientCategory = grainsIngredientCategory
couscous.referenceQuantityInGrams = 100
couscous.Grammes_Fat      = 0.14
couscous.Grammes_Carbs    = 23.22
couscous.Grammes_Fibre    = 1.4
couscous.Grammes_Protein  = 3.79
couscous.Grammes_Sugar    = 0.1
couscous.MG_Calcium       = 8
couscous.save()

carrot  = BasicIngredient (name="Carrot")
carrot.save ()
carrot.permittedStates.add (gratedIngredientState)
carrot.ingredientCategory = vegetableIngredientCategory
carrot.referenceQuantityInGrams = 100
carrot.Grammes_Fat      = 0.24
carrot.Grammes_Carbs    = 9.58
carrot.Grammes_Fibre    = 2.8
carrot.Grammes_Protein  = 0.93
carrot.Grammes_Sugar    = 4.74
carrot.MG_Calcium       = 33
carrot.save()

cabbage  = BasicIngredient (name="Cabbage")
cabbage.save ()
cabbage.permittedStates.add (gratedIngredientState)
cabbage.ingredientCategory = vegetableIngredientCategory
cabbage.referenceQuantityInGrams = 100
cabbage.Grammes_Fat      = 0.16
cabbage.Grammes_Carbs    = 7.37
cabbage.Grammes_Fibre    = 2.1
cabbage.Grammes_Protein  = 1.43
cabbage.Grammes_Sugar    = 2.83
cabbage.MG_Calcium       = 45
cabbage.save()

oliveOil  = BasicIngredient (name="Olive Oil")
oliveOil.save ()
oliveOil.permittedStates.add (noIngredientState)
oliveOil.ingredientCategory = grainsIngredientCategory
oliveOil.referenceQuantityInGrams = 100
oliveOil.Grammes_Fat      = 100
oliveOil.Grammes_Carbs    = 0
oliveOil.Grammes_Fibre    = 0
oliveOil.Grammes_Protein  = 0
oliveOil.Grammes_Sugar    = 0
oliveOil.MG_Calcium       = 1
oliveOil.save()

raisins  = BasicIngredient (name="Raisins")
raisins.save ()
raisins.permittedStates.add (looseIngredientState)
raisins.ingredientCategory = fruitIngredientCategory
raisins.referenceQuantityInGrams = 100
raisins.Grammes_Fat      = 0.46
raisins.Grammes_Carbs    = 79.18
raisins.Grammes_Fibre    = 3.7
raisins.Grammes_Protein  = 3.07
raisins.Grammes_Sugar    = 55.19
raisins.MG_Calcium       = 50
raisins.save()


cottageCheese  = BasicIngredient (name="Cottage Cheese")
cottageCheese.save ()
cottageCheese.permittedStates.add (noIngredientState)
cottageCheese.ingredientCategory = dairyIngredientCategory
cottageCheese.referenceQuantityInGrams = 100
cottageCheese.Grammes_Fat      = 4.3
cottageCheese.Grammes_Carbs    = 3.38
cottageCheese.Grammes_Fibre    = 0
cottageCheese.Grammes_Protein  = 11.12
cottageCheese.Grammes_Sugar    = 2.67
cottageCheese.MG_Calcium       = 83
cottageCheese.save()


print "\n\n#############################################"
print "Basic Ingredients"
print "------------------"

for i in BasicIngredient.objects.all ():
    print i
print "#############################################"

cupCottageCheese = ContainedIngredient ()
cupCottageCheese.save()
cupCottageCheese.ingredientState   = noIngredientState
cupCottageCheese.basicIngredient   = cottageCheese
cupCottageCheese.containerMeasure  = cupContainerMeasure
cupCottageCheese.gramsPerContainer = 210
cupCottageCheese.save()

cupGratedCarrot = ContainedIngredient ()
cupGratedCarrot.save()
cupGratedCarrot.ingredientState   = gratedIngredientState
cupGratedCarrot.basicIngredient   = carrot
cupGratedCarrot.containerMeasure  = cupContainerMeasure
cupGratedCarrot.gramsPerContainer = 110
cupGratedCarrot.save()

cupGratedCabbage = ContainedIngredient ()
cupGratedCabbage.save()
cupGratedCabbage.ingredientState   = gratedIngredientState
cupGratedCabbage.basicIngredient   = cabbage
cupGratedCabbage.containerMeasure  = cupContainerMeasure
cupGratedCabbage.gramsPerContainer = 70
cupGratedCabbage.save()

cupRaisins = ContainedIngredient ()
cupRaisins.save()
cupRaisins.ingredientState   = looseIngredientState
cupRaisins.basicIngredient   = raisins
cupRaisins.containerMeasure  = cupContainerMeasure
cupRaisins.gramsPerContainer = 145
cupRaisins.save()

tbspOliveOil = ContainedIngredient ()
tbspOliveOil.save()
tbspOliveOil.ingredientState   = looseIngredientState
tbspOliveOil.basicIngredient   = oliveOil
tbspOliveOil.containerMeasure  = tbspContainerMeasure
tbspOliveOil.gramsPerContainer = 13.5
tbspOliveOil.save()

print "\n\n#############################################"
print "Contained Ingredients"
print "------------------"

for i in ContainedIngredient.objects.all ():
    print i
print "#############################################"

bulgarianColeslawRecipe = Recipe (name = "Bulgarian Coleslaw")
bulgarianColeslawRecipe.servings = 1
bulgarianColeslawRecipe.save ()

PenneAlaArabiataColeslawRecipe = Recipe (name = "Penne a la Arabiata")
PenneAlaArabiataColeslawRecipe.servings = 1
PenneAlaArabiataColeslawRecipe.save ()

print "\n\n#############################################"
print "Receipe"
print "------------------"

for i in Recipe.objects.all ():
    print i
print "#############################################"

ingredient = RecipeIngredient ()
ingredient.save ()
ingredient.recipe = bulgarianColeslawRecipe
ingredient.containedIngredient = cupGratedCabbage
ingredient.quantity = 1
ingredient.save ()

ingredient = RecipeIngredient ()
ingredient.save ()
ingredient.recipe = bulgarianColeslawRecipe
ingredient.containedIngredient = cupGratedCarrot
ingredient.quantity = 1
ingredient.save ()

ingredient = RecipeIngredient ()
ingredient.save ()
ingredient.recipe = bulgarianColeslawRecipe
ingredient.containedIngredient = cupCottageCheese
ingredient.quantity = 0.75
ingredient.save ()

ingredient = RecipeIngredient ()
ingredient.save ()
ingredient.recipe = bulgarianColeslawRecipe
ingredient.containedIngredient = tbspOliveOil
ingredient.quantity = 2
ingredient.save ()

ingredient = RecipeIngredient ()
ingredient.save ()
ingredient.recipe = bulgarianColeslawRecipe
ingredient.containedIngredient = cupRaisins
ingredient.quantity = 0.25
ingredient.save ()

print "\n\n#############################################"
print "Ingredients"
print "------------------"

for i in RecipeIngredient.objects.all ():
    print i
    print i.nutritionValues ()
print "#############################################"

print "\n\n#############################################"
print "Receipe"

bulgarianColeslawRecipe = Recipe.objects.get (id=1)
print bulgarianColeslawRecipe.name
print bulgarianColeslawRecipe.nutritionValues ()
print "------------------"


