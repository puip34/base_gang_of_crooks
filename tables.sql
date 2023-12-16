CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Role VARCHAR(50) NOT NULL
);

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatorUserID INT,
    FOREIGN KEY (CreatorUserID) REFERENCES Users(UserID)
);

CREATE TABLE Tasks (
    TaskID INT PRIMARY KEY,
    TaskName VARCHAR(255) NOT NULL,
    Description TEXT,
    ProjectID INT,
    CreatorUserID INT,
    AssigneeUserID INT,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (CreatorUserID) REFERENCES Users(UserID),
    FOREIGN KEY (AssigneeUserID) REFERENCES Users(UserID)
);

CREATE TABLE Comments (
    CommentID INT PRIMARY KEY,
    TaskID INT,
    UserID INT,
    CommentText TEXT,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE Roles (
    RoleID INT PRIMARY KEY,
    RoleName VARCHAR(50) NOT NULL
);

CREATE TABLE UserRoles (
    UserRolesID INT PRIMARY KEY,
    UserID INT,
    RoleID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

CREATE TABLE ProjectUserRoles (
    ProjectUserRolesID INT PRIMARY KEY,
    ProjectID INT,
    UserID INT,
    RoleID INT,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

CREATE TABLE CompletedProjects (
    CompletedProjectID INT PRIMARY KEY,
    ProjectID INT,
    CompletionDate DATE,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

CREATE TABLE TaskStatus (
    TaskStatusID INT PRIMARY KEY,
    StatusName VARCHAR(50) NOT NULL
);

CREATE TABLE TaskHistory (
    TaskHistoryID INT PRIMARY KEY,
    TaskID INT,
    StatusID INT,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID),
    FOREIGN KEY (StatusID) REFERENCES TaskStatus(TaskStatusID)
);
