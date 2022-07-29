function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
  }
function alertfun(){
  alert('you have pressed button!');
}
function writefun(){
  document.write("writing into document");
}
function toprint(){
  window.print();
}
function stater(){
  a=1;
  b=2;
  c=a+b;
  return c;
}
function tochange(){
  q=stater();
  document.getElementById("o").innerHTML = q;
  console.log(q);
}
class scriptclass{
     constructor(name,age)
     {
      this.name=name;
      this.age=age;
     }

}
class getset{
  constructor(a)
  {
    this.f=a;
  }
  set fa(d)
  {
    g= this.f+d;
    return g;
  }
  get fa()
  {
    return this.f;
  }
}
function homepage(){
  window.location.href="page1.html";
  return false;
}
function num() {
  const inpObj = document.getElementById("id1");
  if (!inpObj.checkValidity()) {
    document.getElementById("demo").innerHTML = inpObj.validationMessage;
  } else {
    document.getElementById("demo").innerHTML = "Input OK";
  } 
} 


function fordata() {
    // var x = document.getElementById("asd");
    // var text1 = "";
    // var i;
    // for (i = 0; i < x.length ;i++) {
    //   text1 += x.elements[i].value + "<br>";
    // }
    // document.getElementById("em").innerHTML = text1;
    // console.log(text1);
    // let result=text1.replace('<br>', '');;
    fetch ($("#asd").val())
    .then(x => x.text())
    .then(y => document.getElementById("mo").innerHTML = y);
  }


function et(file_name){
  
  fetch (file_name)
  .then(x => x.text())
  .then(y => document.getElementById("mo").innerHTML = y);

}
$(document).ready(function(){
  $("#er").click(function(){
    $("#er").hide();
  });
  $("#tr").hover(function(){
    $("#tr").css("background-color", "yellow")
  });
  $("#tr").mouseleave(function(){
    $("#tr").css("background-color", "white")
  });
  $("#fom").click(function(){
    const fs = require('fs')
    console.log($("#firstName").val())
    fs.writeFile('info.txt',$("#firstName").val() , (err) => {
        
      // In case of a error throw err.
      if (err) throw err;
  })
  fs.writeFile('info.txt',$("#lastName").val() , (err) => {
        
    // In case of a error throw err.
    if (err) throw err;
  })
  
    
  
   
  });

});





////////////////
var xhr = null;
var name;
$(document).ready(function(){
  
  $("#us").click(function(){
    name=$("#newuser").val()
    addUsers();

  });
});

    getXmlHttpRequestObject = function () {
        if (!xhr) {
            // Create a new XMLHttpRequest object 
            xhr = new XMLHttpRequest();
        }
        return xhr;
    };
    function dataCallback() {
        // Check response is ready or not
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log("User data received!");
            getDate();
            
            dataDiv = document.getElementById('data');
            // Set current data text
            dataDiv.innerHTML = xhr.responseText;
        }
    }
    function getUsers() {
        console.log("Get users...");
        xhr = getXmlHttpRequestObject();
        xhr.onreadystatechange = dataCallback;
        // asynchronous requests
        xhr.open("GET", "http://127.0.0.1:8000/gettxtenterdata", true);
        // Send the request over the network
        xhr.send(null);
    }
    function addUsers() {

      console.log("adding users...");
      xhr = getXmlHttpRequestObject();
      // xhr.onreadystatechange = dataCallback;
      // asynchronous requests
    
      xhr.open("POST","http://127.0.0.1:8000/enterdata?name="+name, true);
      // Send the request over the network
      xhr.send(null);
  }
    function getDate() {
        date = new Date().toString();
        document.getElementById('time-container').textContent
            = date;
    };




