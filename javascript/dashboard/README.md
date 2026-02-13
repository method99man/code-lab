# 📊 Real-Time Analytics Dashboard
A sleek, responsive data dashboard built with Vanilla JavaScript and Chart.js. This project simulates a live analytics environment where user statistics, financial data, and activity charts update automatically every few seconds.

## 🚀 Features
- Live Data Simulation: The dashboard updates every 3 seconds to reflect "real-time" changes in users, income, and growth.
- Interactive Charting: Utilizes Chart.js to render a smooth, animated line graph with cubic interpolation (tension).
- Responsive Layout: Built using CSS Grid and Flexbox, ensuring the dashboard looks great on various screen sizes.
- Modern UI: Features a dark-themed professional sidebar and high-contrast stat cards with soft shadows.
## 🛠️ Tech Stack
- HTML5: Semantic structure.
- CSS3: Custom properties (variables), Grid, and Flexbox layout.
- JavaScript (ES6+): DOM manipulation and interval-based data logic.
- Chart.js: External library for data visualization via CDN.

## 📁 Project Structure
```bash
├── index.html   # Main dashboard structure & CDN imports
├── style.css    # Layout, sidebar styling, and card components
└── app.js       # Chart initialization and live update logic
```

## ⚙️ How to Use
Clone the repository:
```Bash
git clone https://github.com/your-username/your-repo-name.git
```
Open the project:
Simply double-click the index.html file in your browser. No local server or installation is required since it uses a CDN for Chart.js.

## 🧠 Code Highlights
Dynamic Chart Updates
The chart is updated by mapping new random values into the existing dataset and calling the .update() method to trigger built-in animations:

```JavaScript
setInterval(() => {
    const newData = myChart.data.datasets[0].data.map(() => Math.floor(Math.random() * 1000));
    myChart.data.datasets[0].data = newData;
    myChart.update();
    
    // UI updates...
}, 3000);
```

### Number Formatting
For a more professional feel, the project converts raw numbers into formatted strings:
- Income: Prefixed with $ symbol.
- Growth: Appended with % suffix.