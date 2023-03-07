db = db.getSiblingDB("flaskitems");
db.createUser({
  user: "flask",
  pwd: "flaskpassword",
  roles: [{ role: "readWrite", db: "flaskitems" }],
});
