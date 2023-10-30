<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Profile - AchieveIT</title>
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

        /* Style the profile container */
        .profile-container {
            text-align: center;
            margin: 20px;
            padding: 20px;
            border-radius: 5px;
            background-color: #f5f5f5;
        }

        /* Style the user information */
        .user-info {
            font-size: 18px;
        }
    </style>
</head>
<body>
<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="/reviews">Reviews</a>
    <a class="header-button" href="/dashboard">Dashboard</a>
    <a class="header-button" href="/logout">Logout</a>
</header>

<!-- Profile Container -->
<div class="profile-container">
    <h2>My Profile</h2>
    <div class="user-info">
        <p><strong>Name:</strong> {{first_name}} {{last_name}}</p>
        <p><strong>Username:</strong> {{username}}</p>
        <p><strong>Email:</strong> {{email}}</p>
    </div>
</div>

</body>
<footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
    &copy; 2023 AchieveIT. All rights reserved.
</footer>
</html>

