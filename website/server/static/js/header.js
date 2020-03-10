var templates = document.querySelector("#template-link").import;

window.onload = function() {
  header = document.importNode(templates.getElementById("header-container"), true)
  $("body").prepend(header)
}