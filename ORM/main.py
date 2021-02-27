from data import db_session
from data.users import User
from data.jobs import Jobs


def main():
    db_session.global_init('db/mars_explorer.db')
    session = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    user.hashed_password = hash('cap')
    session.add(user)

    user = User()
    user.surname = 'Weir'
    user.name = 'Andy'
    user.age = 20
    user.position = 'chief scienecist'
    user.speciality = 'geologist'
    user.address = 'module_1'
    user.email = 'andy_chief@mars.org'
    user.hashed_password = hash('sci')
    session.add(user)

    user = User()
    user.surname = 'Walles'
    user.name = 'Grommit'
    user.age = 23
    user.position = 'chief inventor'
    user.speciality = 'inventor'
    user.address = 'module_2'
    user.email = 'walles_chief@mars.org'
    user.hashed_password = hash('inv')
    session.add(user)

    user = User()
    user.surname = 'Alex'
    user.name = 'Kebig'
    user.age = 29
    user.position = 'middle inventor'
    user.speciality = 'radio research'
    user.address = 'module_2'
    user.email = 'alex_mid@mars.org'
    user.hashed_password = hash('rad')
    session.add(user)

    session.commit()


if __name__ == '__main__':
    main()