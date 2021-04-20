/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "left" });
  $(".collapsible").collapsible();
  $(".datepicker").datepicker({
    format: "yyyy",
    showClearBtn: true,
    i18n: {
      done: "Select",
    },
  });
});

/*
    vanilla JavaScript for MaterializeCSS initialization
*/

// document.addEventListener('DOMContentLoaded', function () {
//     let sidenavs = document.querySelectorAll(".sidenav");
//     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
// });
