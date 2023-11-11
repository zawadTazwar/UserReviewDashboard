# Code Review

_Our code was reviewed in discord when our team had the opportunity to talk about it. This is our code review notes and process._

### Sprint 2 Code Review:

__Pull Request #41-45 (Date: Oct. 25)__
* meetingNotes were updated and some organization of markdown files into doc folder. No review needed.

__Pull Request #47-48 (Date: Oct. 26)__
* Session Management
* __Participants of review:__ Everyone
* Md Golam Mahmud Chowdhury was assigned this task. He implemented a new python file called session_management.py. Inside this file 4 functions were created; create_session, delete_session, manage_session, and get_session.
__create_session:__ This function is used to create a new user session. It generates a unique session ID, creates a session document containing user data, and stores it in the MongoDB collection designated for sessions. It also stores the session data in a dictionary for quick access.
__delete_session:__ This function is used to delete a user session associated with the provided session ID. It removes the session document from the MongoDB collection and removes the session data from the dictionary.
__manage_sessions:__ This function is meant to be used as a hook before processing requests. It checks if a session cookie (session_id) is present in the incoming request. If the session is valid, it sets the request.session attribute to the session data for use in the web application.
__get_session:__ This function retrieves the user session associated with the provided request. It reads the session ID from the request's cookies and uses it to fetch the session data from the dictionary.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well
* __Coding style conventions:__ Code does follow our conventions and docstrings clearly explain what code does.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ need to update info saved in each session to allow for unique pages based on the user. Such as Profiles, dashboard.

__Pull Request #55 (Date: Oct. 27)__
* meetingNotes was only thing updated. No review needed.

__Pull Request #56 (Date: Oct. 30)__
* updates to do_login function and create_session function. This was so the proper info was saved to implement unique pages for profiles and dashboard.
* __Participants of review:__ Everyone
* Md Golam Mahmud Chowdhury was assigned this task based on the improvement we found from his last pull request. user_id, first name, last name, and email was added to session data dictionary in create_session function. These attributes were also added to do_login function so that the HTML code will have access to this data of the user logged in.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ No improvements found after discussion.

__Pull Request #57 (Date: Oct. 30)__
* updated profile page html to have unique info of user logged in.
* __Participants of review:__ Everyone
* Jason was assigned this task. Current code displayed a generic name and info so the page worked. Now the profile.tpl file is updated so that it pulls the session data for the unique user.
The profile page now displays the username, first name, last name, and email of the user logged in.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ Want to update profile page to redirect you to the log in if you are not signed in. This will be put in backlog of kanban board.

__Pull Request #58-60 (Date: Oct. 31)__
* Incident made by Jason when trying to merge Master to his own branch. When trying to fetch and merge the master branch to his own, it causes conflicts on the pycharm ide. He was not sure what was happening and it caused some of the code on the master
to go back to a earlier version. He then made a pull request of the current code to fix the error. No code was harmed in the process and everything works as normal now.

__Pull Request #64 (Date: Oct. 31)__
* meetingNotes was only thing updated. No review needed.

__Pull Request #65 (Date: Oct. 31)__
* added HTML code for search bar form, and comment form.
* __Participants of review:__ Everyone
* Jason was assigned this task. We are implementing a search feature and comment feature. Jason updated the html code of reviews.tpl to add a search bar form and submit button. The server.py code is not functional to allow search to happen yet.
He also created a comment form on the view_review.tpl page to allow for comments once server.py code is implemented.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ No improvements found after discussion.

__Pull Request #66 (Date: 31)__
* added delete review button in HTML
* __Participants of review:__ Everyone
* Tazwar was assigned this task. He added a delete button to the dashboard to allow users to delete reviews they have made. This button works with the delete_review function in server.py.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ An idea of adding a confirm delete button for accidental clicks of button is added to backlog.

__Pull Request #81 (Date: Nov. 2)__
* meetingNotes was only thing updated. No review needed.

__Pull Request #83 (Date: Nov. 4)__
* added comment code to server.py. Updated database for comments as well.
* __Participants of review:__ Everyone
* Mahad was assigned this task. He updated the server.py code adding a comment table to the database that stores review id, username of user writing the comment, and content of the comment.
He also created a comment function on the server.py file. This function takes the review_id, username, and content from the HTML form and stores it in the comment table of database.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Docstrings need to be added, otherwise fine. We can do this before sprint deadline/final code review.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ Update HTML in view_review to now display all comments made on a review.

__Pull Request #84 (Date: Nov. 4)__
* added HTML to display the comments.
* __Participants of review:__ Everyone
* Jason was assigned this task. He updated the HTML of the view_review.tpl file. He accessed the comments stored in the database and displayed the information of the comment and the username of the user that wrote the comment.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ Add a delete comment button was added to backlog.

__Pull Request #85-87 (Date: Nov. 6)__
* added like/dislike feature.
* Jason worked on the HTML of view_review.tpl. He updated the file by created a like/dislike button form and displayed the count. 
Mahad updated the store_review function in server.py. He initialized the like and dislike attributes to be 0 when creating a review.
Tazwar added the like_review function in server.py. This function takes the argument review id and increases the count of the likes/dislikes. This happens by getting the action and determining what action was pressed. Then the function increases that action by one in the database.
* __Participants of review:__ Everyone
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Docstings need to be added. Otherwise fine, we can update before sprint deadline/final code review.
* __Code Guidelines:__ Code guidelines were checked and code is approved. Although improvement could be made since the like action is similar to dislike. It is possible to make it one line instead of almost duplicating the code with the if statement. Added to backlog because we are on tight schedule.
* __Improvement:__ Only allow logged in users to like/dislike and the user can only like/dislike once. Added to backlog.

__Pull Request #89-90 (Date: Nov. 6)__
* Added meetingNotes for today, and added our code_reviews.md file. No review needed.

__Pull Request #92 (Date: Nov. 7)__
* added Search bar
* __Participants of review:__ Everyone
* Md Golam Mahmud Chowdhury was assigned this task. He created the function search_reviews in server.py file. This function retrieves a search query from the URL's 'query' parameter and searches for reviews in the 'reviews_collection' with titles or usernames that match the query. 
It returns the search results using a template. He also created the search_results.tpl file. This file displays the search results performed by the call search_reviews. It also allows you to search again.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions. Docstrings look great.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ No improvement came from code review.

__Pull Request #93 (Date: Nov. 7)__
* Only meetingNotes, no review needed.

__Pull Request #94 (Date: Nov. 8)__
* Added Process Model Diagram and Unit Tests
* __Participants of review:__ Everyone
* Jason was assigned this task. Unit tests are in place now to test key calls to the server.py file. These will be used when doing code reviews going forward.
Process Model Document is used to explain our process of how we are working on the sprint as of today.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Coding style conventions:__ Code does follow our conventions.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ No improvement came from code review.

__Pull Request #98 (Date: Nov. 8)__
* Added rating review form and updated profile in server.py
* __Participants of review:__ Everyone
* Jason was assigned this task. He added a HTML form to view_review for rating users reviews. He also updated profile in server.py to redirect to log in page when not logged in.
* __Does it cause rest of code to not work?__ Code still works properly and new code does as well.
* __Unit Tests:__ All tests pass now for the first time ever. Because of this profile fix.
* __Coding style conventions:__ Docstrings need to be added which will be added tomorrow.
* __Code Guidelines:__ Code guidelines were checked and code is approved.
* __Improvement:__ The server.py needs to be updated to handle the HTML form for rating reviews. We haven't figured out how we want to handle this data yet and task will be in backlog.

**Final Code Review of Sprint 2 (Date: Nov. 10)**
* All code is in place and are working.
* Unit Tests all pass.
* Coding style conventions: Everything passes now since we added docstrings.
* Code Guidelines: Guidelines were reviewed and it is approved.




