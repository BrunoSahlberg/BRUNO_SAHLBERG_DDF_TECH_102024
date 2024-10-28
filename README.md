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
<hr>
<p> API - Home (/docs)
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/api.png" alt="API">
</p>
<p> API - POST
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/api_post.png" alt="API POST">
</p>
<p> API - GETALL
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/api_post.png" alt="API GETALL">
</p>
<p> API - PUT
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/api_post.png" alt="API PUT">
</p>
<p> API - DELETE
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/api_delete.png" alt="API DELETE">
</p>
<hr>
<h1 align="center"> Streamlit APP </h1>
<p>I also created an app with Streamlit on the Dadosfera intelligence platform, that can be accessed by this <a href="https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=f4006681-c07a-4270-8aed-2271b5f37fac&pipeline_uuid=3969dc54-dec0-4beb-bed3-448725a197e2"> link</a>. </p>
<p> APP - HOME
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/app.png" alt="APP">
</p>
<p> APP - TABLE & GRAPH
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/app_table.png" alt="APP TABLE AND GRAPH">
</p>
<p> APP - GENERATED DATASET 
<img src="https://github.com/BrunoSahlberg/dadosfera-api/blob/main/prints/app_dataset.png" alt="APP DATASET">
</p>
