create table Project
(
    id   int auto_increment,
    name varchar(50) not null,

    primary key (id),

    constraint Projects_id_uindex
        unique (id),
    constraint Projects_name_uindex
        unique (name)
);

create table User
(
    id       int auto_increment,
    password varchar(32)  not null,
    name     varchar(50)  not null,
    email    varchar(254) not null,

    primary key (id),

    constraint User_email_uindex
        unique (email),
    constraint User_id_uindex
        unique (id)
);

create table User_Project
(
    user_id    int not null,
    project_id int not null,
    constraint project_id
        foreign key (project_id) references Project (id)
            on delete cascade,
    constraint user_id
        foreign key (user_id) references User (id)
            on delete cascade
);

create table WorkingHour
(
    user_id       int  not null,
    project_id    int  not null,
    calendar_week int  not null,
    monday        text null,
    tuesday       text null,
    wednesday     text null,
    thursday      text null,
    friday        text null,

    primary key (user_id, project_id, calendar_week),

    constraint wh_project_id
        foreign key (project_id) references Project (id)
            on delete cascade,
    constraint wh_user_id
        foreign key (user_id) references User (id)
            on delete cascade
);

