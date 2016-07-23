from flask import Flask

app = Flask(__name__)

#list of all resumes
@app.route('/')
def resume_list():
    return 'list of all resumes live here'

#list of all resumes
@app.route('/<int:id>')
def resume_view(id):
    return 'resume id: {id}'.format(id)

#list of all resumes
@app.route('/add')
def resume_add():
    return 'we can add resume here'


if __name__ == '__main__':
    app.run()

#this is a test