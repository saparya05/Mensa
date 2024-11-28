const playlistMenu = document.getElementById('playlistMenu');
const songsList = document.getElementById('songsList');
const musicPlayerSide = document.getElementById('musicPlayerSide');
const audioPlayer = document.getElementById('audioPlayer');
const songsElement = document.getElementById('songs');
const songsCategory = document.getElementById('songsCategory');

let currentCategory = '';
let currentTrackIndex = 0;

const playlists = {
    yoga: [
        { title: 'Yoga Track 1', src: 'static/CSS/images/Audio1.mp3' },
        { title: 'Yoga Track 2', src: 'static/CSS/images/Audio2.mp3' },
    ],
    meditation: [
        { title: 'Meditation Track 1', src: 'static/CSS/images/Audio3.mp3' },
        { title: 'Meditation Track 2', src: 'static/CSS/images/Audio4.mp3' },
    ],
    sleep: [
        { title: 'Sleep Track 1', src: 'static/CSS/images/Audio5.mp3' },
        { title: 'Sleep Track 2', src: 'static/CSS/images/Audio1.mp3' },
    ],
    motivational: [
        { title: 'Motivational Track 1', src: 'static/CSS/images/Audio2.mp3' },
        { title: 'Motivational Track 2', src: 'static/CSS/images/Audio3.mp3' },
    ],
    energetic: [
        { title: 'Energetic Track 1', src: 'static/CSS/images/Audio4.mp3' },
        { title: 'Energetic Track 2', src: 'static/CSS/images/Audio5.mp3' },
    ],
};
window.onload = function () {
    playlistMenu.style.display = 'none';
    songsList.style.display = 'none';
    musicPlayerSide.style.display = 'none';
};


function toggleMenu() {
    playlistMenu.style.display = playlistMenu.style.display === 'flex' ? 'none' : 'flex';
}

function closeMenu() {
    playlistMenu.style.display = 'none';
}

function selectCategory(category) {
    currentCategory = category;
    currentTrackIndex = 0;

    songsElement.innerHTML = playlists[category]
        .map((track, index) => `<li onclick="playTrack(${index})">${track.title}</li>`)
        .join('');
    songsCategory.textContent = `${category.charAt(0).toUpperCase() + category.slice(1)} Playlist`;

    songsList.style.display = 'block';
    playlistMenu.style.display = 'none';
    
}

// Play a selected track
function playTrack(index) {
    currentTrackIndex = index;

    const track = playlists[currentCategory][index];
    audioPlayer.src = track.src;

    musicPlayerSide.style.display = 'flex';
    songsList.style.display = 'none';

    audioPlayer.play();
}

// Close the songs list
function closeSongsList() {
    songsList.style.display = 'none';
    playlistMenu.style.display = 'flex';
}

// Close the music player
function closeMusicPlayer() {
    musicPlayerSide.style.display = 'none';
    playlistMenu.style.display = 'flex';
}



// --------------------------------------------------SlideShow-----------------------------------------------
window.onload = function() {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
  

    function changeSlide() {

      slides.forEach((slide, index) => {
        slide.classList.remove('active');
      });
  

      slides[currentSlide].classList.add('active');
  

      currentSlide = (currentSlide + 1) % slides.length;
    }
  
    changeSlide();
    setInterval(changeSlide, 15000); 
  };
  
// -------------------------------------------Signup---------------------------------------------

function toggleMenu2() {
    const menu = document.getElementById('menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

// Close the menu if clicking outside
document.addEventListener('click', function (event) {
    const profile = document.getElementById('profile');
    const menu = document.getElementById('menu');

    if (!profile.contains(event.target) && !menu.contains(event.target)) {
        menu.style.display = 'none';
    }
});

// ---------------------------------------------activity fade----------------------------------------------------
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    const offset = 100; // Trigger when 100px away from the viewport
    return rect.top <= window.innerHeight - offset && rect.bottom >= offset;
  }
  
  
  // Function to toggle fade-in and fade-out
  function handleScroll() {
    const elements = document.querySelectorAll('.activity_item');
    elements.forEach(element => {
      if (isInViewport(element)) {
        element.classList.add('visible'); // Add class when in view
      } else {
        element.classList.remove('visible'); // Remove class when out of view
      }
    });
  }
  
  window.addEventListener('scroll', handleScroll);


// ------------------------------------------------------diary-entry-----------------------------------

function editEntry(entryId, title, content) {
    // Populate the form with the entry's data
    document.getElementById('entry-id').value = entryId;
    document.getElementById('title').value = title;
    document.getElementById('content').value = content;
    document.getElementById('action').value = 'edit';
    window.scrollTo(0, 0); // Scroll to the top where the form is
}