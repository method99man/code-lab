// --- DOM Element Selectors ---
const userDisplay = document.querySelector('.usersNumber');
const incomeDisplay = document.querySelector('.income');
const growthDisplay = document.querySelector('.growth');

// --- Chart Initialization ---
const ctx = document.getElementById('myChart');

// Create the Chart instance
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Active users',
            data: [300, 500, 420, 610, 780, 900],
            borderWidth: 3,
            tension: 0.4,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false
            }
        }
    }
});

/**
 * Live Data Simulation Loop
 * Updates the chart and dashboard stats every 3 seconds (3000ms)
 */

setInterval(() => {
    // Update Chart Data
    // Generates a new random array of data based on the existing length
    const newData = myChart.data.datasets[0].data.map(() => Math.floor(Math.random() * 1000));
    myChart.data.datasets[0].data = newData;
    // Crucial: Tells Chart.js to re-render with the new values
    myChart.update();

    // Update User Count
    userDisplay.innerText = Math.floor(Math.random() * 1000);
    // Update Income Display
    incomeDisplay.innerText = '$' + (Math.floor(Math.random() * 10000)).toString();
    // Update Growth Percentage
    growthDisplay.innerText = Math.floor(Math.random() * 10);
}, 5000);

