INSERT INTO Roles (RoleID, RoleName) VALUES
    (1, 'Standard User'),
    (2, 'Advanced User');

INSERT INTO Users (UserID, Username, Password, Email, Role) VALUES
    (1, 'standard_user', 'password123', 'standard@example.com', 'Standard User'),
    (2, 'advanced_user', 'password456', 'advanced@example.com', 'Advanced User');

INSERT INTO UserRoles (UserRolesID, UserID, RoleID) VALUES
    (1, 1, 1), -- Assign Standard User role to standard_user
    (2, 2, 2); -- Assign Advanced User role to advanced_user;
