import os
import re

def parse_line(lines, prefix):
    for line in lines:
        if line.startswith(prefix):
            return line.strip().replace(prefix, "").strip()
    return ""

def parse_content(lines):
    content = ""
    ul_open = False  # flag to track if <ul> tag is open
    for line in lines:
        if not any(line.startswith(prefix) for prefix in ["title:", "subtitle:", "founder:", "created:", "last-updated:", "last-updater:", "topics:"]):

            # converts some "markers" to HTML tags
            line = re.sub(r'\/\*\/(.*?)\/\*\/', r'<b>\1</b>', line)  # Bold
            line = re.sub(r'\/\/\/(.*?)\/\/\/', r'<i>\1</i>', line)  # Italics
            line = re.sub(r'\/\_\/(.*?)\/\_\/', r'<u>\1</u>', line)  # Underline
            line = re.sub(r'\/\~\/(.*?)\/\~\/', r'<del>\1</del>', line)  # Crossed
            line = re.sub(r'\/\#\/(.*?)\/\#\/', r'<code>\1</code>', line)  # Monospace
            line = re.sub(r'\/\!\/(.*?)\/\!\/', r'<mark>\1</mark>', line)  # Marked
            line = re.sub(r'\/\§\/ (.*?)', r'&emsp;&emsp;\1', line)  # Indentation
            line = re.sub(r'\/\,\/(.*?)', r'<hr>', line)  # HR Line

            # image marker
            section1 = '<img onclick="'
            section2 = "inform('"
            section3 = "')"
            section4 = '"'
            section5 = "src='../img/"
            section6 = "'>"

            line = re.sub(r'\/\@\/(.*?)\/(.*?)\/\@\/', section1 + section2 + r"\1" + section3 + section4 + section5 + r"\2" + section6, line)   

            # converts headings into HTML headings
            line = re.sub(r'\/\#1\/(.*?)\/\#1\/', r'<h1>\1</h1>', line)  # h1
            line = re.sub(r'\/\#2\/(.*?)\/\#2\/', r'<h2>\1</h2>', line)  # h2
            line = re.sub(r'\/\#3\/(.*?)\/\#3\/', r'<h3>\1</h3>', line)  # h3
            line = re.sub(r'\/\#4\/(.*?)\/\#4\/', r'<h4>\1</h4>', line)  # h4
            line = re.sub(r'\/\#5\/(.*?)\/\#5\/', r'<h5>\1</h5>', line)  # h5
            line = re.sub(r'\/\#6\/(.*?)\/\#6\/', r'<h6>\1</h6>', line)  # h6   

            # handles UL and LI markers
            if line.startswith("/=/"):  # UL
                if not ul_open:
                    content += "<ul>\n"
                    ul_open = True
            elif line.startswith("/-/"):  # LI
                content += f"<li>{line[3:]}</li>\n"
            else:
                # closes UL if it's open and not UL or LI
                if ul_open:
                    content += "</ul>\n"
                    ul_open = False
                content += line

    # closes UL if it's still open after processing all lines
    if ul_open:
        content += "</ul>\n"

    return content.strip()

def format_paragraphs(content):
    paragraphs = content.split('\n\n')
    html_paragraphs = ""
    for paragraph in paragraphs:
        html_paragraphs += f"<p>{paragraph}</p>\n\n"
    return html_paragraphs

def create_html_from_text(text_file, existing_html_file):
    # checks if the file exists
    if not os.path.exists(text_file):
        print(f"file '{text_file}' not found")
        return
    if not os.path.exists(existing_html_file):
        print(f"file '{existing_html_file}' not found")
        return

    # reads the content of the text file
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # parses tags
    title = parse_line(lines, "title:")
    subtitle = parse_line(lines, "subtitle:")
    founder = parse_line(lines, "founder:")
    created = parse_line(lines, "created:")
    lastupdated = parse_line(lines, "last-updated:")
    lastupdater = parse_line(lines, "last-updater:")
    topics = parse_line(lines, "topics:")
    content = parse_content(lines)
    formatted_content = format_paragraphs(content)

    # reads the HTML file
    with open(existing_html_file, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # inserts content into the <article> tag of the HTML file
    article_start = html_content.find("<article>") + len("<article>")
    article_end = html_content.find("</article>")
    html_content = html_content[:article_start] + f"""
    <p class="toc" onclick="informtoc();">ToC</p>
    <h1 class="title">{title}</h1>
    <p class="subtitle">{subtitle}</p>
    <div class="topics"><p>{topics}</p></div>
    <p class="created">Created by {founder} | {created}</p>
    <p class="lastupdated">Last updated by {lastupdater} | {lastupdated}</p>
    <hr>
    {formatted_content}

    """ + html_content[article_end:]

    # add meta tags
    meta_tags = f"""
    <link rel="stylesheet" type="text/css" href="../styles/font.css">
    <link rel="stylesheet" type="text/css" href="../styles/style.css">
    <script src="../js/info.js"></script>
    <script src="../js/toc.js"></script>
    <link rel="icon" type="x-icon" href="../img/encycloplate.png">
    <title>Encycloplate - {title}</title>
    <meta name="description" content="{subtitle}">
    <meta name="author" content="{founder}">
    <meta name="keywords" content="{topics}">
    """

    # replace the entire head with meta tags
    head_start = html_content.find("<head>") + len("<head>")
    head_end = html_content.find("</head>")
    html_content = html_content[:head_start] + meta_tags + html_content[head_end:]

    # writes updated HTML content into the HTML file
    with open(existing_html_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"content has been inserted into '{existing_html_file}' successfully")

if __name__ == "__main__":
    text_file = input("the input file name: ")
    existing_html_file = input("the html file name: ")
    create_html_from_text(text_file, existing_html_file)
    input("")
