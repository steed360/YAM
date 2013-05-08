# execfile ("testmodels.py")
# python manage.py sqlclear yam | python manage.py dbshell
# python manage.py syncdb

import yam.models as m

seafood = m.IngredientCategory (name = "seafood")
seafood.save()
vegetables = m.IngredientCategory (name = "vegetables")
vegetables.save()

cup = m.ContainerMeasure (name="cup")
cup.save ()

cup = m.ContainerMeasure (name="handful")
cup.save ()

chopped = m.IngredientState (state="chopped")
chopped.save()

diced = m.IngredientState (state="diced")
diced.save ()

cucumber = m.BasicIngredient (name="cucumber")
cucumber.ingredientCategory = vegetables
cucumber.Grammes_Fat = 1
cucumber.save ()

#cucumber.permittedStates.add (chopped)
#cucumber.permittedStates.add (diced)
#cucumber.save ()

fish = m.BasicIngredient (name="fish")
fish.ingredientCategory = seafood
fish.Grammes_Fat = 5
fish.save ()

#fish.permittedStates.add (chopped)
#fish.save ()

cucumberInCup =  m.ContainedIngredient ()
cucumberInCup.ingredientState = chopped
cucumberInCup.basicIngredient = cucumber
cucumberInCup.containerMeasure= cup
cucumberInCup.gramsPerContainer= 100
cucumberInCup.save ()

cupFish =  m.ContainedIngredient ()
cupFish.ingredientState = chopped
cupFish.basicIngredient = fish
cupFish.containerMeasure= cup
cupFish.gramsPerContainer= 2
cupFish.save ()

sushi = m.Recipe (name = "sushi")
sushi.save ()

addCupCucumber = m.RecipeIngredient ()
addCupCucumber.recipe = sushi
addCupCucumber.containedIngredient = cupFish
addCupCucumber.numberContainers = 0.5
addCupCucumber.save ()

print m.RecipeIngredient.objects.all()[0].ingredientGrams ()


