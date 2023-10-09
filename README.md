# Stock Indices Dashboard Project

## Overview

This project provides an interactive dashboard developed with Dash to track the real-time evolution of the S&P 500 and NASDAQ stock indices. The data is updated every minute and presents a graphical visualization of the indices' evolution along with some basic statistics.

![Example Image](Example.jpg)

## Features

- **Real-Time Graphs**: Visualize the evolution of the S&P 500 and NASDAQ indices with interactive graphs.
- **Live Statistics**: Obtain real-time statistics such as the minimum, maximum, standard deviation, last, and first value for each index.
- **Automatic Update**: Data and visualizations are automatically updated every minute.

## How Does It Work?

Data is extracted, processed, and stored in a CSV file. Then, the dashboard reads this file and updates the graphs and statistics in real-time.

## Technologies Used

- **[Python](https://www.python.org/)**: Programming language used for data processing and dashboard creation.
- **[Dash](https://dash.plotly.com/)**: Python framework used to create the web application and interactive dashboard.
- **[Plotly](https://plotly.com/)**: Python library for creating interactive graphs.

## How to Run the Project?

1. Clone the GitHub repository.
2. Ensure that Python and the necessary libraries (Dash, Plotly, etc.) are installed.
3. Run the `main.py` script to start the Dash server.
4. Open your web browser and go to `localhost:8050` to see the dashboard in action.

## Important Note

The main Python script is run in the "Session_active" tmux session. To access it, use: 
```shell
tmux attach -t Session_active
```
IP to access the site: [http://13.53.150.105:8050/](http://13.53.150.105:8050/)

## Author

[Rostane F](https://github.com/RostaneF)
