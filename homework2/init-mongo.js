db.createUser(
    {
        user: "flask",
        pwd: "flaskpassword",
        roles: [
            {
                role: "readWrite",
                db: "flaskitems"
            }
        ]
    }
);
db.createCollection("test");
