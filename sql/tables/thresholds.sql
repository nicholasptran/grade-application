create table dbo.thresholds
(
    threshold_id int identity(1,1) primary key,
    date datetime not null,
    available_points int not null
)