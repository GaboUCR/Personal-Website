from flask import Flask, render_template, redirect
import os
import markdown


app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="pepino")

@app.route("/")
def home():
    return redirect("/projects")

@app.route("/me")
def me():
    return render_template('me.html')

@app.route("/blog")
def blogs():
    dir = os.getcwd()+"\\server\\templates\\blogs"

    blogsName = [blog for blog in os.listdir(dir)]

    blogs = [open(dir+"\\"+blogName+"\\preview.html").read() for blogName in blogsName]

    return render_template('blogs.html', blogs=blogs)



@app.route("/projects")
def projects():
    dir = os.getcwd()+"\\server\\templates\\projects"

    projectsName = [project for project in os.listdir(dir)]

    projects = [open(dir+"\\"+projectName+"\\preview.html").read() for projectName in projectsName]

    return render_template('projects.html', projects=projects)
