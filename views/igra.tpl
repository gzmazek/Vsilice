<!DOCTYPE html>
<html>

<body>

  <h1>Stanje igre</h1>

  <p>
    Trenutno uganjeni del gesla: {{igra.pravilni_del_gesla()}}
  </p>

  <p>
    Nepravilne črke: {{igra.nepravilni_ugibi()}}
  </p>

  <p>
    Stopnja obešenosti:
  </p>

  <img src="img/{{igra.stevilo_napak}}.jpg" alt="obesanje">

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
</body>

</html>