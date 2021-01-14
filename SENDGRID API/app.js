const sgMail = require('@sendgrid/mail');
const API_KEY='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';

sgMail.setApiKey(API_KEY);
const msg = {
  to: 'kaustubh.ag5@gmail.com', // Change to your recipient
  from: 'nishipal121@gmail.com', // Change to your verified sender
  subject: 'Sending with SendGrid is Fun',
  text: 'and easy to do anywhere, even with Node.js ,I did it with SENDGRID API if you are reading this then my project is complted ;)',
  html: '<strong>and easy to do anywhere, even with Node.js ,I did it with SENDGRID API if you are reading this then my project is complted ;)</strong>',
}
sgMail
  .send(msg)
  .then(() => {
    console.log('Email sent')
  })
  .catch((error) => {
    console.error(error)
  })