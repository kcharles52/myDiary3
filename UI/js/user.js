let host_server = "http: //127.0.0.1:5000"
//function to register user
function register_user() {
    let url = host_server + "/api/v1/auth/signup";
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "name": document.getElementById("FName").value + " "+ document.getElementById("LName"),
                "email": document.getElementById("email").value,
                "password": document.getElementById("password").value
            })
        })
        .then(function (response) {
            return response.json();
        })
        .catch(function (error) {
            console.log(error);
        });
}