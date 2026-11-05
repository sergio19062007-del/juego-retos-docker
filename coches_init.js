db = db.getSiblingDB("concesionario");
db.coches.insertMany([
  { id: 1,  marca: "Toyota",     modelo: "Corolla", color: "Blanco", km: 45000, precio: 15000 },
  { id: 2,  marca: "Honda",      modelo: "Civic",   color: "Negro",  km: 60000, precio: 17000 },
  { id: 3,  marca: "Ford",       modelo: "Focus",   color: "Azul",   km: 50000, precio: 14000 },
  { id: 4,  marca: "Chevrolet",  modelo: "Malibu",  color: "Rojo",   km: 70000, precio: 16000 },
  { id: 5,  marca: "Nissan",     modelo: "Sentra",  color: "Gris",   km: 55000, precio: 15500 },
  { id: 6,  marca: "Volkswagen", modelo: "Jetta",   color: "Blanco", km: 40000, precio: 16500 },
  { id: 7,  marca: "Hyundai",    modelo: "Elantra", color: "Negro",  km: 45000, precio: 14500 },
  { id: 8,  marca: "Kia",        modelo: "Rio",     color: "Azul",   km: 30000, precio: 13500 },
  { id: 9,  marca: "Mazda",      modelo: "Mazda3",  color: "Rojo",   km: 48000, precio: 15800 },
  { id: 10, marca: "Seat",       modelo: "Leon",    color: "Gris",   km: 53000, precio: 16800 },
  { id: 11, marca: "BMW",        modelo: "Serie 3", color: "Blanco", km: 75000, precio: 28000 },
  { id: 12, marca: "Audi",       modelo: "A4",      color: "Azul",   km: 69000, precio: 29000 }
]);