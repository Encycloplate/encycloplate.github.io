# What is the Encycloplate?
The Encycloplate is a completely free template, a base for indie, authoritative non-wiki online encyclopedias about anything, with built-in useful JavaScript functions such as its own, custom, easy to use markup language with an automatic parser to HTML, an automatic, hassle-free ToC (Table of Contents) maker, a subtitle popup function, working random page button, modern CSS and more! You don't need to be an expert in coding, styling, formatting and SEO to make your encyclopedia anymore.

Please see the license before using this template.

# How to use it?
To use it to make your own project it is really simple, and basically you just need to fork it or download the files, customize the branding, style, and add your pages. Here is a list of steps you need to make:

1. Fork this repository or download the files
2. Download the Python 3.11.9 or newer at the [official Python website](https://www.python.org/downloads/)
3. Customize the branding to your own, and optionally, the styles
4. Write your article in an [.skt markup language](#silkrow) file in proper §Text formatting
5. Execute the silkrowparser.py and select the input .skt file path and the output .html path
6. Add the name of your new article in random.js under the js folder
7. Credit me and this repository in a visible part of your website :)
8. Make a new GitHub repository following the [Pages documentation](https://pages.github.com/) and dump the files and folders there
9. It should automatically deploy your website to the internet

# About the search box
In the home page there is a custom [Google Programmable Search Engine](https://programmablesearchengine.google.com/about/) box that, as it is an example, will only search on Wikipedia. However, you can make your own and seamlessly integrate it into the page. To make your own, go to their website, make a new search engine and put your pages there. After you set it up, replace the Google meta tag on the index.html with yours, and you are done.

<a name="silkrow"></a>

# About §Text
§Text, or SilkrowText, is a custom, FOSS, lightweight markup language developed by me previously, and I re-used it here and edited it to fit the needs of this project. To learn more about its syntax, I suggest taking a look at its [original repository](https://github.com/Pyrbor/SilkrowText). After you made your file, open its parser and type the path to your input file, the skt file, and the output file, the HTML file. It should look something like this if you didn't change the original file/folder structure:

![image](https://github.com/Encycloplate/encycloplate.github.io/assets/111013695/06c71998-457c-4dd9-a5b3-f84653c09fe3)

# Feature of Encycloplate

- Custom, editable and easy to use lightweight markup language
- Fairly modern, and clean and readable CSS
- Automatic keywording, description, title and SEO meta tags
- HTML parser for the custom markup language
- Wikipedia-like random article button/page
- Automatic/smart Table of Contents generator script
- Readable and pleasant homepage
- Google Programmable Search Engine integration
