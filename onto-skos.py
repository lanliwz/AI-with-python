from owlready2 import *

onto_path.append("/Users/weizhang/ontology/repository")

onto = get_ontology("http://www.w3.org/TR/skos-reference/skos.rdf")

onto.load()
print("-------------classes------------------")
for cls in onto.classes():
    print(cls)
print("------------individuals-------------------")
for ind in onto.individuals():
    print(f"${ind} with ${ind.__class__}")

print("-------------------------------")
print("----------properties---------------------")
for ind in onto.properties():
    print(f"${ind} with ${ind.__class__}")

print("-------------------------------")
# class NonVegetarianPizza(onto.Pizza):
#     equivalent_to = [
#         onto.Pizza
#         & (onto.has_topping.some(onto.MeatTopping)
#            | onto.has_topping.some(onto.FishTopping)
#            )]
#
#     def eat(self): print("Hi! I'm vegetarian!")



onto.save()

