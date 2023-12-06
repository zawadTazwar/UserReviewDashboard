<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>AchieveIT - Reset Password</title>
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

        /* Form Style */
        form {
            text-align: center;
            margin: auto;
            padding: 20px;
            max-width: 400px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
        }

        /* Footer Style */
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
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
    <a class="header-button" href="/contactus">Contact Us</a>
    <a class="header-button" href="/forgot_password">Forgot Password</a>
</header>

<main>
    <section>
        <h2>Reset Password</h2>
        <form action="/reset_password/{{ token }}" method="post">
            <input type="hidden" name="token" value="{{ token }}">
            <label for="password">Enter your new password:</label><br>
            <input type="password" id="password" name="password" required><br><br>
            <label for="confirm_password">Confirm your new password:</label><br>
            <input type="password" id="confirm_password" name="confirm_password" required><br><br>
            <input type="submit" value="Reset Password">
        </form>
    </section>
</main>

<footer>
    &copy; 2023 AchieveIT. All rights reserved.
</footer>

</body>
</html>
