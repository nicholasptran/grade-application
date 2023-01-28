create table grade_scale
(
    grade_scale_id int identity(1, 1) primary key,
    letter_grade varchar(4) not null,
    grade_percent dec(2, 2) not null,
    GPA dec(2, 1) not null
)

;

create index ixdex_grade_percent
on grade_scale (grade_percent)