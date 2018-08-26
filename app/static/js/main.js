//Switch tabs on the home page
function switchTab(evt, tabName) {
    var classes = document.getElementsByClassName('tab')
    switch (tabName) {
        case 'login':
            document.getElementById(tabName).style.display = "block";
            document.getElementById('signup').style.display = "none";
            classes[1].className = classes[0].className.replace(' active', '');
            classes[0].className += ' active';
            break;

        case 'signup':
            document.getElementById(tabName).style.display = "block";
            document.getElementById('login').style.display = "none";
            classes[0].className = classes[0].className.replace(' active', '');
            classes[1].className += ' active';
            break;

    }

}



//get active tab content
// var activeTab = document.getElementsByClassName("activeTab")
// activeTab[0].style.display="block"

function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks,currentTab;
    activeTab = document.getElementsByClassName("activeTab")

    activeTab[0].className = activeTab[0].className.replace("activeTab","tabcontent")

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");

    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    currentTab = document.getElementById(tabName);
    currentTab.style.display = "block";
    currentTab.className = className.replace("tabcontent","activeTab");
    evt.currentTarget.className += " active";

}

// let host_server = "http://127.0.0.1:5000"
//function to register user
function register_user() {
    let url = "http://127.0.0.1:5000/api/v1/auth/signup";
    let Fullname = document.getElementById('FName').value + " " + document.getElementById('LName').value
    fetch(url, {
            method: 'POST',
            mode: 'cors',
            redirect:'manual',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "name": Fullname,
                "email": document.getElementById("email").value,
                "password": document.getElementById("password").value
            })
        })
        .then(function (response) {
            return response.json();
        })
        .then(function(data){
           if(true){
               alert(data['message'])
               window.location.href="index.html"
           }
        })
        .catch(function (error) {
            console.log(error);
        });
}
function login() {
    fetch('http://127.0.0.1:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'email': document.getElementById('logEmail').value,
            'password': document.getElementById('password').value
        }),
        mode: 'cors',
        redirect: 'manual'
    })
        .then(Response => Response.json())
        .then(reply => {
            if (!reply['Message']) {
                let key = 'token';
                let value = reply['token'];
                localStorage.setItem(key, value);
                console.log(localStorage.getItem('token'));
                window.location.href = 'welcome.html';
            } else if (reply['Message']) {
                return alert(reply['Message'])
            }
            return true;
        })
        .catch(error => alert(error))
}