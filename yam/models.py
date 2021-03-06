# John Steedman, Sunday 17 March 2013

# A basic representation of the measures and nutrient value
# of ingredients in a recipe. Will be populated with some 
# of the information in the following dataset 
# http://www.ars.usda.gov/Services/docs.htm?docid=22771

# The only continuous measure supported is
# 'gram'. But for usability "container
#  measures" are also used, such as 'handful', 'cup'

from django.db import models

class ContainerMeasure (models.Model):

    # E.g.Cup, Handful, Tablespoon etc

    name               = models.CharField (max_length = 20 )

    def __unicode__(self):
        return self.name 

class IngredientCategory  (models.Model):

   name            = models.CharField (max_length = 20 )

   def __unicode__(self):
       return self.name

class IngredientState ( models.Model ):

    #TODO add in possible states for each ingredient...
#    This model represents the type of ingredient dealt with
#    Anticipated instances are : "chopped", "grated", "whole unit". 
#    It currently assumed that all ingredients are unprepared/raw 

    state =models.CharField (max_length = 20 )
    subState =models.CharField (max_length = 20, blank=True, null=True)

    def __unicode__(self):
        if self.subState == None:
            return self.state
        else:
            return self.state + "," + self.subState

class BasicIngredient (models.Model):

#    This model represents a basic food ingredient
#    E.g. sugar, carrot, pork

    name                     = models.CharField (max_length = 20 )
    permittedStates          = models.ManyToManyField ( IngredientState, null=True)
    ingredientCategory       = models.ForeignKey(IngredientCategory, null=True)
    referenceQuantityInGrams = models.IntegerField(default=100, null=True)
    Grammes_Fat              = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 
    Grammes_Carbs            = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 
    Grammes_Fibre            = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 
    Grammes_Protein          = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 
    Grammes_Sugar            = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 
    MG_Calcium               = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 



    def __unicode__(self):
        return self.name

class ContainedIngredient (models.Model):

    # e.g. chopped/unit/grated/sliced etc 
    ingredientState             = models.ForeignKey (IngredientState , null = True )
    basicIngredient             = models.ForeignKey(BasicIngredient, null = True)
    containerMeasure            = models.ForeignKey(ContainerMeasure, null = True)
    gramsPerContainer           = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 

    def __unicode__(self):
        return self.containerMeasure.name + " of " + self.ingredientState.state  + " " + self.basicIngredient.name

class Recipe  (models.Model):

    name            = models.CharField (max_length = 40 )
    description     = models.CharField (max_length = 200 )
    servings        = models.IntegerField(default=1)

    def nutritionValues (self):
        recipeIngredients = self.recipeingredient_set.all ()

        result =  { "fat"     :  0, \
                    "carbs"   :  0, \
                    "fibre"   :  0, \
                    "protein" :  0, \
                    "sugar"   :  0, \
                    "calcium" :  0   }

        for thisRI in recipeIngredients:
            thisRINut = thisRI.nutritionValues ()
            result ["fat"]     += thisRINut ["fat"]            
            result ["carbs"]   += thisRINut ["carbs"]            
            result ["fibre"]   += thisRINut ["fibre"]            
            result ["protein"] += thisRINut ["protein"]            
            result ["sugar"]   += thisRINut ["sugar"]            
            result ["calcium"] += thisRINut ["calcium"]            

        return result 

    def __unicode__(self):
        return self.name


class RecipeIngredient (models.Model):

  # TODO : need to find a way to use ingredients without a container
  recipe                   = models.ForeignKey   ( Recipe, null=True)
  containedIngredient      = models.ForeignKey   ( ContainedIngredient, null=True)
  quantity                  = models.DecimalField ( max_digits = 5, decimal_places=2, null=True ) 

  def ingredientGrams (self):
      gramsPerContainer = self.containedIngredient.gramsPerContainer
      return float( gramsPerContainer * self.quantity)

  def nutritionValues (self):

       ing      = self.containedIngredient.basicIngredient
       grams    = self.ingredientGrams ()
       refGrams = ing.referenceQuantityInGrams 
       prop     = grams / refGrams

       return { "fat"      :  prop * float(ing.Grammes_Fat)     ,   \
                "carbs"    :  prop * float(ing.Grammes_Carbs)   ,   \
                "fibre"    :  prop * float(ing.Grammes_Fibre)   ,   \
                "protein"  :  prop * float(ing.Grammes_Protein) ,   \
                "sugar"    :  prop * float(ing.Grammes_Sugar)   ,   \
                "calcium"  :  prop * float(ing.MG_Calcium) }

  def __unicode__(self):
      return str(self.quantity) + " " + self.containedIngredient.__unicode__() + " is " + \
             str (self.ingredientGrams () ) + " grams "


