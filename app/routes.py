from flask import render_template, redirect, url_for, request, send_from_directory, flash
from app import app
import os
from werkzeug import secure_filename
from app import faceMorph

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('static',filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files:
            flash('No file01 part')
            return redirect(request.url)
        
        if 'file2' not in request.files:
            flash('No file02 part')
            return redirect(request.url)
        file1 = request.files['file1']
        file2 = request.files['file2']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file1.filename == '':
            flash('No selected file01')
            return redirect(request.url)

        if file2.filename == '':
            flash('No selected file02')
            return redirect(request.url)

        #work on this to make it similar to our part
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename) :
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            save_to1=(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            save_to2=(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            file1.save(save_to1)
            file2.save(save_to2)
            #need a if statement to coorperate with Morph botton(p.s need to get Morph botton work)
            Morph_result= faceMorph.makeMorph(save_to1,save_to2)
            
            return render_template('index.html#about', morph= Morph_result)
            
    return render_template('index.html#feature')

# allowed image types
ALLOWED_EXTENSIONS = set(['jpg'])
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
