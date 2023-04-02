const express = require('express');
const multer = require('multer');
const app = express();
// const rembut=document.getElementById('removing');
const storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, 'images/');
  },
  filename: function(req, file, cb) {
    cb(null,'input.png');
  }
});

const upload = multer({ storage: storage });

app.use(express.static('public'));

app.post('/upload', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ message: 'No image file uploaded' });
  }
  console.log("Image saved");


  const {exec} =require('child_process');
  const { error } = require('console');
  const { stdout, stderr } = require('process');

  exec('python demo.py',(error,stdout,stderr)=>{
      if(error){
          console.log(`error: ${error.message}`);
          return;
      }
      if(stderr){
          console.log(`stderr: ${stderr}`);
          return;
      }
      console.log(`stdout: ${stdout}`);
  })
  console.log("Shadow removed");
  res.status(200).json({ message: '' });
  
});


app.post('/uploadblur', upload.single('images'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ message: 'No image file uploaded' });
  }
  console.log("Images saved");


  const {exec} =require('child_process');
  const { error } = require('console');
  const { stdout, stderr } = require('process');

  exec('python test.py',(error,stdout,stderr)=>{
      if(error){
          console.log(`error: ${error.message}`);
          return;
      }
      if(stderr){
          console.log(`stderr: ${stderr}`);
          return;
      }
      console.log(`stdout: ${stdout}`);
  })
  
 
  console.log("Blur Detected");
  
  res.status(200).json({ message: `` });
  
});



app.get('/', function(req, res) {
  res.sendFile( __dirname+'/start.html');
});
app.get('/shadow', function(req, res) {
  res.sendFile( __dirname+'/shadow.html');
});
app.get('/blur', function(req, res) {
  res.sendFile( __dirname+'/blur.html');
});
app.get('/removed', function(req, res) {
  res.sendFile( __dirname+'/index2.html');
});
app.get('/detected', function(req, res) {
  res.sendFile( __dirname+'/index3.html');
});
app.get('/texttodisplay', function(req, res) {
  res.sendFile( __dirname+'/output.txt');
});
app.get('/styles', function(req, res) {
  res.sendFile( __dirname+'/styles.css');
});
app.get('/script', function(req, res) {
  res.sendFile( __dirname+'/script.js');
});
app.get('/scriptblur', function(req, res) {
  res.sendFile( __dirname+'/scriptblur.js');
});
app.get('/server', function(req, res) {
  res.sendFile( __dirname+'/server.js');
});
app.get('/displaypic', function(req, res) {
  res.sendFile( __dirname+'/images/img1.png');
});

app.get('/input', function(req, res) {
  res.sendFile( __dirname+'/images/input.png');
});
app.get('/output', function(req, res) {
  res.sendFile( __dirname+'/images/output.png');
});
app.listen(3000, () => console.log('Server started on port 3000'));
