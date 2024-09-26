dinosaurs = {
    "Tyrannosaurus Rex": "North America",
    "Stegosaurus": "North America",
    "Triceratops": "North America",
    "Brachiosaurus": "North America",
    "Velociraptor": "Mongolia",
    "Ankylosaurus": "North America",
    "Diplodocus": "North America"
}

print("a. Entire dictionary:", dinosaurs)

print("b. Location of the 4th dinosaur's fossils:", dinosaurs["Brachiosaurus"])

dinosaurs["Stegosaurus"] = "Europe"

del dinosaurs["Ankylosaurus"]

print("c. Updated dictionary:", dinosaurs)

last_key = list(dinosaurs.keys())[-1]
last_value = dinosaurs[last_key]

print("d. Last key-value pair in the dictionary:", last_key, last_value)