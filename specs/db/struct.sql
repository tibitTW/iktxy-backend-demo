-- Table: users
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    pwd VARCHAR(255),
    email VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255),
    is_backend_user BOOLEAN,
    backend_level INT,
    created_at DATETIME,
    updated_at DATETIME
);

-- Table: programs
CREATE TABLE programs (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    programs_name_id INT,
    type INT,
    start_time DATETIME,
    end_time DATETIME,
    duration_hour FLOAT,
    holly_house_id INT,
    google_meet_url VARCHAR(255),
    youtube_url VARCHAR(255),
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (holly_house_id) REFERENCES holly_houses(id)
);

-- Table: programs_name
CREATE TABLE programs_name (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    created_at DATETIME,
    updated_at DATETIME
);

-- Table: holly_houses
CREATE TABLE holly_houses (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    gps_latitude FLOAT,
    gps_longitude FLOAT,
    owner_id INT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

-- Table: participate_records
CREATE TABLE participate_records (
    id INT PRIMARY KEY,
    user_id INT,
    program_id INT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (program_id) REFERENCES programs(id)
);
