class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):                  
            pet.set_owner(self)
            self._pets.append(pet)
            pet.owner= self
        else:
            raise Exception('Pet must be an instance of Pet class')

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type. Valid types are: {', '.join(Pet.PET_TYPES)}")
        self.set_owner(owner)
        self.owner = owner
        Pet.all.append(self)


    
    def set_owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise TypeError('Owner must be an instance of Owner class')
        self._owner = owner
        
    


