<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reviews - AchieveIT</title>
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

        /* Style the form for adding questions */
        .question-form {
            text-align: center;
            margin: 20px;
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
        }

        .question-input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .question-type {
            margin: 10px 0;
        }

        .question-button {
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

        .question-button:hover {
            background-color: #45a049;
        }

        /* Style for the review titles */
        .review-titles {
            text-align: center;
            margin: 20px;
        }

        .review-title {
            font-size: 20px;
            margin: 10px 0;
        }
        /* Style for the search bar */
        .search-bar {
            text-align: center;
            margin: 20px;
        }

        .search-bar form {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .search-bar input[type="text"] {
            width: 60%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .search-bar button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 10px 0;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            width: 20%;
            border-radius: 5px;
        }

        .search-bar button:hover {
            background-color: #45a049;
        }
            .top-review {
        text-align: center;
        margin: 20px auto;
        background-color: #f2f2f2; /* Light grey background */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
        max-width: 600px; /* Set a max-width for larger screens */
    }

    .top-review h2 {
        color: #2368dc; /* Matching the header-button color */
        margin-bottom: 15px;
    }

    .top-review p {
        font-size: 16px;
        color: #333; /* Dark grey for text */
        margin: 10px 0;
    }

    .top-review p strong {
        color: #000; /* Black for emphasis */
    }

    /* Responsive adjustments (if necessary) */
    @media (max-width: 768px) {
        .top-review {
            width: 90%;
            margin: 20px auto;
        }
    }


    </style>
</head>
<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="reviews">Reviews</a>
    <a class="header-button" href="profile">Profile</a>
    <a class="header-button" href="/login">Login</a>
    <a class="header-button" href="/logout">Logout</a>
    <a class="header-button" href="/contactus">Contact Us</a>

</header>
<body>

<!-- Review Titles Section -->
<div class="review-titles">
    <h1>Review Titles</h1>
    <div class="search-bar">
        <form action="search_reviews" method="GET">
            <input type="text" name="query" placeholder="Search for reviews...">
            <button type="submit">Search</button>
        </form>
<div class="top-review">
    <h2>Top Review</h2>
    % if top_review:
        <p><strong>Title:</strong> {{ top_review['title'] }}</p>
        <p><strong>Content:</strong> {{ top_review['content'] }}</p>
        <p><strong>Likes:</strong> {{ top_review['like'] }}</p>
    % else:
        <p>No top reviewer found.</p>
    % end
</div>

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
