from flask import Flask, render_template
import os
import markdown

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="pepino")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/projects")
def projects():
    dir = os.getcwd()+"\\server\\templates\\projects"

    projectsName = [project for project in os.listdir(dir)]

    projects = [markdown.markdown(open(dir+"\\"+projectName).read()) \
                for projectName in projectsName]

    return render_template('projects.html', projects=projects)
