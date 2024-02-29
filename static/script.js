document.querySelector(".thankyou").style.display="none";
var submitted = 0;

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
    if(!submitted){
      submitQuiz();
    }
  }
});

function submitQuiz() {


  var data = {
    name: 'Deepak Yadav',
    enroll:'2022BCSE039',
    ans:'Ab aaya na shi ans'
  }

  var radioButtons = document.getElementsByName("ans");

// Iterate over radio buttons to find the selected one
  var selectedValue = "";
  for (var i = 0; i < radioButtons.length; i++) {
    if (radioButtons[i].checked) {
      selectedValue = radioButtons[i].value;
      break; // Exit loop if found the selected radio button
    }
  }
  data.ans = selectedValue

  console.log(data.ans)
  
  var url = '/write';

  // // Example data to send to the server
  // var data = {
  //     "name": "Deepak Yadav",
  //     "enroll": "2022BCSE035",
  //     "ans": "Some answer"
  // };

  // Configuration for the Fetch API
  var requestOptions = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
  };

  // Send the request to the Flask server
  fetch(url, requestOptions)
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
          // Handle the response from the Flask server
          // document.getElementById("message").innerHTML = data['msg']
          alert(data.msg)
          if(data.val === 1){
            document.getElementById("question").style.display = "none";
            // document.getElementById("quiz-container").style.display = "flex";
            document.querySelector(".thankyou").style.display="flex";
          }
          else if(data.val === 0){
            document.getElementById("question").style.display = "none";
            document.getElementById("quiz-container").style.display = "flex";
          }
          submitted = 1
      })
      .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
      });

  // Send AJAX request to PHP script to submit the selection
  // var xhr = new XMLHttpRequest();
  // xhr.open("POST", "write", true);
  //   xhr.setRequestHeader("Content-Type", "application/json");
  //   xhr.onreadystatechange = function() {
  //     if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
  //       console.log("Quiz submitted successfully.", userSelection);
  //     }
  //     // redirect to thank you page
  //     document.getElementById("question").style.display = "none";
  //     // document.getElementById("quiz-container").style.display = "flex";
  //     document.querySelector(".thankyou").style.display="flex";
      
      
  //   };
  //   xhr.send(JSON.stringify(data)); // Send user selection as POST data
  }
  document.getElementById("submit_button").addEventListener("click", submitQuiz);
});


