 const hamburgervv = document.querySelector(".hamburgervv");
 const navLinksvv = document.querySelector(".navbar-contentvv");
 const linksvv = document.querySelectorAll(".navbar-contentvv li");
 
 hamburgervv.addEventListener('click', () => {
   // Toggle the openvv class on navLinksvv
   navLinksvv.classList.toggle("openvv");

   // Toggle the fadevv class on each link
   linksvv.forEach((link, index) => {
     // Add a delay to stagger the animation of each link
     setTimeout(() => {
       link.classList.toggle("fadevv");
     }, index * 100); // Adjust the delay as needed
   });

   // Toggle the togglevv class on hamburgervv
   hamburgervv.classList.toggle("togglevv");
 });

// document.addEventListener("DOMContentLoaded", function() {
//   // Check if there is a hash in the URL (indicating an anchor link)
//   if (window.location.hash) {
//     // Scroll to the target container after a delay
//     setTimeout(() => {
//       const targetContainer = document.querySelector(window.location.hash);
//       if (targetContainer) {
//         targetContainer.scrollIntoView({
//           behavior: 'smooth'
//         });
//       }
//     }, 500); // Adjust the delay as needed
//   }
// });

// const hamburgervv = document.querySelector(".hamburgervv");
// const navLinksvv = document.querySelector(".navbar-contentvv");
// const linksvv = document.querySelectorAll(".navbar-contentvv li");

// hamburgervv.addEventListener('click', () => {
//   // Toggle the openvv class on navLinksvv
//   navLinksvv.classList.toggle("openvv");

//   // Toggle the fadevv class on each link
//   linksvv.forEach((link, index) => {
//     // Add a delay to stagger the animation of each link
//     setTimeout(() => {
//       link.classList.toggle("fadevv");
//     }, index * 100); // Adjust the delay as needed
//   });

//   // Toggle the togglevv class on hamburgervv
//   hamburgervv.classList.toggle("togglevv");
// });

// function navigateAndScrollHome() {
//   navigateAndScroll('#', 'home-container');
// }

// function navigateAndScrollService() {
//   navigateAndScroll('#service-container', 'service-container');
// }

// function navigateAndScroll(target, containerId) {
//   // Close the navigation menu
//   navLinksvv.classList.remove("openvv");
//   hamburgervv.classList.remove("togglevv");

//   // Scroll to the target container after a delay
//   setTimeout(() => {
//     const targetContainer = document.querySelector(containerId);
//     if (targetContainer) {
//       targetContainer.scrollIntoView({
//         behavior: 'smooth'
//       });
//     }
//   }, 500); // Adjust the delay as needed

//   // Prevent the default link behavior
//   event.preventDefault();
// }