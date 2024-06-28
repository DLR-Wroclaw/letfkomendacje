// $(function() {

//   $('.list-group-item').on('click', function() {
//     $(this).toggleClass('.collapse.show')
//     $('.fas', this)
//       .toggleClass('fa-angle-right')
//       .toggleClass('fa-angle-down');
//   });

// });
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".list-group-item").forEach(function (item) {
    item.addEventListener("click", function () {
      var fasIcon = this.querySelector(".fas");
      if (fasIcon) {
        fasIcon.classList.toggle("fa-angle-right");
        fasIcon.classList.toggle("fa-angle-down");
      }
    });
  });
});

