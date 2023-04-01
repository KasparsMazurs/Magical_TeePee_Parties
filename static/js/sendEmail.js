function sendMail(contactForm) {
    emailjs.send('Gmail', 'Magical_TeePee_Parties', {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "request": contactForm.summary.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            $('.alert').show();
        },
        function(error) {
            console.log("FAILED", error);
    });
    
    return false; // Prevent the default form submission behavior
    
    }