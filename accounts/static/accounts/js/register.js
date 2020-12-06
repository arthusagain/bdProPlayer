onload = function() {
  document.getElementById('id_username').addEventListener('blur', 
  function(e){
    var fieldUsername = e.target.value;

    xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET','/accounts/verify_username' + "?username=" + encodeURIComponent(fieldUsername),true);
    xmlhttp.onreadystatechange = function(){
      if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
        var response = JSON.parse(xmlhttp.responseText);
        if(response.exists){
          document.getElementById('idErro').
            replaceChild(document.createTextNode("Username already exists"),
              document.getElementById('idErro').firstChild);
        }
        else{
          document.getElementById('idErro').
            replaceChild(document.createTextNode(""),
              document.getElementById('idErro').firstChild);
        }
      }
    };
    xmlhttp.send(null);
  });
}

