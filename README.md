Limar Expenses Dashboard 

 A dashboard built with Python's Dash framework to visualize monthly expenses for Limar Soya. 
 The data is processed from a CSV file and displayed using interactive pie and bar charts. 
 

 Features 

  * Visualize total monthly expenses based on different expense categories. 
  * Interactive dropdown to select specific expense categories. * Pie chart showing monthly expense distribution. 
  * Bar chart displaying monthly expense totals. 
  

  Prerequisites 

  * Python 3.x 
  *  Dash 
  *  Plotly 
  * Pandas 
  
   
  Installation 
  
   1. Clone the repository: bash Copy code `git clone https://github.com/username/limar-expenses-dashboard.git cd limar-expenses-dashboard`
   2. Install the required libraries: bash Copy code `pip install dash pandas plotly` 
   3. Add your financial records in CSV format (e.g., `Limar Soya 2024 Financial Record.csv`). Ensure that the file contains at least the following columns: * `date` (Date of the transaction) * `particulars` (Description of the expense) * `amount` (Amount spent, formatted as a string with or without commas) 
   

   Running the App 
   
   4. To run the Dash app, execute the following command: bash Copy code `python app.py` 
   5. Open your browser and navigate to `http://127.0.0.1:8050/` to view the dashboard. 
   

   File Structure

   `📦 limar-expenses-dashboard
    ┣ 📜 app.py # The main Python file to run the Dash app
    ┣ 📜 Limar Soya 2024 Financial Record.csv # The CSV file containing financial data 
    ┣ 📜 README.md # Project documentation 
    ┗ 📜 requirements.txt # Python dependencies` 
   

   Usage 

   * After starting the app, you can select different expense categories from the dropdown menu to view the monthly total expenses. 
   * Two visualizations are provided: 
   * A **pie chart** showing the distribution of expenses across months. 
   * A **bar chart** showing the monthly total expenses for the selected category.


License

This project is licensed under the MIT License.

