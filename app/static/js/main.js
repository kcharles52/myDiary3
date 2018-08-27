let host_server = "http://127.0.0.1:5000"

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


//function to register user
function register_user() {
    let url = host_server+ "/api/v1/auth/signup";
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
    url = host_server + '/api/v1/auth/login'
    fetch(url, {
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
            if (reply['Message']==='Login failed, Please try again') {
                return alert(reply['Message'])
            } else{
                alert(reply['Message']);
                window.location= 'welcome.html';
            }
            return true;
        })
        .catch(error => alert(error))
}
function logout() {
    localStorage.removeItem('token');
    window.location.href = 'index.html';
}

function create_entry() {
    url = host_server + '/api/v1/entries'
    fetch(url,{
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
                'diaryTitle': document.getElementById('Title').value,
                'date': document.getElementById('date').value,
                'diaryEntryBody': document.getElementById('diaryMessage').value
            }),
        mode: 'cors',
        redirect: 'manual'

    })
        .then(Response => Response.json())
        .then(reply => {
            if (reply['Message'] === 'You have successfully created your entry') {
                alert(reply['Message'])
                window.location.href = 'diaryentries.html';
            } else if (reply['Message']) {
                alert(reply['Message']);
                console.log(reply)
            }
            return true;
        })
        .catch(error => alert(error))

}

function fetch_entries() {
    url = host_server + '/api/v1/entries'
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        redirect: 'manual'
        })
        .then(Response => Response.json())
        .then(data => {
            if (data['Message'] === 'Successfully fetched entries') {
                let output = `
                        <table>
                            <tr>
                            <th> Date </th> <th> Title </th> <th> Category </th> <th> Action </th>
                            </tr> `;

                data['entries'].forEach((entry) => {
                    output +=`
                    <tr class="ceremony">
                    <td>${entry.Date}</td>
                    <td><a href="">${entry.title}</a></td>
                    <td>ceremony</td>
                    <td class="action"><a href="#">Edit</a><a href="#">Archive</a></td>
                    </tr>
                    `
                });
                output += `</table>`;

               document.getElementById('AllEntries').innerHTML = output;
                console.log(data);

            } else if (data['Message']) {
                alert(data['Message']);
                console.log(data)
            }
            return true;
        })
        .catch(error => alert(error))
    }

