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
 
    document.getElementById('entry-id').value = entryId;
    document.getElementById('title').value = title;
    document.getElementById('content').value = content;
    document.getElementById('action').value = 'edit';
    window.scrollTo(0, 0);
}


// ------------------------------------------------------------Notification------------------------------------------

document.addEventListener("DOMContentLoaded", () => {
    const bell = document.getElementById("notification-bell");

    if (bell) {
        bell.addEventListener("click", () => {
            alert("Redirecting to Notifications...");
        });
    }
});

// ------------------------------------------------------------MIni-game------------------------------------------


let userScore=0;
let computerScore=0;

const choices = document.querySelectorAll(".choice");
const message = document.querySelector("#message");
const userScorePara = document.querySelector("#user_score");
const computerScorePara = document.querySelector("#computer_score");

const genComputerChoice = () => {
    const options = ["rock", "paper", "scissor"];
    const ranindx = Math.floor(Math.random() * 3);
    return options[ranindx];
    //Rock Paper Scissor
}

const drawGame = () => {
    message.innerText = "Game was Draw! Play Again";
    message.style.backgroundColor = "rgb(6, 9, 36)"; 
}

const showWinner = (userWin, userChoice, compChoice) => {
    if(userWin) {
        userScore++;
        userScorePara.innerText=userScore;
        message.innerText = `You Wins! Your ${userChoice} beats ${compChoice}`
        message.style.backgroundColor = "green"; 
    } else{
        computerScore++;
        computerScorePara.innerText=computerScore;
        message.innerText = `You Lose! ${compChoice} beats your ${userChoice}` 
        message.style.backgroundColor = "red"; 
    }
}

const playGame =  (userChoice) => {
    console.log("user choice = ", userChoice)
    const compChoice = genComputerChoice();
    console.log("Computer choice = ", compChoice);
    // Generate computer choice
    if (userChoice === compChoice){
        //Draw Game
        drawGame();
    }
    else{
        let userWin = true;
        if (userChoice==="rock") {
            //scissor, paper
            userWin = compChoice === "paper" ? false : true;
        } else if (userChoice === "paper") {
            // rock, scissor
            userWin = compChoice === "scissor" ? false : true;
        } else {
            // rock, paper
            userWin = compChoice === "rock" ? false : true;
        }
        showWinner(userWin, userChoice, compChoice);
    }
}

choices.forEach((choice) => {
    choice.addEventListener("click", () => {
        const userChoice = choice.getAttribute("Id");
        playGame(userChoice);
    })
})

function submitThoughtForm() {
    const form = document.getElementById("challenge-thoughts-form");
    alert("Thoughts submitted! Keep practicing.");
    form.reset();
}

function submitGratitudeForm() {
    const form = document.getElementById("gratitude-form");
    alert("Gratitude entries submitted!");
    form.reset();
}

function startBreathingExercise() {
    let step = 0;
    const instructions = ["Inhale for 4 seconds...", "Hold your breath for 7 seconds...", "Exhale for 8 seconds..."];
    const breathingElement = document.getElementById("breathing-instructions");

    const interval = setInterval(() => {
        breathingElement.textContent = instructions[step];
        step = (step + 1) % instructions.length;
    }, 4000);

    setTimeout(() => clearInterval(interval), 12000); // Stops after one cycle
}

// ------------------------------------------------------------mood------------------------------------------


document.getElementById('detect-mood').addEventListener('click', () => {
    fetch("{% url 'detect_mood' %}", { method: 'POST', headers: { 'X-CSRFToken': '{{ csrf_token }}' } })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('mood-result').innerText = `Detected Mood: ${data.mood}`;
        }
    });
});