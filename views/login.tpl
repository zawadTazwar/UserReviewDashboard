<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login - AchieveIT</title>
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

        /* Style the login form */
        .login-container {
            text-align: center;
            margin: 20px;
        }

        .login-form {
            width: 300px;
            margin: 0 auto;
        }

        .login-input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .login-button {
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

        .login-button:hover {
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
    <a class="header-button" href="signup">Sign Up</a> <!-- Added "Sign Up" button -->
</header>

<!-- Login Form -->
<div class="login-container">
    <h2>Login to Your Account</h2>
    <form class="login-form" action="login" method="post">
        <input class="login-input" type="text" name="username" placeholder="Username" required>
        <input class="login-input" type="password" name="password" placeholder="Password" required>
        <button class="login-button" type="submit">Log In</button>
    </form>
</div>

</body>
<footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
    &copy; 2023 AchieveIT. All rights reserved.
</footer>
</html>
