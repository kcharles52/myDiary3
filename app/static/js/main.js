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
    let Fullname = document.getElementById('FName').value + " " + document.getElementById('LName').value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    fetch(url, {
            method: 'POST',
            mode: 'cors',
            redirect:'manual',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "name": Fullname,
                "email": email,
                "password": password
            })
        })
        .then(function (response) {
            return response.json();
        })
        .then(function(data){
            console.log(data);
           if(data['status']==='success'){
               alert(data['message'])
               window.location.href="index.html"
           }else{
               alert(data['message'])
           }
        })
        .catch(function (error) {
            console.log(error);
        });
}
function login() {
    let email = document.getElementById('logEmail').value
    let password = document.getElementById('password').value
    let  url = host_server + '/api/v1/auth/login'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'email': email,
            'password': password
        }),
        mode: 'cors',
        })
        .then(Response => Response.json())
        .then(reply => {
            if (reply['Message']==='Login failed, Please try again') {
                return alert(reply['Message'])
            } else if (reply['status'] ==='success'){
                location.href = 'welcome.html';
            }
        })
        .catch(error => alert(error))
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = 'index.html';
}

function create_entry() {
   let url = host_server + '/api/v1/entries'
    let Title = document.getElementById('Title').value;
    let date = document.getElementById('date').value;
    let Body = document.getElementById('diaryMessage').value;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify({
            'diaryTitle': Title,
            'date': date,
            'diaryEntryBody': Body
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
                    <td> <a href = "/diaryentry.html/${entry.id}"> ${entry.title} </a></td >
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

function fetch_entry(id) {
    url = host_server + '/api/v1/entries/'+id
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
            if (data['Message'] === 'Successfully fetched entry') {
               output =`
               <div class="dHeader">
                    <h2> ${data['entry']['Date']}</h2>
                    <h2>${data['entry']['title']}</h2>
                </div>
                <div class="dBody" >
                    <p>${data['entry']['Diary Body']}</p>
                    <br>
                    <div class="action"> <a href="modifyentry.html">Edit</a> <a href="#">Archive</a>
                </div> `
                document.getElementById('diaryEntry').innerHTML = output;
                return output;
            } else if (data['Message']) {
                alert(data['Message']);
                console.log(data)
            }

        })
        .catch(error => alert(error))
}
