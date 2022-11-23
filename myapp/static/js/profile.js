let imageUrl = document.getElementById('image').src

function onEdit() {
  let buttoncontainer = document.getElementById('btnDiv')
  buttoncontainer.style.display = 'flex'
  let inpts = document.getElementsByTagName('input')
  for (let i = 0; i < inpts.length-2; i++) {
      inpts[i].disabled = false
  }
  document.getElementById('address').disabled = false
  document.getElementById('photo').style.display = 'inline-block'
  document.getElementById('add').style.display = 'inline-block'
}






function uploadImage(file) {
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
    localStorage.setItem("image", reader.result);
    document.getElementById("image").setAttribute("src", localStorage.getItem("image"))
    };
}

function onAddPhoto() {
    let photo = document.getElementById('photo').files[0]
    uploadImage(photo)    
}

function onCan() {
  let inpts = document.getElementsByTagName('input')
  for (let i = 0; i < inpts.length-2; i++) {
      var x =inpts[i].defaultValue
      console.log(x)
      inpts[i].value = x
  }

  document.getElementById('image').src = imageUrl

}