<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Review - AchieveIT</title>
    <style>
        /* Simple CSS for styling */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
        main {
            max-width: 600px;
            margin: 30px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 4px;
            border: 1px solid #ccc;
        }
        button {
            background-color: #007BFF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<header>
    <h1>AchieveIT - Edit Review</h1>
</header>

<main>
    <h2>Edit Your Review</h2>

    <form action="/update_review" method="post">
        <!-- Hidden input to send review_id back to server -->
        <input type="hidden" name="review_id" value="{{review['_id']}}">

        <label for="content">Review Content:</label>
        <textarea name="content" id="content" rows="10" required>{{review['content']}}</textarea>
        <button type="submit">Update Review</button>
    </form>
</main>

<footer style="background-color: #333; color: #fff; text-align: center; padding: 10px;">
    &copy; 2023 AchieveIT. All rights reserved.
</footer>

</body>
</html>
