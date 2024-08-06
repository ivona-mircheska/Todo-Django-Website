The Todo Website Django project is a web application designed to help users manage their tasks efficiently. Built using Django, this project employs function-based views and leverages Django's built-in authentication system to provide a comprehensive to-do list management experience.

Features

User Authentication: Users can register, log in, and log out.

Task Management: Authenticated users can create, update, and delete tasks.

Task Status: Users can categorize tasks by status, including "Finished" and "Done".

Task Viewing: Users can view their tasks and filter by status.

Project Structure

Home: The landing page displays tasks for authenticated users and provides login functionality.

Register: Users can create new accounts with a sign-up form.

Create Task: Authenticated users can add new tasks to their to-do list.

Update Task: Users can edit existing tasks, with validation to ensure only the task creator can update it.

Delete Task: Users can remove tasks from their list.

Finished Tasks: A dedicated view to list tasks marked as "Finished" or "Done".
