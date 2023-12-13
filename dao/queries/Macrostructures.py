createMacroTable = """CREATE TABLE Macrostructure_Data(
	macrostructureID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	macrostructureType VARCHAR(50),
	sectionHeight DECIMAL(5,2),
	comments VARCHAR(255),
    waypointID INT UNSIGNED NOT NULL, 
    megastructureType VARCHAR(30),
    megastructureShape VARCHAR(30),
    megastructureSize VARCHAR(30),
    substrate VARCHAR(30),
    initiation VARCHAR(30),
    planView VARCHAR(30),
    linkage VARCHAR(30),
    spacing VARCHAR(30),
    shape VARCHAR(30),
    shapelayering VARCHAR(30),
    shapeDome VARCHAR(30),
    shape3d VARCHAR(30),
    aspectRation VARCHAR(30),
    growthVariability VARCHAR(30),
    attitude VARCHAR(30),
    branchingStyle VARCHAR(30),
    branchingMode VARCHAR(30),
    branchingAngle VARCHAR(30),
    columnShape VARCHAR(30),
    FOREIGN KEY (waypointID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);"""

createSearchesMacroTable = """CREATE TABLE Searches_Macro(
	userID INT,
	macrostructureID INT UNSIGNED NOT NULL,
	PRIMARY KEY(userID, macrostructureID),
	FOREIGN KEY (userID) REFERENCES User(userID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (macrostructureID) REFERENCES Macrostructure_Data(macrostructureID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

createAddMacroTable = """CREATE TABLE Add_Macro_Data(
	analystID INT UNSIGNED NOT NULL,
	macrostructureID INT UNSIGNED NOT NULL,
	PRIMARY KEY(analystID, macrostructureID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (macrostructureID) REFERENCES Macrostructure_Data(macrostructureID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);   """

createPhotoTable = """CREATE TABLE Macrostructure_Photo(
	macrostructureID INT UNSIGNED NOT NULL,
	macroPhotoID INT,
	macroPhoto VARCHAR(255),
	PRIMARY KEY(macrostructureID, macroPhotoID),
    FOREIGN KEY (macrostructureID) REFERENCES Macrostructure_Data(macrostructureID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""

dropDataTable = "DROP TABLE IF EXISTS Macrostructure_Data;"

dropSearchesTable = "DROP TABLE IF EXISTS Searches_Macro;"

dropAddDataTable = "DROP TABLE IF EXISTS Add_Macro_Data;"

dropPhotoTable = "DROP TABLE IF EXISTS Macrostructure_Photo;"