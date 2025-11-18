document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

  const composeForm = document.querySelector('#compose-form');



  composeForm.addEventListener('submit', (event) => {

    event.preventDefault(); //preventing default submission



    const recipients = document.querySelector('#compose-recipients').value;

    const subject = document.querySelector('#compose-subject').value;

    const body = document.querySelector('#compose-body').value;



    fetch('/emails', {

      method: 'POST',

      body: JSON.stringify({

      recipients,

      subject,

      body

      })

    })



    .then(response => response.json())

    .then(result => {



      if (result.error){

        console.error(result.error);

      }

      else {

        console.log("Email sent succesfully");

        document.querySelector('#compose-recipients').value = '';

        document.querySelector('#compose-subject').value = '';

        document.querySelector('#compose-body').value = '';

      }

    })



    .catch(error => {

      console.error("Error sending email", error);

    });



  });


  function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  }

  function load_mailbox(mailbox) {
    
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


    fetch('/emails/${mailbox}')

    .then(response => response.json())

    .then(emails => {

      // Print emails

      console.log(emails);



      const emailList = document.getElementById('email-list');

      emailList.innerHTML = '';



      emails.forEach(email => {



        const emailItem = document.createElement('li');

        emailItem.innerHTML = `



        <strong>From:</strong> ${email.sender}<br>

        <strong>Subject:</strong> ${email.subject}

        `;



        emailList.appendChild(emailItem);

      })


    })



    .catch(error => {

      console.error("Error getting emails");

    });

  }

});

