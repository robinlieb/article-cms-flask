from flask import render_template, flash, redirect, request, url_for, current_app
from FlaskWebProject.forms import PostForm
from flask_login import current_user, login_required
from FlaskWebProject.models import Post
from FlaskWebProject import db
from . import posts_blueprint

@posts_blueprint.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post()
        post.save_changes(form, request.files['image_path'], current_user.id, new=True)
        current_app.logger.info("Successfully created post.")
        return redirect(url_for('users.home'))
    return render_template(
        'posts/post.html',
        title='Create Post',
        imageSource=_get_image_source_url,
        form=form
    )


@posts_blueprint.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id):
    post = Post.query.get(int(id))
    form = PostForm(formdata=request.form, obj=post)
    if form.validate_on_submit():
        post.save_changes(form, request.files['image_path'], current_user.id)
        return redirect(url_for('users.home'))
    return render_template(
        'posts/post.html',
        title='Edit Post',
        imageSource=_get_image_source_url(),
        form=form
    )

@posts_blueprint.route('/post/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    Post.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('users.home'))

@posts_blueprint.route('/post/delete/<image_name>/image', methods=['GET', 'POST'])
@login_required
def delete_image(image_name):
    Post.query.filter_by(image_path=image_name).first().remove_image()
    return redirect(url_for('users.home'))

def _get_image_source_url():
    return 'https://'+ current_app.config['BLOB_ACCOUNT']  + '.blob.core.windows.net/' + current_app.config['BLOB_CONTAINER']  + '/'
