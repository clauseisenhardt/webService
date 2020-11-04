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
function PathFetch2(req, init, id)
{
  var output = "";
  fetch(req, init) 
  .then(function(response) {
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
        output += (i+1) + ": " + fileList[i] + "<br /> ";
  
      console.log("Return1: " + output);
      var txtOutput = document.getElementById(id);
      txtOutput.value = output;
      return output;
     });
  })
  .catch(function(err) {
    console.log('Path fetch Error :-S', err);
  });
  console.log("Return2: " + output);
  return output;
}

function listPath() {
  var inputPath = document.getElementById("inputPath");
  console.log("Input path: " + inputPath.value);
  var filesUrl="http://localhost:8081/listFiles?path=/data/" + inputPath.value;
  var myPathRequest = new Request(filesUrl);

  var myHeaders = new Headers();
  myHeaders.append('pragma', 'no-cache');
  myHeaders.append('cache-control', 'no-cache');
  var myGet = {
    method: 'GET',
    mode: 'cors',
    headers: myHeaders,
  };

  PathFetch(myPathRequest, myGet, "outputList");
  //PathFetch(myPathRequest, myGet, "outputList2");
  //PathFetch2(myPathRequest, myGet, "outputList3");

}
