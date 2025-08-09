animal = input()
switch_animal = {
    "dog": "manmal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile",
}
print(switch_animal.get(animal, "unknown"))