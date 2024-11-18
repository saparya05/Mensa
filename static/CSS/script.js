window.onload = function() {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
  
    // Function to change the active slide
    function changeSlide() {
      // Remove active class from all slides
      slides.forEach((slide, index) => {
        slide.classList.remove('active');
      });
  
      // Add active class to the current slide
      slides[currentSlide].classList.add('active');
  
      // Increment slide index, reset to 0 when it reaches the end
      currentSlide = (currentSlide + 1) % slides.length;
    }
  
    // Start the slideshow
    changeSlide();
    setInterval(changeSlide, 15000); // Change slide every 7 seconds
  };
  