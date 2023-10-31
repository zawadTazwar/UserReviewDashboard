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
        /* Style for the comment container */
        .comment-container {
            text-align: center;
            margin: 20px;
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
        }

        .comment-container h2 {
            font-size: 18px;
            margin-bottom: 10px;
        }

        .comment-container form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .comment-container textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .comment-container button {
            background-color: #2368dc;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 10px 0;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            width: 40%;
            border-radius: 5px;
        }

        .comment-container button:hover {
            background-color: #45a049;
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

    <div class="comment-container">
        <h2>Add a Comment</h2>
        <form action="/add_comment/{{review['_id']}}" method="POST">
            <textarea name="comment" placeholder="Write your comment here..." rows="4" required></textarea>
            <button type="submit">Submit Comment</button>
        </form>
    </div>


</body>
<footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
    &copy; 2023 AchieveIT. All rights reserved.
</footer>
</html>
