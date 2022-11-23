
let indexI = 0
let indexJ = 0
let id = "0.0"


let lessonList = []

function loadJson(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute('data-'))
}


var isObjectExist = function(search){
  return lessonList.find(function(obj){
     if(obj.course_name===search){
          return true;
     }
     return false;
  });
}

window.onload = function () {
  var dataArray = loadJson('#courseData')

 
  let listCont =  document.getElementById('enroll-course-list')
  for (let i = 0; i < dataArray.length; i++) {
    let list = document.createElement('li')
    list.innerHTML = dataArray[i].course_name
    list.style.marginLeft = '18px'
    list.style.listStyle = 'disc'
    list.style.cursor = 'pointer'

    list.addEventListener('click', () => {
      
      let clickedCourse = isObjectExist(dataArray[i].course_name)
      if (typeof clickedCourse === 'undefined') {
        let obj = {
          "course_name": dataArray[i].course_name,
          "videos": dataArray[i].urls
        }
        lessonList.pop()
        lessonList.push(obj)  
        renderCourse()
      }
      
      
    })
    listCont.appendChild(list)

  }
   
  if (lessonList.length == 0) {
    let obj = {
      "course_name": dataArray[0].course_name,
      "videos": dataArray[0].urls
    }
    lessonList.push(obj)
    renderCourse()
  }

  
}




function setVideo(link) {
  document.getElementById('vid').src = link

}

function renderCourse() {
  document.getElementById('mySidenav').innerHTML = ""
  document.getElementById('course-title').innerHTML = lessonList[0].course_name
  for (let i = 0; i < lessonList.length; i++) {

    let element = document.createElement('div')
    element.classList.add('wrap-div')
  
    for (let j = 0; j < lessonList[i].videos.length; j++) {
      let el = document.createElement('div')
      el.style.display = 'flex'
      el.style.alignItems = 'center'
      el.style.justifyContent = 'center'
      el.id = `${i}.${j}`
  
      let link = document.createElement('a')
      link.style.cursor = 'pointer'
      link.style.width = 'fit-content'
      link.textContent = `${i+1}.${j+1}`
      let tick = document.createElement('img')
      tick.src = '../static/img/kliponious-green-tick.png'
      tick.style.width = '25px'
      let disp = lessonList[i].videos[j].complete == true ? 'block' : 'none'
      tick.style.display = disp
      let tickWrp = document.createElement('div')
      tickWrp.style.width = '25px'
      tickWrp.appendChild(tick)
      el.appendChild(tickWrp)
      el.appendChild(link)
  
      
      link.addEventListener('click', () => {
           document.getElementById(id).childNodes[1].style.color = 'inherit'
           id = `${i}.${j}`
           indexI = i
           indexJ = j
          link.style.color = 'darkorange'
          setVideo(lessonList[i].videos[j])
      })
      element.appendChild(el)
    }
  
    document.getElementById('mySidenav').appendChild(element)
    setVideo(lessonList[0].videos[0])
  }
  
  document.getElementById(id).childNodes[1].style.color = 'darkorange'
  

}




function onComplete() {
  let cont =  document.getElementById(id)
  let tickwrp = cont.querySelector('div')
  let tick = tickwrp.querySelector('img')
  tick.style.display = 'block'
}

function onNext() {
  let newID = ""
  if (indexJ + 1 == lessonList[indexI].videos.length) {
    document.getElementById('vid').src = lessonList[indexI+1].videos[0].link
    newID = `${indexI+1}.${0}`
    indexI = indexI +1
    indexJ = 0
  } else {
    document.getElementById('vid').src = lessonList[indexI].videos[indexJ +1].link
    newID = `${indexI}.${indexJ + 1}`
    indexJ = indexJ + 1
  }
  document.getElementById(id).childNodes[1].style.color = 'inherit'
  document.getElementById(newID).childNodes[1].style.color = 'darkorange'
  id = newID
}


function onPrev() {
  if (id != '0.0') {
    let newID = ""
    if (indexJ - 1 < 0) {
      document.getElementById('vid').src = lessonList[indexI-1].videos[lessonList[indexI-1].videos.length-1].link
      newID = `${indexI-1}.${lessonList[indexI-1].videos.length-1}`
      indexI = indexI -1
      indexJ = lessonList[indexI].videos.length-1
    } else {
      document.getElementById('vid').src = lessonList[indexI].videos[indexJ -1].link
      newID = `${indexI}.${indexJ - 1}`
      indexJ = indexJ - 1
    }
    document.getElementById(id).childNodes[1].style.color = 'inherit'
    document.getElementById(newID).childNodes[1].style.color = 'darkorange'
    id = newID
  }
}
