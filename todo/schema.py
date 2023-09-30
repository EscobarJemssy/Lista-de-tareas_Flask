instructions_sql=[
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE users;',
    'DROP TABLE todo;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE users(
            id_user int not null auto_increment,
            username varchar(50) not null unique,
            password varchar(100) not null,
            primary key(id_user)
            );
    """,
    """
        CREATE TABLE todo(
            id_todo int not null auto_increment,
            created_by int not null,
            created_date timestamp not null default CURRENT_TIMESTAMP,
            description text not null,
            completed boolean not null,
            primary key(id_todo),
            foreign key(created_by) references Users(id_user)
            );
    """
]