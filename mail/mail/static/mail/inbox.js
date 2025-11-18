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

    const emailsView = document.querySelector('#emails-view');

    emailsView.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


    let emailList = document.getElementById('email-list');

      if (!emailList) {

        emailList = document.createElement('ul');

        emailList.id = 'email-list';

        emailsView.appendChild(emailList);

      }


    fetch(`/emails/${mailbox}`)

    .then(response => response.json())

    .then(emails => {

      // Print emails

      console.log(emails);



      const emailList = document.getElementById('email-list');

      emailList.innerHTML = '';



      emails.forEach(email => {



        const emailItem = document.createElement('li');

        emailItem.innerHTML = `

        <div class="email">

        <strong>From:</strong> ${email.sender}<br>

        <strong>Subject:</strong> ${email.subject}<br>

        </div>

        <div class="button">

          <input type="submit" class="archive" value="${email.archived ? "Unarchive" : "Archive"}">

        </div>

        `;

        emailItem.querySelector('.email').addEventListener('click', () => {

        check_email(email.id, email.read, mailbox);

        })



        emailItem.querySelector('.archive').addEventListener('click', () =>{

          archive_email(email.id, email.archived, mailbox);

        })



        if (email.read == true){

          emailItem.querySelector('.email').style.backgroundColor = '#77dd11';

        }



        emailList.appendChild(emailItem);

      })


    })



    .catch(error => {

      console.error("Error getting emails",error);

    });

  }

  function check_email(emailMessage, emailRead){


    fetch(`/emails/${emailMessage}`, {

      method: 'PUT',

      body: JSON.stringify({

        read: !emailRead

      })

    });

    fetch(`/emails/${emailMessage}`)
    .then(response => response.json())

    .then(email => {

        // Print email

        console.log(email);

      if (emailRead == false){



        document.querySelector('#emails-view').style.display = 'none';

        document.querySelector('#compose-view').style.display = 'none';

        document.querySelector('#email-view').style.display = 'block';



        const emailItem = document.createElement('li');

        emailItem.innerHTML = `

          <div class="email">

            <strong>From:</strong> ${email.sender}<br>

            <strong>Subject:</strong> ${email.subject}<br>

            <strong>Recipients:</strong> ${email.recipients}</br>

            <strong>Tiomestamp:</strong> ${email.timestamp}</br>

            <strong>Body:</strong> ${email.body}

          </div>`;



        const emailView = document.querySelector('#email-view');

        emailView.innerHTML = ""; // Clear any previous content

        emailView.appendChild(emailItem);



        emailItem.querySelector('.email').addEventListener('click', () => {

          load_mailbox('inbox');

        });

      }



        // ... do something else with email ...

    })



    .catch(error => {

      console.error("Error getting email");

    });

  }



  function archive_email(emailId, isArchived, currentMailbox){


    fetch(`/emails/${emailId}`, {

      method: 'PUT',

      body: JSON.stringify({

          archived: !isArchived

      })

    })

    .then(() =>{

      load_mailbox(currentMailbox);

    });

  }

});



// pending check email