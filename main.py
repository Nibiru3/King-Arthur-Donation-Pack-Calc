from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Калькулятор стоимости</title>
  </head>
  <body>
    <h1>Рассчитать стоимость пакета</h1>
    <form method="post">
      <label>Количество призывов:</label>
      <input type="number" name="pulls" value="0"><br>
      <label>Количество кристаллов:</label>
      <input type="number" name="crystals" value="0"><br>
      <label>Количество стамины:</label>
      <input type="number" name="stamina" value="0"><br>
      <label>Количество лег:</label>
      <input type="number" name="leg" value="0"><br>
      <button type="submit">Посчитать стоимость</button>
    </form>
    {% if cost is not none %}
      <h2>Итоговая стоимость: ${{ cost }}</h2>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    cost = None
    if request.method == "POST":
        pulls = int(request.form.get("pulls", 0))
        crystals = int(request.form.get("crystals", 0))
        stamina = int(request.form.get("stamina", 0))
        leg = int(request.form.get("leg", 0))

        cost = (pulls * 1) + (crystals * 0.00067) + (stamina * 0.00335) + (leg * 60)

    return render_template_string(HTML_TEMPLATE, cost=cost)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
