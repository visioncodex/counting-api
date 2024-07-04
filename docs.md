# Flask API Documentation

This Flask application serves as an API for managing cameras, entrance layouts, and count data. Below is a detailed description of each endpoint and its functionality.

## Endpoints

### Home

- **URL:** `/`
- **Methods:** `GET`
- **Description:** Serves the `docs.html` file as the homepage.

### Cameras

- **URL:** `/cameras`
- **Methods:** `GET`, `POST`
- **Description:**
- `GET`: Retrieves all cameras from the database.
- `POST`: Adds a new camera to the database.
- **Request Body (POST):** JSON object containing camera details.
- **Response (POST):** JSON message confirming the addition of the camera.

### Entrance Layouts

- **URL:** `/entrance_layouts`
- **Methods:** `GET`, `POST`
- **Description:**
- `GET`: Retrieves all entrance layouts from the database.
- `POST`: Adds a new entrance layout to the database.
- **Request Body (POST):** JSON object containing entrance layout details.
- **Response (POST):** JSON message confirming the addition of the entrance layout.

### Count Data

- **URL:** `/count_data`
- **Methods:** `GET`, `POST`
- **Description:**
- `GET`: Retrieves all count data from the database.
- `POST`: Adds new count data to the database. If the request body is a list, it adds multiple count data entries.
- **Request Body (POST):** JSON object or list containing count data details.
- **Response (POST):** JSON message confirming the addition of the count data.

### Group Count Data

- **URL:** `/group_count_data`
- **Methods:** `GET`, `POST`
- **Description:**
- `POST`: Adds new group count data to the database. If the request body is a list, it adds multiple group count data entries.
- **Request Body (POST):** JSON object or list containing group count data details.
- **Response (POST):** JSON message confirming the addition of the group count data.

### Input Count data

- **URL:** `/input_count_data`
- **Methods:** `GET`
- **Description:** Takes in a list of count data entries and adds them to the database.

### Output Count data

- **URL:** `/output_count_data`
- **Methods:** `GET`
- **Description:** Takes in a list of count data entries and outputs them in JSON format.

### Truncate Count Data

- **URL:** `/truncate_count_data`
- **Methods:** `GET`
- **Description:** Truncates (deletes all entries) the count data from the database.
- **Response:** JSON message confirming the truncation of the count data.

### Truncate Group Count Data

- **URL:** `/truncate_group_count_data`
- **Methods:** `GET`
- **Description:** Truncates (deletes all entries) the group count data from the database.
- **Response:** JSON message confirming the truncation of the group count data.

### Truncate Cameras

- **URL:** `/truncate_cameras`
- **Methods:** `GET`
- **Description:** Truncates (deletes all entries) the cameras from the database.
- **Response:** JSON message confirming the truncation of the cameras.

### Truncate Entrance Layouts

- **URL:** `/truncate_entrance_layouts`
- **Methods:** `GET`
- **Description:** Truncates (deletes all entries) the entrance layouts from the database.
- **Response:** JSON message confirming the truncation of the entrance layouts.
