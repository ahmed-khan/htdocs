<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    $captcha = $_POST['captcha'];

    // Simple CAPTCHA check
    if ($captcha == '5') { // 3 + 2 = 5
        // Prepare the content to be saved
        $content = "Name: $name\nEmail: $email\nMessage: $message\n\n";
        
        // Save to a text file
        file_put_contents('contact_responses.txt', $content, FILE_APPEND);
        
        // Display thank you message
        echo "Thank you for contacting us, $name! We will get back to you soon.";
    } else {
        echo "CAPTCHA verification failed. Please try again.";
    }
}
?>