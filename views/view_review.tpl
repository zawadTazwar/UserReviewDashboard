<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Review - AchieveIT</title>
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

        /* Style the content container */
        .content-container {
            text-align: center;
            margin: 20px;
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
        }

        .content-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .content {
            margin: 10px 0;
        }
    </style>
</head>
<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="/reviews">Reviews</a>
    <a class="header-button" href="/profile">Profile</a>
</header>
<body>

<!-- Content Section -->
<div class="content-container">
    <h1>Review</h1>
    <div class="content-title">{{review['title']}}</div>
    <div class="content">{{review['content']}}</div>
</div>

</body>
<footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
    &copy; 2023 AchieveIT. All rights reserved.
</footer>
</html>
