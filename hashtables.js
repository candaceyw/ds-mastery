let user = {
  age: 54,
  name: 'Kylie',
  magic: true,
  scream: function () {
    console.log('ahhhhhh');
  },
};

user.age; // O(1)
user.spell = 'abra kadabra'; // O(1)
user.scream(); //O(1)

// https://www.cs.usfca.edu/~galles/visualization/OpenHash.html Open hashing visualization tool

// Hashtable examples
const a = new Map();
const b = new Sets();
