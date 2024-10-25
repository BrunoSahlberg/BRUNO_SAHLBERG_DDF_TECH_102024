<h1 align="center"> Python Process API </h1>
<p> Project created to represent an API in Python in which the user can insert, edit and delete processes through HTTP requests. </p>
<p> Technologies: 
<li> Python </li>
<li> FastAPI </li>
<li> PostgreSQL</li>
<li> SQL Alchemy </li>
  <br>

To use de same database that is already configured in the project, you have to install PostgreSQL and access with: <br>
username: <em> postgres </em> <br>
password: <em> root </em> <br>
Then, create a database named '<strong>dadosfera</strong>.'
  
<p> You also need to install de requirements.txt in a virtual environment (venv) in root folder and then execute the app: <br>
  <ol>
    <li> python -m venv venv </li>
    <li> .\venv\Scripts\activate </li>
    <li> pip install -r requirements.txt </li>
    <li> uvicorn app.main:app --reload </li>
  </ol>
<p>
  Now, you can access the API in <em> http://127.0.0.1:8000/docs </em> and test the requests in your browser or in a dedicated software like Postman!
</p>
</p>
