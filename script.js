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
