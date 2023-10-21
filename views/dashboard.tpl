<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>AchieveIT - Dashboard</title>
    <style>
        /* Existing styles here */
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
        /* Style the "Edit Review" button */
        .edit-button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 5px 10px;
            margin: 5px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
        }

        .edit-button:hover {
            background-color: #45a049;
        }

        /* Style the "Create New Review" button */
        .create-button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            border-radius: 5px;
        }

        .create-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<!-- Header Section -->
<header>
    <h1>AchieveIT - Dashboard</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="/reviews">Reviews</a>
    <a class="header-button" href="/profile">Profile</a>
</header>

<!-- Main Content Section -->
<main style="background-color: #f5f5f5; padding: 20px; text-align: center;">
    <h2>Your Reviews</h2>

    <!-- Review 1 -->
    <div>
        <h3>Review 1</h3>
        <p>
            Your review content goes here.
        </p>
        <!-- Updated href for "Edit Review" button to point to the edit_review template -->
        <a class="edit-button" href="/edit_review?id=1">Edit Review</a>
    </div>

    <!-- Review 2 -->
    <div>
        <h3>Review 2</h3>
        <p>
            Your review content goes here.
        </p>
        <!-- Updated href for "Edit Review" button to point to the edit_review template -->
        <a class="edit-button" href="/edit_review?id=2">Edit Review</a>
    </div>

    <!-- Updated href for "Create New Review" button to point to the create_review template -->
    <a class="create-button" href="/create_review">Create New Review</a>
</main>

<footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
    &copy; 2023 AchieveIT. All rights reserved.
</footer>
</body>
</html>
