Use dimas; 

drop procedure if exists sozdanie_postov;

delimiter $$

create procedure sozdanie_postov(
	id_posta int,
    views int,
    post_date date,
    group_id int,
    out result tinyint,
    out error_id int
)
begin

    if
		id_posta not in (select post_vk_id from post)
    then
		insert into post (post_vk_id, views_of_post, post_date, group_vk_id)
		values (id_posta, views, post_date, group_id);
		set result = 1;
    else
		set result = 0;
        set error_id = post_vk_id;
	end if;

end $$
delimiter ;