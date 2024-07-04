"""
    Database Methods:
        - Insert
        - Update
        - Delete
        - Get

    Class Methods:
    
    add_camera:
        - camera_id: str(ordinal number)
        - camera_name: str
        - camera_url: str
    
    get_cameras:
        - return all cameras

    add_entrance_layout:
        - camera_id: str
        - layout: str(cordinates, example: "0;0;0;0;0;0;0;0")

    get_entrance_layout:
        - camera_id: str

    add_count_data:
        - camera_id: str
        - input: int(0 or 1, if input is 1 then output is 0)
        - output: int(0 or 1, if input is 0 then output is 1)
        - timestamp: str

    get_input_count_data:
        return all input count data

    get_output_count_data:
        return all output count data

    add_group_count_data:
        - people_ids: list
        - number_of_people: int
        - timestamp: str
    
    get_group_count_data:
        return all group count data

    # trancate count data table
    truncate_count_data:
        remove all count data

    truncate_group_count_data:
        remove all group count data
    """

from flask import Flask, jsonify, request
from database import Database
import pathlib
import markdown

db = Database()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    path = str(pathlib.Path().absolute()/'docs.md')  # Assuming the file is named docs.md
    with open(path, 'r') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)
    return html_content


@app.route('/cameras', methods=['GET', 'POST'])
def cameras():
    if request.method == 'GET':
        return jsonify(db.get_cameras())
    elif request.method == 'POST':
        data = request.get_json()
        db.add_camera(data)
        return jsonify({"message": "Camera added successfully."})
    

@app.route('/entrance_layouts', methods=['GET', 'POST'])
def entrance_layouts():
    if request.method == 'GET':
        return jsonify(db.get_entrance_layout())
    elif request.method == 'POST':
        data = request.get_json()
        db.add_entrance_layout(data)
        return jsonify({"message": "Entrance layout added successfully."})
    

@app.route('/count_data', methods=['GET', 'POST'])
def count_data():
    if request.method == 'GET':
        return jsonify(db.get_count_data())
    elif request.method == 'POST':
        data = request.get_json()
        if type(data) != list:
            db.add_count_data(data)
        else:
            db.add_several_count_data(data)
        return jsonify({"message": "Count data added successfully."})
    

@app.route('/group_count_data', methods=['GET', 'POST'])
def group_count_data():
    if request.method == 'GET':
        return jsonify(db.get_group_count_data())
    elif request.method == 'POST':
        data = request.get_json()
        if type(data) != list:
            db.add_group_count_data(data)
        else:
            db.add_several_group_count_data(data)
        return jsonify({"message": "Group count data added successfully."})
    

@app.route('/truncate_count_data', methods=['GET'])
def truncate_count_data():
    db.truncate_count_data()
    return jsonify({"message": "Count data trancated successfully."})


@app.route('/truncate_group_count_data', methods=['GET'])
def truncate_group_count_data():
    db.truncate_group_count_data()
    return jsonify({"message": "Group count data trancated successfully."})

@app.route('/truncate_cameras', methods=['GET'])
def truncate_cameras():
    db.truncate_cameras()
    return jsonify({"message": "Cameras trancated successfully."})

# truncate entrance_layouts
@app.route('/truncate_entrance_layouts', methods=['GET'])
def truncate_entrance_layouts():
    db.truncate_layouts()
    return jsonify({"message": "Entrance layouts trancated successfully."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)