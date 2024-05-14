CREATE TABLE Farms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    rating FLOAT, 
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    address TEXT,
    website TEXT,
    phonenumber TEXT
    CHECK (rating >= 0 AND rating <=5 )
);

CREATE TABLE Tags (
    tag TEXT PRIMARY KEY
);

CREATE TABLE Farm_Tags(
    farm TEXT,
    tag TEXT,
    PRIMARY KEY (farm, tag),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (tag) REFERENCES Tags(tag)
);

--Här under finns en bas för att senare kunna lägga in öppettider--

CREATE TABLE Weekdays(
    weekday INT PRIMARY KEY,
    CHECK (weekday = 1 OR weekday = 2 OR weekday = 3 OR weekday = 4 OR weekday = 5 OR weekday = 6 OR weekday = 7)
);

INSERT INTO Weekdays (weekday) VALUES 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7);

CREATE TABLE Opening_Hours(
    farm_id TEXT,
    weekday INT,
    open_time TEXT,
    close_time TEXT,
    PRIMARY KEY (farm_id,weekday),
    FOREIGN KEY (farm_id) REFERENCES Farms(id),
    FOREIGN KEY (weekday) REFERENCES Weekdays(weekday)
);

--Och här under finns en bas för att kunna lägga in produkter--

CREATE TABLE Products(
    product TEXT PRIMARY KEY
);

CREATE TABLE Farm_Products(
    farm TEXT,
    product TEXT,
    PRIMARY KEY (farm,product),
    FOREIGN KEY (farm) REFERENCES Farms(id),
    FOREIGN KEY (product) REFERENCES Products(product)
);
-- Tables för reviews om vi vill låta usern reviewa farms
CREATE TABLE User_Ratings(
    farm TEXT,
	username TEXT, -- user är reserved keyword, bytit till username för att kunna skapa denna och nedanstående table.
	rating INT,
    PRIMARY KEY (farm, username),
    FOREIGN KEY (farm) REFERENCES Farms(id),
	CHECK (rating IN (1, 2, 3, 4, 5))
);

CREATE TABLE Farm_Reviews(
    review_id TEXT PRIMARY KEY,
    farm TEXT,
    username TEXT,
    comment TEXT,
    review_date DATE,
    FOREIGN KEY (farm) REFERENCES Farms(id)
);
