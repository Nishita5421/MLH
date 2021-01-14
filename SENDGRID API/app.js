
var express=require("express");
var app=express();
var path = require('path');
var bodyParser=require("body-parser");

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));
const sgMail = require('@sendgrid/mail');
const API_KEY='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';
app.get("/",function(req,res)
{
res.render("email.ejs");
});

app.post("/",function(req,res){
  var frome=req.body.from;
  var toe=req.body.to;
  
  var subjecte=req.body.subject;
  var msge=req.body.msgs;
  sgMail.setApiKey(API_KEY);
const msg = {
  to: toe, // Change to your recipient
  from: frome, // Change to your verified sender
  subject: subjecte,
  //text: 'and easy to do anywhere, even with Node.js ,I did it with SENDGRID API if you are reading this then my project is complted ;)',
  html: msge,
}
sgMail
  .send(msg)
  .then(() => {
    console.log('Email sent')
    res.render("thankyou.ejs",{thankyou:'Email sent',error:null});
    
 
    
  })
  .catch((error) => {
    console.error(error)
    res.render("thankyou.ejs",{thankyou:'null',error:'There was some error!'});
 
  })
  


});
app.listen(4000,function(){
    console.log("Server has started");
})


