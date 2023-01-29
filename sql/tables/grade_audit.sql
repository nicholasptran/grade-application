create table grade_audit (
    grade_audit_id int IDENTITY(1,1) primary key,
    username varchar(100) not null,
    date datetime not null,
    grade_scale_id int not null foreign key references grade_scale(grade_scale_id)
)