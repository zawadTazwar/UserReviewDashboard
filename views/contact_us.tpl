<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>AchieveIT</title>
    <style>
        /* Header Style */
        header {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        /* Style the buttons */
        .header-button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
        }

        /* Style the buttons on hover */
        .header-button:hover {
            background-color: #45a049;
        }

        h2 {
            text-align: center;
            margin-bottom: 10px;
        }

        p {
            text-align: center;
            margin-bottom: 10px;
        }

        form {
            margin-top: 30px;
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
        }

        label {
            display: block;
            margin-bottom: 8px;
        }

        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 4px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        button {
            background-color: #007BFF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #0056b3;
        }

    </style>
</head>
<body>

<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="/reviews">Reviews</a>
    <a class="header-button" href="/login">Login</a>
    <a class="header-button" href="/logout">Logout</a>
</header>

<main>
    <h2>Get In Touch</h2>
    <p>We will get back to you as soon as possible!</p>

    <form action="/submit_inquiry" method="post">
        <!-- Username Field -->
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>

        <!-- Name Field -->
        <label for="name">Full Name:</label>
        <input type="text" name="name" id="name" required>

        <!-- Email Field -->
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>

        <!-- Subject Field -->
        <label for="subject">Subject:</label>
        <input type="text" name="subject" id="subject" required>

        <!-- Content Field -->
        <label for="content">Message:</label>
        <textarea name="content" id="content" rows="10" required></textarea>

        <button type="submit">Send Inquiry</button>
    </form>
</main>


</body>
    <footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
        &copy; 2023 AchieveIT. All rights reserved.
    </footer>
</html>
