let string = "";

let buttons = document.querySelectorAll('.button')

Array.from(buttons).forEach((button) => {

    button.addEventListener('click', (e) => {

        buttonText = e.target.innerText;
        console.log('Button text is ', buttonText);
        if (e.target.innerHTML == '=') {
            string = eval(string)
            document.querySelector('.resultscreen').value = string;


        }else if(e.target.innerHTML== 'C'){
            document.querySelector('input').value = ""
        }
        else if(e.target.innerText == 'AC'){
            document.querySelector('input').value = ""
            document.querySelector('.resultscreen').value = ""
            string=""

        }
        else {
            console.log(e.target)
            string = string + e.target.innerHTML;
            document.querySelector('.input').value = string;
        }

    })


})