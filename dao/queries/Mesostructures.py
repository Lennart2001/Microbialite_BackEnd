# Mesostructure_Data
createDataTable = """CREATE TABLE Mesostructure_Data(
	mesostructureID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	mesostructureType VARCHAR(50),
    mesostructureTexture VARCHAR(50),
    mesostructureDesc VARCHAR(255),
    macrostructureID INT UNSIGNED NOT NULL,
    sampleSize VARCHAR(20),
    fieldDescription VARCHAR(255),
    rockDescription VARCHAR(255),
    laminaThickness DECIMAL(2,2),
    synopticRelief DECIMAL(2,2),
    wavelength DECIMAL(2,2),
    amplitude DECIMAL(2,2),
    mesostructureGrains VARCHAR(50),
	FOREIGN KEY (macrostructureID) REFERENCES Macrostructure_Data(macrostructureID)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);"""
dropDataTable = "DROP TABLE IF EXISTS Mesostructure_Data;"
getData = "SELECT * FROM Mesostructure_Data;"
getDataByID = "SELECT * FROM Mesostructure_Data WHERE mesostructureID = {mesostructureID};"
insertData = """INSERT INTO Mesostructure_Data (
    mesostructureType, 
    mesostructureTexture, 
    mesostructureDesc, 
    macrostructureID, 
    sampleSize, 
    fieldDescription, 
    rockDescription, 
    laminaThickness, 
    synopticRelief, 
    wavelength, 
    amplitude, 
    mesostructureGrains
) VALUES (
    '{mesostructureType}', 
    '{mesostructureTexture}', 
    '{mesostructureDesc}', 
    {macrostructureID}, 
    '{sampleSize}', 
    '{fieldDescription}', 
    '{rockDescription}', 
    {laminaThickness}, 
    {synopticRelief}, 
    {wavelength}, 
    {amplitude}, 
    '{mesostructureGrains}');"""
updateData = """UPDATE Mesostructure_Data SET 
    mesostructureType='{mesostructureType}', 
    mesostructureTexture='{mesostructureTexture}', 
    mesostructureDesc='{mesostructureDesc}', 
    macrostructureID={macrostructureID}, 
    sampleSize='{sampleSize}', 
    fieldDescription='{fieldDescription}', 
    rockDescription='{rockDescription}', 
    laminaThickness={laminaThickness}, 
    synopticRelief={synopticRelief}, 
    wavelength={wavelength}, 
    amplitude={amplitude}, 
    mesostructureGrains='{mesostructureGrains}' 
    WHERE 
    mesostructureID = {mesostructureID};"""
deleteData = "DELETE FROM Mesostructure_Data WHERE mesostructureID = {mesostructureID};"


# Searches_Meso
createSearchesTable = """CREATE TABLE Searches_Meso(
	userID INT UNSIGNED NOT NULL,
	mesostructureID INT UNSIGNED NOT NULL,
	PRIMARY KEY(userID, mesostructureID),
	FOREIGN KEY (userID) REFERENCES User(userID)       
	ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (mesostructureID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""
dropSearchesTable = "DROP TABLE IF EXISTS Searches_Meso;"
getSearches = "SELECT * FROM Searches_Meso;"
getSearchesByIDs = """SELECT * FROM Searches_Meso 
                    WHERE 
                    userID = {userID} 
                    AND 
                    mesostructureID = {mesostructureID};"""
insertSearches = """INSERT INTO Searches_Meso (userID, mesostructureID) 
                    VALUES 
                    ({userID}, {mesostructureID});"""
updateSearches = """UPDATE Searches_Meso 
                    SET 
                    userID = {newUserID} 
                    WHERE 
                    userID = {currentUserID} 
                    AND 
                    mesostructureID = {mesostructureID};"""
deleteSearches = """DELETE FROM Searches_Meso 
                    WHERE 
                    userID = {userID} 
                    AND 
                    mesostructureID = {mesostructureID};"""

# Add_Meso_Data
createAddTable = """CREATE TABLE Add_Meso_Data(
	analystID INT UNSIGNED NOT NULL,
	mesostructureID INT UNSIGNED NOT NULL,
	PRIMARY KEY(analystID, mesostructureID),
	FOREIGN KEY (analystID) REFERENCES Analyst(analystID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (mesostructureID) REFERENCES Waypoint_Data(waypointID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""
dropAddTable = "DROP TABLE IF EXISTS Add_Meso_Data;"
getAdd = "SELECT * FROM Add_Meso_Data;"
getAddByIDs = """SELECT * FROM Add_Meso_Data 
                     WHERE 
                     analystID = {analystID} 
                     AND 
                     mesostructureID = {mesostructureID};"""
insertAdd = """INSERT INTO Add_Meso_Data (analystID, mesostructureID) 
                   VALUES 
                   ({analystID}, {mesostructureID});"""
updateAdd = """UPDATE Add_Meso_Data 
                   SET 
                   analystID = {newAnalystID} 
                   WHERE 
                   analystID = {currentAnalystID} 
                   AND 
                   mesostructureID = {mesostructureID};"""
deleteAdd = """DELETE FROM Add_Meso_Data 
                   WHERE 
                   analystID = {analystID} 
                   AND 
                   mesostructureID = {mesostructureID};"""


# Mesostructure_Photo
createPhotoTable = """CREATE TABLE Mesostructure_Photo(
	mesostructureID INT UNSIGNED NOT NULL,
	mesoPhotoID INT,
	mesoPhoto VARCHAR(255),
	PRIMARY KEY(mesostructureID, mesoPhotoID),
    FOREIGN KEY (mesostructureID) REFERENCES Mesostructure_Data(mesostructureID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);"""
dropPhotoTable = "DROP TABLE IF EXISTS Mesostructure_Photo;"
getPhoto = "SELECT * FROM Mesostructure_Photo;"
getPhotoByIDs = """SELECT * FROM Mesostructure_Photo 
                   WHERE 
                   mesostructureID = {mesostructureID} 
                   AND 
                   mesoPhotoID = {mesoPhotoID};"""
insertPhoto = """INSERT INTO Mesostructure_Photo (mesostructureID, mesoPhotoID, mesoPhoto) 
                 VALUES 
                 ({mesostructureID}, {mesoPhotoID}, '{mesoPhoto}');"""
updatePhoto = """UPDATE Mesostructure_Photo 
                 SET 
                 mesoPhoto='{mesoPhoto}' 
                 WHERE 
                 mesostructureID = {mesostructureID} 
                 AND 
                 mesoPhotoID = {mesoPhotoID};"""
deletePhoto = """DELETE FROM Mesostructure_Photo 
                 WHERE 
                 mesostructureID = {mesostructureID} 
                 AND 
                 mesoPhotoID = {mesoPhotoID};"""
