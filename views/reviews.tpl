<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Review - AchieveIT</title>
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
    </style>
</head>
<body>
<!-- Header Section -->
<header>
    <h1>AchieveIT</h1>
    <a class="header-button" href="/">Home</a>
    <a class="header-button" href="reviews">Reviews</a>
    <a class="header-button" href="profile">Profile</a>
</header>

<!-- Review Creation Form -->
<div class="question-form">
    <h2>Create a Review</h2>
    <form action="#" method="post">
        <label for="question">Question:</label>
        <input class="question-input" type="text" name="question" id="question" required>

        <label for="questionType">Question Type:</label>
        <select class="question-type" id="questionType" name="questionType">
            <option value="wordBox">Word Box</option>
            <option value="multipleChoice">Multiple Choice</option>
        </select>

        <button class="question-button" type="submit">Add Question</button>
    </form>
</div>

</body>

    <footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
        &copy; 2023 AchieveIT. All rights reserved.
    </footer>
</html>
