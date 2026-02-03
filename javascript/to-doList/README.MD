# 📝 To-Do List App

A simple and clean **To-Do List application** built with **HTML, CSS and Vanilla JavaScript**.  
The project allows users to add and remove tasks, with data persisted using **Local Storage**.

This app was created as a practice project and portfolio example to demonstrate core front-end concepts.

---

## 🚀 Features

- Add new tasks to the list
- Delete tasks individually
- Persist tasks using **Local Storage**
- Responsive and clean UI
- Simple and readable code structure

---

## 🛠️ Technologies Used

- **HTML5** – semantic structure
- **CSS3** – layout, styling and responsiveness
- **JavaScript (ES6)** – DOM manipulation, events, local storage

---

## 📂 Project Structure

├── index.html # Application structure
├── style.css # Styles and layout
├── app.js # Application logic
└── README.md # Project documentation


---

## ⚙️ How It Works

1. The user types a task into the input field.
2. Clicking **"Add task"** adds the task to the list.
3. Tasks are stored in **localStorage**, so they persist after page reload.
4. Each task has a delete button that removes it from the list and storage.
5. The UI is re-rendered after every change to keep data in sync.

---

## 💾 Local Storage

Tasks are saved using the browser's `localStorage` API:

```js
localStorage.setItem('myTasks', JSON.stringify(taskList));

This ensures tasks are not lost when the page is refreshed.