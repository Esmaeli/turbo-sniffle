# generate_html.py

def generate_html():
    content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    """
    with open("index.html", "w") as file:
        file.write(content)

if __name__ == "__main__":
    generate_html()
