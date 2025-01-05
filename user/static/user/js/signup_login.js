host = 'http://127.0.0.1:8000'

document.getElementById('signupForm').addEventListener('submit', function (event) {
    event.preventDefault();

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;
    let password = document.getElementById('signupPassword').value;
    let confirmPassword = document.getElementById('confirmPassword').value;
    let message = document.getElementById('message');
    let passwordError = document.getElementById('passwordError');
    let confirmPasswordError = document.getElementById('confirmPasswordError');

    let passwordValid = validatePassword(password);
    if (!passwordValid) {
        passwordError.textContent = 'Password does not meet the requirements.';
        return;
    } else {
        passwordError.textContent = '';
    }

    if (password !== confirmPassword) {
        confirmPasswordError.textContent = 'Passwords do not match!';
        return;
    } else {
        confirmPasswordError.textContent = '';
    }

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let data = {username:username, password:password, Email:email, phone:phone};
    let url = host+'/user_page/';

    const config = {
        method: "POST",
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    }

   return fetch(url, config)
   .then(response => response.json())
   .then(response => {
         if (response.success) {
            message.style.color = 'green';
            message.textContent = response.message;
         }else{
            message.style.color = 'red';
            message.textContent = response.message;
         }
   })
});

document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();

    let username = document.getElementById('loginUsername').value;
    let password = document.getElementById('loginPassword').value;

    let data = {username:username, password:password};
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let url = host+'/user_page/'+username;
    const config = {
        method: "POST",
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    }

    return fetch(url, config)
   .then(response => response.json())
   .then(response => {
         if (response.success) {
             console.log(response.url)
            location.replace(host+response.url) ;
         }else{
            loginMessage.style.color = 'red';
            loginMessage.textContent = response.message;
         }
   })
});



        // document.getElementById('signupPassword').addEventListener('focus', function () {
        //     document.getElementById('passwordHint').style.display = 'block';
        // });
        //
        // document.getElementById('signupPassword').addEventListener('blur', function () {
        //     document.getElementById('passwordHint').style.display = 'none';
        // });
        //
        // document.getElementById('signupPassword').addEventListener('input', function () {
        //     let password = this.value;
        //     let passwordStrength = document.getElementById('passwordStrength');
        //     let strength = getPasswordStrength(password);
        //
        //     passwordStrength.innerHTML = ''; // Clear previous strength bars
        //     if (strength) {
        //         let strengthBar = document.createElement('div');
        //         strengthBar.className = strength;
        //         passwordStrength.appendChild(strengthBar);
        //     }
        // });

        function validatePassword(password) {
            let regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
            return regex.test(password);
        }

        function getPasswordStrength(password) {
            if (password.length < 8) {
                return 'weak';
            }
            if (password.match(/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])/)) {
                return 'strong';
            }
            return 'medium';
        }