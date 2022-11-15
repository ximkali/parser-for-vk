Use dimas; 

drop procedure if exists sozdanie_prikreplennih;

delimiter $$

create procedure sozdanie_prikreplennih(
	attachment_id int,
    attachment_link varchar(200),
    comment_id int,
    out result tinyint,
    out error_id int
)
begin

	if
		attachment_vk_id not in (select attachment_vk_id from attachments)
    then
		insert into attachments (attachment_vk_id, attachment_link, comment_id)
		values (attachment_id, attachment_link, comment_id);
        set result = 1;
	else
		set result = 0;
        set error_id = attachment_id;
	end if;

end $$
delimiter ;