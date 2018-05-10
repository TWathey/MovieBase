from flask_script import Manager
from moviebase import app, db, Actor, Movie

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    actor1 = Actor(name='Liam Nesson', quote='"I do not know who you are. I do not know what you want. If you are looking for ransom I can tell you I do not have money, but what I do have are a very particular set of skills. Skills I have acquired over a very long career. Skills that make me a nightmare for people like you. If you let my daughter go now that will be the end of it. I will not look for you, I will not pursue you, but if you do not, I will look for you, I will find you and I will kill you."')
    actor2 = Actor(name='Nicholas Cage', quote='"We have to steal The Declaration of Independence!"')
    actor3 = Actor(name='Al Pacino', quote='"I always tell tell the truth, even when I lie"')
    movie1 = Movie(name='National Treasure', year=2004, plot="A historian races to find the legendary Templar Treasure before a team of mercenaries.", actor=actor2)
    movie2 = Movie(name='Scarface', year=1983, plot="In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.", actor=actor3)
    movie3 = Movie(name='Taken', year=2008, plot="A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris.", actor=actor1)

    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(actor3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
