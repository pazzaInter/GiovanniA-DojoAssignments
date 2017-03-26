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

function printNames(obj) {
    for (var i = 0; i < Object.keys(obj).length; i++) {
        console.log(Object.keys(obj)[i]);
        var usersList = obj[Object.keys(obj)[i]];
        for (var j = 0; j < usersList.length; j++) {
            var f_name_l = usersList[j].first_name.length;
            var l_name_l = usersList[j].last_name.length;
            var name_length = f_name_l+l_name_l;
            console.log(j+1 + " - " + usersList[j].first_name.toUpperCase(), usersList[j].last_name.toUpperCase() + " - " + name_length);
        }
    }
}

printNames(users);
