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
    var x = document.getElementById("abc");
    var text1 = "";
    var i;
    for (i = 0; i < x.length ;i++) {
      text1 += x.elements[i].value + "<br>";
    }
    document.getElementById("em").innerHTML = text1;
    console.log(text1);
    let result=text1.replace('<br>', '');;
    fetch (result)
    .then(x => x.text())
    .then(y => document.getElementById("mo").innerHTML = y);
  }


function et(file_name){
  
  fetch (file_name)
  .then(x => x.text())
  .then(y => document.getElementById("mo").innerHTML = y);

}