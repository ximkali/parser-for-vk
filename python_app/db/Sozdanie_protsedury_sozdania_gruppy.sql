Use dimas; 
# Поменяй название базы
drop procedure if exists sozdanie_gruppy;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sozdanie_gruppy`(
	group_name varchar (100),
    group_vk_id int,
    out result tinyint,
    out error_id int
)
begin
	
    if
		group_name not in (select group_name from vk_group) 
		and 
		group_vk_id not in (select group_vk_id from vk_group)
    then
		insert into vk_group (idgroup_id, group_vk_id, group_name)
		values (default, group_vk_id, group_name);
        set result = 1;
	else
		set result = 0;
        set error_id = group_vk_id;
	end if;
# Данной функции поступает на вход два параметра: group_name и group_vk_id
# По данным параметрам проверяется наличие в таблице vk_group группы вк
# Если группа уже есть в базе, то возвращается 0, если ее нет, то
# Создается запись и возвращается 1
end$$
DELIMITER ;