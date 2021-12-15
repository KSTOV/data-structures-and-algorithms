from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dog, Cat, Cow

def test_dog():
    assert Dog

def test_cat():
    assert Cat

def test_animal_shelter():
    assert AnimalShelter

def test_animal_shelter_enqueue():
    shelter = AnimalShelter()
    dog = Dog()
    cat = Cat()
    cow = Cow()

    shelter.enqueue(dog)
    assert shelter.enqueue(dog) == True
    shelter.enqueue(cat)
    assert shelter.enqueue(cat) == True

    assert shelter.enqueue(cow) == False

def test_animal_shelter_dequeue():
    shelter = AnimalShelter()
    dog = Dog()
    cat = Cat()
    cow = Cow()

    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue(dog)
    shelter.dequeue(cat)
    assert shelter.dequeue(dog) == True
    assert shelter.dequeue(cat) == True
    assert shelter.dequeue(cow) == False

def test_animal_shelter_enqueue_multi():
    shelter = AnimalShelter()
    dog = Dog()
    cat = Cat()
    cow = Cow()

    shelter.enqueue(dog)
    shelter.enqueue(dog)
    shelter.enqueue(dog)
    assert shelter.enqueue(dog) == True

    shelter.enqueue(cat)
    shelter.enqueue(cat)
    shelter.enqueue(cat)
    assert shelter.enqueue(cat) == True

    assert shelter.enqueue(cow) == False

def test_animal_shelter_dequeue_multi():
    shelter = AnimalShelter()
    dog = Dog()
    cat = Cat()
    cow = Cow()

    shelter.enqueue(dog)
    shelter.enqueue(dog)
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.enqueue(cat)
    shelter.enqueue(cat)
    shelter.dequeue(dog)
    shelter.dequeue(cat)
    assert shelter.dequeue(dog) == True
    assert shelter.dequeue(cat) == True
    assert shelter.dequeue(cow) == False
