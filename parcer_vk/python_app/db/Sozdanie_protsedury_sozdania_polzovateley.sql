Use dimas; 

drop procedure if exists sozdanie_polzovatelei;

delimiter $$

create procedure sozdanie_polzovatelei(
	user_id int,
    is_bot TINYINT(1),
    out result tinyint,
    out error_id int
)
begin

	if
		user_id not in (select user_id from users)
    then
		insert into users (vk_id, is_bot)
		values (user_id, is_bot);
        set result = 1;
	else
		set result = 0;
        set error_id = vk_id;
	end if;

end $$
delimiter ;