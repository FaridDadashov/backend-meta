// // "use strict";
// // document.querySelectorAll('.accordion-button').forEach(button => {
// //   button.addEventListener('click', event => {
// //     event.stopPropagation(); // Olayın hamburger menüye yayılmasını engelle
// //   });
// // });

// // let globus_ico = document.querySelector(".res-navbar ul .globus-menu");
// // let globus_ico_droppped = document.querySelector(
// //   ".res-navbar ul .globus-menu ul"
// // );

// // globus_ico.addEventListener("click",function(){
// //     globus_ico_droppped.classList.toggle("active")
// // })

// // let hamburger_li = document.querySelector(".hamburger_li");
// // let checkbox = document.querySelector(".hamburger input ");
// // let hamburger_li_dropped=document.querySelector(".res-navbar ul .hamburger_big__dropped")

// // hamburger_li.addEventListener("click", function () {

// //   if (checkbox.checked) {
// //     // console.log(checkbox)
// //     hamburger_li_dropped.classList.toggle("active");
// //   }
// // });
// "use strict";
// document.querySelectorAll('.accordion-button').forEach(button => {
//   button.addEventListener('click', event => {
//     event.stopPropagation(); // Olayın hamburger menüye yayılmasını engelle
//   });
// });

// let globus_ico = document.querySelector(".res-navbar ul .globus-menu");
// let globus_ico_droppped = document.querySelector(
//   ".res-navbar ul .globus-menu ul"
// );

// globus_ico.addEventListener("click",function(){
//     globus_ico_droppped.classList.toggle("active")
// })

// let hamburger_li = document.querySelector(".hamburger_li");
// let checkbox = document.querySelector(".hamburger input ");
// let hamburger_li_dropped=document.querySelector(".res-navbar ul .hamburger_big__dropped")

// hamburger_li.addEventListener("click", function () {

//   if (checkbox.checked) {
//     // console.log(checkbox)
//     hamburger_li_dropped.classList.toggle("active");
//   }
// });
// let slideIndex = 1;
// showSlides(slideIndex);

// // Next/previous controls
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   let dots = document.getElementsByClassName("dot");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
// }

// let currentIndex = 0;

// function moveSlider(direction) {
//   const track = document.querySelector('.slider-track');
//   const boxes = document.querySelectorAll('.box');
//   const boxWidth = boxes[0].offsetWidth + 20; // Include margin
//   const maxIndex = boxes.length - Math.floor(document.querySelector('.slider').offsetWidth / boxWidth);

//   currentIndex = Math.max(0, Math.min(currentIndex + direction, maxIndex));
//   track.style.transform = `translateX(-${currentIndex * boxWidth}px)`;
// }

// function flipBox(button) {
//   const box = button.parentElement;
//   box.classList.toggle('flipped');
// }

// document.addEventListener('DOMContentLoaded', function () {
//   const slider = document.querySelector('.slider');
//   const slides = document.querySelectorAll('.slide');
//   const prevButton = document.querySelector('.prev');
//   const nextButton = document.querySelector('.next');

//   let currentIndex = 0;
//   const slideWidth = slides[0].clientWidth; // Bir slide'ın genişliği
//   const slidesToShow = 4; // Aynı anda kaç slide gösterilecek
//   const maxIndex = slides.length - slidesToShow;

//   function updateSliderPosition() {
//     slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
//   }

//   prevButton.addEventListener('click', function () {
//     if (currentIndex > 0) {
//       currentIndex--;
//       updateSliderPosition();
//     }
//   });

//   nextButton.addEventListener('click', function () {
//     if (currentIndex < maxIndex) {
//       currentIndex++;
//       updateSliderPosition();
//     }
//   });
// });

// const slider = document.getElementById('slider');
// const leftBtn = document.querySelector('.left-btn');
// const rightBtn = document.querySelector('.right-btn');

// let currentIndex = 0; // Başlangıçta 0 index
// const boxes = document.querySelectorAll('.box');
// const totalBoxes = boxes.length;

// function updateSlider() {
//   const boxWidth = boxes[0].clientWidth;
//   slider.style.transform = `translateX(-${currentIndex * boxWidth}px)`;
// }

// // Sayfa yüklendiğinde slider'ı sabit bırak
// document.addEventListener('DOMContentLoaded', () => {
//   updateSlider(); // İlk pozisyonu doğru şekilde ayarla
// });

// // Sol buton tıklama olayı
// leftBtn.addEventListener('click', () => {
//   currentIndex =  6 ?  currentIndex - 1: totalBoxes - 1;
//   updateSlider();

// });

// // Sağ buton tıklama olayı
// rightBtn.addEventListener('click', () => {
//     currentIndex = 6   ? currentIndex + 1:totalBoxes +  1;
//     updateSlider();

// });

// // Pencere boyutlandırma değişikliklerinde slider'ı yeniden ayarla
// window.addEventListener('resize', updateSlider);

// --------------------------------------------------------

// $('.slider-ferid').slick({
//   infinite: true,
//   slidesToShow: 3,
//   slidesToScroll: 3
// });

$(".slider-ferid").slick({
  infinite: false,
  speed: 300,
  slidesToShow: 6,
  slidesToScroll: 1,
  prevArrow:
  '<button class="slick-prev"><i class="fa-solid fa-chevron-left"></i></button>',
nextArrow:
  '<button class="slick-next"><i class="fa-solid fa-chevron-right"></i></button>',
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        dots: true,
      },
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      },
    },
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ],
});
