console.log('f')
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

    let data = {username:username, password:password, Email:email, phone:phone};
    let url = 'http://127.0.0.1:8000/user_page/';

    const config = {

        method: "POST",

        headers: {
            'Content-Type':'application/json'

        },

        body: JSON.stringify(data)

    }

   return fetch(url, config)
   .then((response) => {
         if (!response.ok) {
            message.style.color = 'red';
            message.textContent = 'Signup fail!';
         }
         return response.text();
   })
  .then((text) => {
        message.style.color = 'green';
        message.textContent = 'Signup successful!';
   })
  .catch((error) => {
        message.style.color = 'green';
        message.textContent = error;
  });
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