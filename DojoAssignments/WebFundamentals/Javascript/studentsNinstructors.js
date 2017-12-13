function myFunction(object){
  for(var i = 0; i < object.length; i++){
    console.log(object[i].first_name + " " + object[i].last_name);
  }
}

var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

myFunction(students);

function directory(object){
  console.log("Students");
  for(var i =0; i < object.Students.length; i++)console.log(i + 1 + " - " + object.Students[i].first_name.toUpperCase() + " " + object.Students[i].last_name.toUpperCase() + " - " + (object.Students[i].first_name + object.Students[i].last_name).length);
  console.log("Instructors");
  for(var i =0; i < object.Instructors.length; i++)console.log(i + 1 + " - " + object.Instructors[i].first_name.toUpperCase() + " " + object.Instructors[i].last_name.toUpperCase() + " - " + (object.Instructors[i].first_name + object.Instructors[i].last_name).length);
}

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

directory(users);
