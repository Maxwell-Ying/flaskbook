from flask import render_template, flash, redirect, url_for, session
from app import app
from app import db
from app.forms import EntryForm, DeleteEntry, SearchEntry, UpdateEntry
from app.models import books

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index')
def index():
    return render_template("index.html",
                           title = 'Home')

@app.route('/result/<search>')
def show_result(search):
    results = books.query.filter_by(name = search).all()
    return render_template("result.html",
                           title = search,
                           results = results)

@app.route('/add', methods = ['GET','POST'])
def add():
    form = EntryForm()
    #print(form.validate_on_submit())
    if form.validate_on_submit():
        #g.book.name = form.name.data
        #g.book.author = form.author.data
        u = books(name = form.name.data,    \
                 author = form.author.data, \
                 age = form.age.data,       \
                 public = form.public.data, \
                 home = form.home.data,     \
                 pages = form.pages.data)
        db.session.add(u)
        db.session.commit()
        #print(u)
        flash('new item added!')
        return redirect('/index')
    else :
        return render_template("edit.html", form = form)
    
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = DeleteEntry()
    if form.validate_on_submit():
        u = books.query.filter_by(id = form.pos.data).first()
        print(u)
        if u != None:
            db.session.delete(u)
            db.session.commit()
            flash('delete finish')
        return redirect('/index')
    else:
        return render_template("delete.html", form = form)
    
@app.route('/deletes/<int:iden>')
def deletes(iden):
    u = books.query.filter_by(id = iden)
    if u:
        drop = u.first()
        db.session.delete(drop)
        db.session.commit()
        flash('delete finish')
        return redirect('/index')
    else:
        flash('not found')
        return redirect('/index')


@app.route('/showall')
def showall():
    results = books.query.all()
    return render_template("result.html",
                           title = 'all', 
                           results = results)

@app.route('/search', methods =['GET', 'POST'])
def search():
    form = SearchEntry()
    #print(form.is_submitted())
    if form.is_submitted():
        results = books.query
        if form.exact.data == False:
            if form.name.data:
                results = results.filter(books.name.like('%'+form.name.data+'%'))
            if form.author.data:
                results = results.filter(books.author.like('%'+form.author.data+'%'))
            if form.age.data:
                results = results.filter(books.age < form.age.data + 10, books.age > form.age.data - 10)
            if form.public.data:
                results = results.filter(books.public.like('%'+form.public.data+'%'))
            if form.home.data:
                results = results.filter(books.home.like('%'+form.home.data+'%'))
            if form.pages.data:
                results = results.filter(books.pages < form.pages.data + 20, books.pages > form.pages.data - 20)
        else:
            if form.name.data:
                results = results.filter(books.name == form.name.data)
            if form.author.data:
                results = results.filter(books.author == form.author.data)
            if form.age.data:
                results = results.filter(books.age == form.age.data)
            if form.public.data:
                results = results.filter(books.public == form.public.data)
            if form.home.data:
                results = results.filter(books.home == form.home.data)
            if form.pages.data:
                results = results.filter(books.pages == form.pages.data)
        return render_template("result.html",
                               title = 'search', 
                               results = results.all())
    else:
        return render_template("search.html", form = form)

@app.route('/update/<int:iden>', methods = ['GET', 'POST'])
def update(iden):
    p = books.query.filter(books.id == iden).first()
    form = UpdateEntry()
    if form.is_submitted():
        u = books(name = form.name.data,    \
                 author = form.author.data, \
                 age = form.age.data,       \
                 public = form.public.data, \
                 home = form.home.data,     \
                 pages = form.pages.data)
        i = books.query.filter(books.id == iden).first()
        if u.name:
            i.name = form.name.data
        if u.author:
            i.author = form.author.data
        if u.age:
            i.age = form.age.data
        if u.public:
            i.public = form.public.data
        if u.home:
            i.home = form.home.data
        if u.pages:
            i.pages = form.pages.data
        db.session.commit()
        flash('update OK')
        return redirect('/index')
    
    return render_template("update.html", form = form, data = p)
