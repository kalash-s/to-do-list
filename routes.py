from flask import render_template, redirect, url_for, flash, get_flashed_messages
from app import app1, db
from models import Task
from datetime import datetime
import forms

@app1.route('/')
@app1.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app1.route('/add', methods = ['GET', 'POST'])
def add():
    form = forms.AddTaskform()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date = datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash("Task added")
        return redirect(url_for('index'))

    return render_template('add.html', form=form)

@app1.route('/edit/<int:task_id>', methods = ['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskform()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task is updated")
            return redirect(url_for('index'))

        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash("Task not found")
    return redirect(url_for('index'))

@app1.route('/delete/<int:task_id>', methods = ['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task is deleted")
            return redirect(url_for('index'))

        return render_template('delete.html', form=form, task_id=task_id, title = task.title)
    else:
        flash("Task does not exists.")
    return redirect(url_for('index'))

