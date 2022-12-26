superPowers=['flight', 'cool cape', '20/20 vision', 'Coding Skillz']
superWeaknesses=['bologna', 'lactose intolerance', 'social settings', 'tight trunks']
del superWeaknesses[1]
superWeaknesses.append('Taco Meat')
print("Behold our fledgling hero/sidekick, \"WonderBoy")
print("His superpowers include:", *superPowers)
print("And his weaknesses are:", *superWeaknesses)