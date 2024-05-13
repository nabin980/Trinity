const reviewWrap = document.getElementById("reviewWrap");
const leftArrow = document.getElementById("leftArrow");
const rightArrow = document.getElementById("rightArrow");
const imgDiv = document.getElementById("imgDiv");
const personName = document.getElementById("personName");
const profession = document.getElementById("profession");
const description = document.getElementById("description");
const surpriseMeBtn = document.getElementById("surpriseMeBtn");
const chicken = document.querySelector(".chicken");

let isChickenVisible;

//  let people = [
//    {
//      photo: `url("${staticUrl}images/profile/Aisha Khan.jfif")`,
//      name: "Aisha Khan",
//      description: "I recently used Trinity Removals for my relocation, and I couldn't be more satisfied with their service. The team arrived on time, and their professionalism was evident throughout the entire process.",
//      rating: 5,
//    },
//   {
//  	photo: `url("${staticUrl}images/profile/Anand Verma.png")`,
//  	name: "Anand Verma",
//  	description:
//  		"The movers were courteous and worked diligently. However, there were a few communication hiccups that caused some confusion about the delivery schedule.",
//  		rating: 4,
//  },

//  {
//  	photo:
//  		`url("${staticUrl}images/profile/Jayawardena Perera.jfif")`,
//  	name: "Jayawardena Perera",
//  	description:
//  		"The team was not only professional but also incredibly friendly. They carefully wrapped and secured all my belongings, and nothing was damaged in transit. If you're looking for a stress-free move, Trinity Removals is the way to go!",
//  		rating: 5,
//  },

//  {
//  	photo: `url("${staticUrl}images/profile/Siddharth Sharma.jfif")`,
//  	name: "Siddharth Sharma",
//  	description:
//  		"Despite these challenges, the customer service team was responsive and addressed my concerns promptly. While there's room for improvement, I appreciate their efforts to make things right.",
//  		rating: 4,
//  },

//  {
//  	photo: `url("${staticUrl}images/profile/Priya Mehra.jfif")`,
//  	name: "Priya Mehra",
//  	description:
//  		"I recently moved with Trinity Removals, and I am beyond impressed with the level of service they provided. From the moment they arrived to the completion of the move, everything was handled with professionalism and care. The team was efficient, friendly. ",
//  		rating: 5,
//  },

//  {
//  	photo:
//    `url("${staticUrl}images/profile/Ahmed Malik.jfif")`,
//  	name: "Ahmed Malik",
//  	description:
//  		"Movers were hardworking and polite, but a piece of furniture suffered a minor scratch during the move. On the positive side, the customer service team was responsive and addressed my concerns promptly.",
//  		rating: 4,
//  }
//  ];

imgDiv.style.backgroundImage = people[0].photo;
personName.innerText = people[0].name;
profession.innerText = people[0].profession;
description.innerText = people[0].description;


function updateStarRating() {
	const starContainer = document.querySelector('.star-container');
	starContainer.innerHTML = '';
  
	const rating = people[currentPerson].rating;
	const fullStars = Math.floor(rating);
	const hasHalfStar = rating % 1 !== 0;
  
	for (let i = 0; i < fullStars; i++) {
	  const star = document.createElement('span');
	  star.className = 'star';
	  star.innerHTML = '★';
	  starContainer.appendChild(star);
	}
  
	if (hasHalfStar) {
	  const halfStar = document.createElement('span');
	  halfStar.className = 'star';
	  halfStar.innerHTML = '★'; // You can customize the appearance of a half-star
	  halfStar.style.width = '50%'; // Adjust the width based on your design
	  starContainer.appendChild(halfStar);
	}
  
	const emptyStars = Math.floor(5 - rating);
	for (let i = 0; i < emptyStars; i++) {
	  const star = document.createElement('span');
	  star.className = 'star';
	  star.innerHTML = '☆';
	  starContainer.appendChild(star);
	}
  }
  

function initializeStarRatings() {
  for (let i = 0; i < people.length; i++) {
    const starContainer = document.createElement('div');
    starContainer.className = 'star-container';
    document.getElementById('reviewWrap').appendChild(starContainer);
  }
}

initializeStarRatings();

let currentPerson = 0;

function slide(whichSide, personNumber) {
  let reviewWrapWidth = reviewWrap.offsetWidth + "px";
  let descriptionHeight = description.offsetHeight + "px";
  let side1symbol = whichSide === "left" ? "" : "-";
  let side2symbol = whichSide === "left" ? "-" : "";

  let tl = gsap.timeline();

  if (isChickenVisible) {
    tl.to(chicken, {
      duration: 0.4,
      opacity: 0
    });
  }

  tl.to(reviewWrap, {
    duration: 0.4,
    opacity: 0,
    translateX: `${side1symbol + reviewWrapWidth}`
  });

  tl.to(reviewWrap, {
    duration: 0,
    translateX: `${side2symbol + reviewWrapWidth}`
  });

  setTimeout(() => {
    imgDiv.style.backgroundImage = people[personNumber].photo;
    updateStarRating(); // Call the updateStarRating function here
  }, 400);

  setTimeout(() => {
    description.style.height = descriptionHeight;
  }, 400);

  setTimeout(() => {
    personName.innerText = people[personNumber].name;
  }, 400);

  setTimeout(() => {
    profession.innerText = people[personNumber].profession;
  }, 400);

  setTimeout(() => {
    description.innerText = people[personNumber].description;
  }, 400);

  tl.to(reviewWrap, {
    duration: 0.4,
    opacity: 1,
    translateX: 0
  });

  if (isChickenVisible) {
    tl.to(chicken, {
      duration: 0.4,
      opacity: 1
    });
  }
}

function setNextCardLeft() {
  if (currentPerson === 5) {
    currentPerson = 0;
    slide("left", currentPerson);
  } else {
    currentPerson++;
  }

  slide("left", currentPerson);
}

function setNextCardRight() {
  if (currentPerson === 0) {
    currentPerson = 5;
    slide("right", currentPerson);
  } else {
    currentPerson--;
  }

  slide("right", currentPerson);
}

leftArrow.addEventListener("click", setNextCardLeft);
rightArrow.addEventListener("click", setNextCardRight);

window.addEventListener("resize", () => {
  description.style.height = "100%";
});

document.addEventListener("DOMContentLoaded", function() {
  const successMessage = document.querySelector('.messages .success');

  if (successMessage) {
      // Show a pop-up or notification
      showPopup('Login successful!');

      // Redirect after a delay (e.g., 3000 milliseconds = 3 seconds)
      setTimeout(function() {
          window.location.href = '{% url "home" %}';
      }, 3000);
  }

  // Function to show a pop-up
  function showPopup(message) {
      const popup = document.createElement('div');
      popup.classList.add('popup');
      popup.textContent = message;

      document.body.appendChild(popup);

      setTimeout(function() {
          popup.remove();
      }, 3000);  // Remove the pop-up after 3 seconds
  }
});

// Close the popup when the close button is clicked
const closeButton = document.getElementById('close-popup');
if (closeButton) {
  closeButton.addEventListener('click', function() {
      const popup = document.getElementById('popup');
      if (popup) {
          popup.remove();
      }
  });
}

const radioButtons = document.querySelectorAll('input[type=radio]');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let currentIndex = 0;
let touchStartX = 0;
let touchMoveX = 0;

const slideShow = () => {
  const showSlide = (index) => {
    for (let i = 0; i < radioButtons.length; i++) {
      radioButtons[i].checked = i === index;
    }
  };

  const handleArrowKeys = (event) => {
    if (event.key === 'ArrowLeft') {
      currentIndex = (currentIndex - 1 + radioButtons.length) % radioButtons.length;
      showSlide(currentIndex);
    } else if (event.key === 'ArrowRight') {
      currentIndex = (currentIndex + 1) % radioButtons.length;
      showSlide(currentIndex);
    }
  };

  const handleTouchStart = (event) => {
    touchStartX = event.touches[0].clientX;
    touchMoveX = 0;
  };

  const handleTouchMove = (event) => {
    touchMoveX = event.touches[0].clientX - touchStartX;
    // You can add visual feedback for the drag here if needed
  };

  const handleTouchEnd = () => {
    handleSwipe();
    // Reset touch values
    touchStartX = 0;
    touchMoveX = 0;
  };

  const handleSwipe = () => {
    const swipeThreshold = 50; // Adjust this value for sensitivity

    if (touchMoveX > swipeThreshold) {
      // Swipe right
      currentIndex = (currentIndex - 1 + radioButtons.length) % radioButtons.length;
      showSlide(currentIndex);
    } else if (touchMoveX < -swipeThreshold) {
      // Swipe left
      currentIndex = (currentIndex + 1) % radioButtons.length;
      showSlide(currentIndex);
    }
  };

  const autoChangeSlide = () => {
    currentIndex = (currentIndex + 1) % radioButtons.length;
    showSlide(currentIndex);
  };

  // Add event listeners
  prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + radioButtons.length) % radioButtons.length;
    showSlide(currentIndex);
  });

  nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % radioButtons.length;
    showSlide(currentIndex);
  });

  // Add event listener for arrow keys
  document.addEventListener('keydown', handleArrowKeys);

  // Add touch event listeners
  document.addEventListener('touchstart', handleTouchStart);
  document.addEventListener('touchmove', handleTouchMove);
  document.addEventListener('touchend', handleTouchEnd);

  // Automatically change slide every 5 seconds
  setInterval(autoChangeSlide, 5000);
};

slideShow();


// Function to open the review form modal
function openReviewForm() {
  document.getElementById("reviewFormModal").style.display = "block";
}

// Function to close the review form modal
function closeReviewForm() {
  document.getElementById("reviewFormModal").style.display = "none";
}

// Optional: Close the modal if the user clicks outside of it
window.onclick = function(event) {
  var modal = document.getElementById("reviewFormModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Optional: Close the modal if the user presses the 'Esc' key
document.onkeydown = function(event) {
  event = event || window.event;
  if (event.key === "Escape") {
    closeReviewForm();
  }
};


const allStar = document.querySelectorAll('.rating .star')
const ratingValue = document.querySelector('.rating input[name="rating"]')

allStar.forEach((item, idx)=> {
	item.addEventListener('click', function () {
		let click = 0
		ratingValue.value = idx + 1

		allStar.forEach(i=> {
			i.classList.replace('bxs-star', 'bx-star')
			i.classList.remove('active')
		})
		for(let i=0; i<allStar.length; i++) {
			if(i <= idx) {
				allStar[i].classList.replace('bx-star', 'bxs-star')
				allStar[i].classList.add('active')
			} else {
				allStar[i].style.setProperty('--i', click)
				click++
			}
		}
	})
})




