# Round 2 Technical Task (Web Sraping)

<h1>Task Completed - </h1> <br>
1) Scrap  Data from "https://cellarbration.com.sg/whiskies.html" <br>
2) Store Data in Excel Sheet <br>
3) Store Data in MYSQL Database <br>

<h1>How to Run the Script - </h1>
<h2>There are two ways to run the Script -</h2>
1) On IDE <br>
2) On Google Colab <br>

<h2>Way 1 - (On IDE) - </h2>
Note :- Download Latest Version of Google Chrome - (https://www.google.com/intl/en_in/chrome/) <br><br>
1) Download and Extract All Files. <br>
2) Open Terminal / Command Prompt (CMD) <br>
3) pip3 install -r requirements.txt <br>
4) If you want to store Scraped Data in Local MYSQL Database (Or Skip) - <br>
    >> i) Install Xampp (https://www.apachefriends.org/download.html) <br>
    >> ii) Start Apache and MYSQL <br>
    >> iii) Goto phpmyadmin panal and create Database with name "task_data" <br>
    >> Note :- Username and Passwod of the Database should be Default as - Username = "root", Password = "" <br>
5) Run "main.py" <br>

<h3>Now, This will collect Data from given website and store it in Excel, JSON and MYSQL Database</h3> <br><br>
<h2>If you get any Error in IDE Method Please try "Google Colab" Method</h2><br>


<h2>Way 2 - (On Google Colab) - </h2>
<h3>Using Google Colab will save some time because low dependency to be download</h3> <br>
1) Open "https://colab.research.google.com/") <br>
2) Upload "Technical_Task_Parth_Barse.ipynb" file <br>
3) Run Each Code Cell in that Notebook <br>
4) From Google Colab we can store Data in Remote Database <br>
     >> Replace - engine = create_engine("mysql+pymysql://<username>:<password>@<hostname>/<Database Name>" <br>

<h3>Now, This will collect Data from given website and store it in Excel, JSON files</h3> <br>

<h1>Scraped Data - </h1>
1) Excel File :- finalData_1.xlsx <br>
2) JSON File :- Final_Data.json <br>

<h1>Time Taken to Execute the Complete Code - </h1>
Time = 1hr (on Google Colab)

<h1>Screenshot of Data in Local MYSQL Database (Optional)- </h1>

![Screenshot (273)](https://user-images.githubusercontent.com/91686761/159962471-23421d8a-dd75-42fc-94a7-de7fe43000d6.png)

<h1>Screenshot of Data in Remote MYSQL Database - </h1>

![Screenshot (274)](https://user-images.githubusercontent.com/91686761/160136865-30290347-a949-4f30-87c6-cbf2529f0565.png)
