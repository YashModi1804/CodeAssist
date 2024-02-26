<?php
// Retrieve user selection from POST data
if(isset($_POST['selection'])) {
  $userSelection = $_POST['selection'];

  // You can process the user's selection here (e.g., save to a database, perform calculations, etc.)
  
  // For demonstration, let's just return a success message
  echo "Quiz submitted successfully with selection: " . $userSelection;
} else {
  // Return an error if selection is not provided
  echo "Error: No selection provided.";
}
?>
