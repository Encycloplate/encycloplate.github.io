function redirectToRandomPage() {
  
  // add the name of the pages in /a/ here
  var pageNames = [ 
    "example"
  ];

  var randomIndex = Math.floor(Math.random() * pageNames.length);
  var url = "/a/" + pageNames[randomIndex] + ".html";
  window.location.href = "https://encycloplate.github.io" + url;
}
