Use dimas; 

drop procedure if exists sozdanie_kommentatiev;

delimiter $$

create procedure sozdanie_kommentatiev(
	comment_id int,
    text_comm mediumtext,
    likes int,
    comment_date date,
    user_id int,
    post_vk_id int,
    out result tinyint,
    out error_id int
)
begin

	if
		attachment_vk_id not in (select attachment_vk_id from attachments)
    then
		insert into comments (
        vk_comment_id,
        com_text,
        likes_ammount,
        comment_date,
        users_vk_id,
        post_vk_id
        )
		values (
        comment_id,
        text_comm,
        likes,
        comment_date,
        user_id,
        post_vk_id
        );
        set result = 1;
	else
		set result = 0;
        set error_id = comment_id;
	end if;

end $$
delimiter ;