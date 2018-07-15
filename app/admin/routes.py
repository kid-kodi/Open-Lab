from app import app, db
from flask import render_template, flash, redirect, url_for
from .forms import CategoryForm, LabelForm, ServiceForm
from flask_login import login_required
from app.models import Category, Label, Service
from . import bp


#routes equipment
@bp.route('/')
@bp.route('/index')
@login_required
def index():
    categories = Category.query.all()
    labels = Label.query.all()
    services = Service.query.all()
    return render_template('admin/dashboard.html',
                           categories=categories,
                           labels=labels,
                           services=services)


#routes category
@bp.route('/category')
@login_required
def category():
    list = Category.query.all()
    return render_template('admin/category/category.html', list=list)


@bp.route('/category/add', methods=['GET', 'POST'])
@login_required
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data,
                            description=form.description.data)
        db.session.add(category)
        db.session.commit()
        flash('données enregistrées')
        return redirect(url_for('admin.category'))
    return render_template('admin/category/add_category.html', form=form)


@bp.route('/category/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category( id ):
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        db.session.commit()
        flash('données modifiées')
        return redirect(url_for('admin.category'))
    form.description.data = category.description
    form.name.data = category.name
    return render_template('admin/category/add_category.html', form=form)


@bp.route('/category/detail/<int:id>')
@login_required
def detail_category(id):
    category = Category.query.get_or_404(id)
    return render_template('admin/category/detail_category.html', category=category)


@bp.route('/label')
@login_required
def label():
    list = Label.query.all()
    return render_template('admin/label/label.html', list=list)


@bp.route('/label/add', methods=['GET', 'POST'])
@login_required
def add_label():
    form = LabelForm()
    if form.validate_on_submit():
        label = Label(name=form.name.data,
                            description=form.description.data)
        db.session.add(label)
        db.session.commit()
        flash('données enregistrées')
        return redirect(url_for('admin.label'))
    return render_template('admin/label/add_label.html', form=form)


@bp.route('/label/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_label( id ):
    label = Label.query.get_or_404(id)
    form = LabelForm(obj=label)
    if form.validate_on_submit():
        label.name = form.name.data
        label.description = form.description.data
        db.session.commit()
        flash('données modifiées')
        return redirect(url_for('admin.label'))
    form.description.data = label.description
    form.name.data = label.name
    return render_template('admin/label/add_label.html', form=form)


@bp.route('/label/detail/<int:id>')
@login_required
def detail_label(id):
    label = Label.query.get_or_404(id)
    return render_template('admin/label/detail_label.html', label=label)


@bp.route('/service')
@login_required
def service():
    list = Service.query.all()
    return render_template('admin/service/service.html', list=list)


@bp.route('/service/add', methods=['GET', 'POST'])
@login_required
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(name=form.name.data,
                            description=form.description.data)
        db.session.add(service)
        db.session.commit()
        flash('données enregistrées')
        return redirect(url_for('admin.service'))
    return render_template('admin/service/add_service.html', form=form)


@bp.route('/service/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_service( id ):
    service = Service.query.get_or_404(id)
    form = ServiceForm(obj=service)
    if form.validate_on_submit():
        service.name = form.name.data
        service.description = form.description.data
        db.session.commit()
        flash('données modifiées')
        return redirect(url_for('admin.service'))
    form.description.data = service.description
    form.name.data = service.name
    return render_template('admin/service/add_service.html', form=form)


@bp.route('/service/detail/<int:id>')
@login_required
def detail_service(id):
    service = Service.query.get_or_404(id)
    return render_template('admin/service/detail_service.html', service=service)
