from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, enumerate=enumerate)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({'id': len(tasks), 'text': task, 'completed': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if 0 <= task_id < len(tasks):
        if request.method == 'POST':
            new_text = request.form.get('task')
            if new_text:
                tasks[task_id]['text'] = new_text
            return redirect(url_for('index'))
        return render_template('edit.html', task=tasks[task_id])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)