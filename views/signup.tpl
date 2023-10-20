<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - AchieveIT</title>
    <style>
        /* Add some basic styling for the header */
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

        /* Style the signup form */
        .signup-container {
            text-align: center;
            margin: 20px;
        }

        .signup-form {
            width: 300px;
            margin: 0 auto;
        }

        .signup-input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .signup-button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 10px 0;
            text-align: center;
            text-decoration: none;
            display: block;
            width: 100%;
            border-radius: 5px;
        }

        .signup-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="reviews">Reviews</a>
    <a class="header-button" href="login">Login</a>
    <a class="header-button" href="profile">Profile</a>
</header>

<!-- Sign Up Form -->
<div class="signup-container">
    <h2>Sign Up for AchieveIT</h2>
    <form class="signup-form" action="/signup" method="post">
        <input class="signup-input" type="text" name="first_name" placeholder="First Name" required>
        <input class="signup-input" type="text" name="last_name" placeholder="Last Name" required>
        <input class="signup-input" type="text" name="username" placeholder="Username" required>
        <input class="signup-input" type="email" name="email" placeholder="Email" required>
        <input class="signup-input" type="password" name="password" placeholder="Password" required>
        <button class="signup-button" type="submit">Sign Up</button>
    </form>
</div>

</body>

    <footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
        &copy; 2023 AchieveIT. All rights reserved.
    </footer>
</html>
