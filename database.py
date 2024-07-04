from tinydb import TinyDB, Query

class Database:
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

    def __init__(self):
        self.db = TinyDB('database.json', indent=4)
        self.cameras = self.db.table('cameras')
        self.entrance_layouts = self.db.table('entrance_layouts')
        self.count_data = self.db.table('count_data')
        self.group_count_data = self.db.table('group_count_data')

    def add_camera(self, data: dict):
        self.cameras.insert(data)

    def get_cameras(self):
        return self.cameras.all()

    def add_entrance_layout(self, data: dict):
        self.entrance_layouts.insert(data)

    def get_entrance_layout(self):
        return self.entrance_layouts.all()

    def add_count_data(self, data: dict):
        self.count_data.insert(data)
    
    def add_several_count_data(self, data: list):
        self.count_data.insert_multiple(data)

    def get_input_count_data(self):
        data = self.count_data.search(Query().input == 1)
        return data
    
    def get_output_count_data(self):
        data = self.count_data.search(Query().output == 1)
        return data
    
    def add_group_count_data(self, data: dict):
        self.group_count_data.insert(data)

    def add_several_group_count_data(self, data: list):
        self.group_count_data.insert_multiple(data)

    def get_group_count_data(self):
        return self.group_count_data.all()
    
    def truncate_count_data(self):
        self.count_data.truncate()

    def truncate_group_count_data(self):
        self.group_count_data.truncate()
    
    def truncate_cameras(self):
        self.cameras.truncate()

    def truncate_layouts(self):
        self.entrance_layouts.truncate()