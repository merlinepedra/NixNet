import json

with open('json/cards.json') as f:
    x = json.load(f)

text = ""
for i in x["cards"]:
    text += f"""
    <div class="card">
        <h1>{i["name"]}</h1>
        <p>{i["description"]}</p>
        <div class="buttons">
        <a href="{i["link"]}"><button class="button">{i["button_text"]}</button></a>
    """
    if i["tor"] != "#":
        text += f'<a href="{i["tor"]}"><button class="tor">Tor</button></a>'

    text += "</div></div>"

with open('_site/index.html') as f:
    y = f.read()

y = y.replace('<!-- Static cards -->', text)
with open('_site/index.html', 'w') as f:
    f.write(y)
