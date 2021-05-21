from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note #List
from . import db
import json
views = Blueprint("views", __name__)
@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        if len(note) <= 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")
    return render_template("home.html", user=current_user)


# @views.route("/todo", methods=["GET", "POST"])
# @login_required
# def todo():
#     if request.method == "POST":
#         title = (request.form['title'])
#         desc = (request.form['desc'])
#         todo = List(title=title, desc=desc)
#         db.session.add(todo)
#         db.session.commit()
#     alltodo = List.query.all()
#     return render_template("index.html", alltodo=alltodo)

# @views.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):
#     if request.method == 'POST': 
#         title = (request.form['title'])
#         desc = (request.form['desc'])
#         todo = List.query.filter_by(sno=sno).first()
#         todo.title = title
#         todo.desc = desc
#         db.session.add(todo)
#         db.session.commit()
#         return redirect("/")
#     todo = List.query.filter_by(sno=sno).first()
#     return render_template("update.html", todo=todo)




# @views.route('/delete/<int:sno>')
# def delete(sno):
#     todo = List.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect("/")

@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})