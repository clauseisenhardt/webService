function changeParagraph() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
function demo2() {
    document.getElementById("demo2").innerHTML = 5 + 6;
}

function PathFetch(req, init, id)
{
  fetch(req, init) 
  .then(
      function(response) {
        console.log(response);
        if (response.status !== 200) {
          console.log('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }
  
        // Examine the text in the response
        response.json().then(function(data) {
          console.log(data);
      
          var fileList = JSON.parse(data);
          var i;
          for (i = 0; i < fileList.length; i++)
            document.getElementById(id).innerHTML += (i+1) + ": " + fileList[i] + "<br /> ";
  
          console.log(fileList);
        });
  
        }
    )
    .catch(function(err) {
      console.log('Path fetch Error :-S', err);
    });
  
}