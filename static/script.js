document.querySelector(".thankyou").style.display="none";

document.addEventListener("DOMContentLoaded", function() {
  var quizContainer = document.getElementById("interface");
  var startQuizBtn = document.getElementById("start-quiz-btn");
  
  startQuizBtn.addEventListener("click", function() {
    // Request fullscreen
    document.getElementById("question").style.display = "block";
    document.getElementById("quiz-container").style.display = "none";
    document.querySelector(".thankyou").style.display="none";
    if (quizContainer.requestFullscreen) {
      quizContainer.requestFullscreen();
    } else if (quizContainer.mozRequestFullScreen) { /* Firefox */
    quizContainer.mozRequestFullScreen();
  } else if (quizContainer.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
  quizContainer.webkitRequestFullscreen();
} else if (quizContainer.msRequestFullscreen) { /* IE/Edge */
quizContainer.msRequestFullscreen();
}
});

// Exit fullscreen
document.addEventListener("fullscreenchange", function() {
  if (!document.fullscreenElement) {
    // Submit the quiz when exiting fullscreen
    submitQuiz();
  }
});

function submitQuiz() {
  // Get user selections (example: assume user selected option 2)
  // var userSelection = 2;
  var data = {
    name: 'Deepak Yadav',
    enroll:'2022BCSE035',
    ans:'Ab aaya na shi ans'
  }
  
  // Send AJAX request to PHP script to submit the selection
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "write", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        console.log("Quiz submitted successfully.", userSelection);
      }
      // redirect to thank you page
      document.getElementById("question").style.display = "none";
      // document.getElementById("quiz-container").style.display = "flex";
      document.querySelector(".thankyou").style.display="flex";
      
      
    };
    xhr.send(JSON.stringify(data)); // Send user selection as POST data
  }
  document.getElementById("submit_button").addEventListener("click", submitQuiz);
});


