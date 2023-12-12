<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results - AchieveIT</title>
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

        /* Style for the review titles */
        .review-titles {
            text-align: left; /* Align items to the left */
            margin: 20px;
        }

        .review-block {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }

        .review-title {
            font-size: 20px;
            margin: 10px 0;
        }

        /* Style for the search bar */
        .search-bar {
            text-align: left; /* Align the search bar to the left */
            margin: 20px;
        }

        .search-bar form {
            display: flex;
            justify-content: space-between; /* Spacing between the input and button */
            align-items: center;
        }

        .search-bar input[type="text"] {
            width: 70%; /* Adjust the width */
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .search-bar button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px;
            margin: 10px 0;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            width: 25%; /* Adjust the width */
            border-radius: 5px;
        }

        .search-bar button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <header>
        <h1>AchieveIT</h1>
        <a class="header-button" href="/">Home</a>
        <a class="header-button" href="/reviews">Reviews</a>
        <a class="header-button" href="/profile">Profile</a>
        <a class="header-button" href="/login">Login</a>
        <a class="header-button" href="/logout">Logout</a>
        <a class="header-button" href="/contactus">Contact Us</a>
    </header>

    <div class="review-titles">
        <h1>Search Results</h1>
        <div class="search-bar">
            <form action="search_reviews" method="GET">
                <input type="text" name="query" placeholder="Search for reviews or usernames...">
                <button type="submit">Search</button>
            </form>
        </div>

        <h2>Results</h2>
        % for result in reviews:
        <div class="review-block">
            <a href="/view_review/{{result['_id']}}">{{result['title']}}</a>
            <p>Username: {{result['username']}}</p>
        </div>
        % end
    </div>

    <footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
        &copy; 2023 AchieveIT. All rights reserved.
    </footer>
</body>
</html>
