#import sys
from flask import render_template, jsonify, request, session, flash, redirect, url_for
from app import app, db
from app.models import Markers, MarkersSchema, Content, ContentSchema, subContentSchema, Feedback
from app.forms import FeedbackForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/map1')
def map1():
  return render_template('map1.html', title='Map 1')

@app.route('/_get_markers')
def get_markers():
    markers = Markers.query.all()
    markers_schema = MarkersSchema(many=True)
    return jsonify(markers_schema.dump(markers))

@app.route('/_get_content')
def get_content():
    lref = request.args.get('linkRef', 0, type=str)
    return render_template(lref)

@app.route('/_get_list')
def get_list():
    mid = request.args.get('mid')
    contentList = Content.query.filter_by(marker_id=mid)
    content_schema = subContentSchema(many=True)
    return jsonify(content_schema.dump(contentList))

@app.route('/_template_test')
def template_test():
    return render_template('extends_test.html')

@app.route('/boxtest')
def boxtest():
    return render_template('boxes/wolvertoncollege.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/_feedbackform', methods=['GET', 'POST'])
def feedbackform():
    title = request.args.get('title', None)
    form = FeedbackForm(fbSubject=title)
    if request.method == 'POST':
      if 'submit' in request.form:
        if form.validate_on_submit():
          feedback = Feedback(item=form.fbSubject.data, fname=form.yourname.data, contact=form.contact.data, copyright=form.copyright.data, privacy=form.privacy.data, message=form.message.data)
          db.session.add(feedback)
          db.session.commit()
          flash('Thank you, your feedback about: {} has been recorded'.format(form.fbSubject.data))
          return redirect(url_for('map1'))
      else:
        return redirect(url_for('map1'))
    return render_template('FeedBackForm.html', title=title, form=form)


