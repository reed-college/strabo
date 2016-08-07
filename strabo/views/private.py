'''
The admin interface has 4 different core features:

1. You can view an html table that corresponds directly with the database table. (interest_points_table)

2. There will be delete and edit options on that table. When these options are chosen
in the html form, the interest_points_redirect function is called,
no matter which option is chosen. So interest_points_redirect figures out which option was chosen.
If "delete" was chosen, it deletes the item from the table and refreshes the page.
If "edit" was chosen, it brings up an editing interface.

3. Upload/edit interface. The logic of this occurs in show_ips_upload_form.
It takes in an row object which can be blank, and does not have to be in the database
and process it so that an upload html form can be rendered with default entries corresponding to the
entries in the row object.

4. Upload interface. upload_images and upload_ips gives edit interface from #3
a row object with empty entries in it.

5. Submission: interest_points_post.
'''

from flask import request, render_template, redirect, url_for

from strabo import geojson_wrapper
from strabo import database
from strabo import private_helper
from strabo import schema
from strabo import utils
from strabo import app
from strabo import db
from strabo import straboconfig

# Landing page allows viewer to select amoung tabs to start editing
@app.route("/admin/", methods=["GET"])
def index():
  return render_template("private/base.html",**straboconfig)


###
###
### Views for login page
###
###
@app.route("/login/", methods=["GET"])
def login():
    return render_template("/public/login.html",**straboconfig)

###
###
### Views to upload interest points to db
###
###

@app.route("/admin/edit_ips/")
def interest_points_table():
    interest_points = db.session.query(schema.InterestPoints).all()
    return render_template("private/edit_ips.html",
      interest_points=interest_points,
      **straboconfig)

@app.route("/admin/edit_ips/redirect")
def interest_points_redirect():
    edit_id = request.args.get("edit-btn")
    del_id = request.args.get("delete-btn")
    if edit_id:
        return show_ips_upload_form(db.session.query(schema.InterestPoints).get(edit_id))
    elif del_id:
        database.delete_ip(del_id)
        return redirect(url_for('interest_points_table'))
    else:
        raise RuntimeError("edit form somehow submitted without delete or edit being pressed")

def show_ips_upload_form(interest_point):
    #Gets all interest points, so that they can be displayed on the leaflet map.
    all_ips = db.session.query(schema.InterestPoints).all()
    geo_features = [geojson_wrapper.make_other_attributes_properties(ip) for ip in all_ips]
    #gets the geojson object corrsponding to the current interest point so that
    #the html form contains a default values for the geojson
    my_ip_json = geojson_wrapper.to_geo_obj(interest_point.geojson_object) if interest_point.id else False

    #gets images that the current interest point already owns
    ip_images = interest_point.images
    ip_images.sort(key=lambda img: img.ip_order_idx)
    jsonifiable_ip_images = [utils.concatenate_dicts(database.to_dictonary(img),{'day':img.taken_at.day,'month':img.taken_at.month,'year':img.taken_at.year}) for img in ip_images]

    return render_template("private/upload_ips.html",
        geo_features=geo_features,
        ip_images=jsonifiable_ip_images,
        interest_point=interest_point,
        my_ip_json=my_ip_json,
        straboconfig=straboconfig,
        image=db.session.query(schema.Images).first(),
        **straboconfig)

@app.route("/admin/upload_ips/")
def upload_ips():
    return show_ips_upload_form(schema.InterestPoints(title="",descrip_body="",geojson_object="",layer="",icon=""))

@app.route("/admin/interest_points/post", methods=["POST"])
def interest_points_post():
    imgs = [private_helper.make_image(ip_idx,*img_args) for ip_idx,img_args in enumerate(zip(
        request.form.getlist('img_id'),
        request.files.getlist('file'),
        request.form.getlist('img-descrip'),
        request.form.getlist('year'),
        request.form.getlist('month')
    ))]

    ip = private_helper.make_interest_point(request.form.get("ip_id"),imgs,
        request.form['title'],request.form['description'],request.form['geojson'],
        request.form['layer'],request.form['icon'])

    db.session.add(ip)
    db.session.commit()

    return redirect(url_for('interest_points_table'))
