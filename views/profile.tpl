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

        ul {
            list-style: none;
            padding: 0;
            margin: 10px 0;
            text-align: center;
        }

        /* Style the review list items (anchors) */
        ul a {
            text-decoration: none;
            color: #2368dc;
            display: block;
            margin-bottom: 5px;
        }

        /* Hover effect for the review links */
        ul a:hover {
            text-decoration: underline;
        }


        /* Style the rating form */
        .rating-form {
            margin-top: 20px;
        }

        .rating-form label {
            font-weight: bold;
            font-size: 16px;
        }

        .rating-form input[type="number"] {
            width: 50px;
            padding: 5px;
            font-size: 16px;
        }

        .rating-form input[type="submit"] {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }

        .rating-form input[type="submit"]:hover {
            background-color: #45a049;
        }

        .average-rating {
            font-size: 20px;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="/reviews">Reviews</a>
    <a class="header-button" href="/contactus">Contact Us</a>
</header>

<!-- Profile Container -->
<div class="profile-container">
    <h2>{{username}} Profile</h2>
    <div class="user-info">
        <p><strong>Name:</strong> {{first_name}} {{last_name}}</p>
        <p><strong>Username:</strong> {{username}}</p>
        <p><strong>Email:</strong> {{email}}</p>
        <p><strong>Average Rating:</strong> {{average_rating}}</p>
    </div>

    <div class="rating-form">
        <form action="/rate_user/{{username}}" method="post">
            <label for="rating">Rate this profile:</label>
            <input type="number" id="rating" name="rating_value" min="1" max="5" required>
            <input type="submit" value="Rate">
        </form>
    </div>
        <h3>{{username}} Reviews:</h3>
            <ul>
                % for review in reviews:
                    <a href="/view_review/{{review['_id']}}">{{review['title']}}</a><br>
                % end
            </ul>
</div>


</body>
    <footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
        &copy; 2023 AchieveIT. All rights reserved.
    </footer>
</html>
