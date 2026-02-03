// Select the "Add task" button
const addBtn = document.querySelector('.send');

// Load tasks from localStorage or initialize an empty array
let taskList = JSON.parse(localStorage.getItem('myTaks')) || [];

/**
 * Adds click event listeners to all delete buttons.
 * Each button removes its corresponding task.
 */
function delBtns() {
    const delBtn = document.querySelectorAll('.del');
    delBtn.forEach(btn => {
        btn.addEventListener('click', () => {
            // Get the task text related to the clicked delete button
            const taskText = btn.parentNode.querySelector('.task').innerText;

            // Find the index of the task in the array
            const taskIndex = taskList.indexOf(taskText);

            // Remove task from the array
            taskList.splice(taskIndex, 1);

            // Update localStorage
            localStorage.setItem('myTasks', JSON.stringify(taskList));

            // Re-render the task list
            renderTaskList();
        })
    }); 
}

/**
 * Renders the task list in the DOM.
 * Clears the list and rebuilds it based on taskList array.
 */
function renderTaskList() {
    const list = document.querySelector('.task-list');

    // Clear existing tasks
    list.innerHTML = '';
    
    taskList.forEach(task => {
        const liElement = document.createElement("li");
        liElement.classList.add('bullet-point')
        liElement.innerHTML = `<span class="task">${task}</span> <button class="del"><img src="trash_icon-icons.com_48207.png" alt="trash icon" srcset=""></button>`;
        list.appendChild(liElement);
    });
    
    // Attach delete button events
    delBtns();
}

// Handle add task button click
addBtn.addEventListener('click', () => {
    const input = document.querySelector(".task").value;

    // Add new task to the array
    taskList.push(input);

    // Save updated tasks to localStorage
    localStorage.setItem('myTasks', JSON.stringify(taskList));

    // Update UI
    renderTaskList();  
})

// Initial render on page load
renderTaskList();