domain = "https://api.vk.com/method/"
access_data = "access_token={access_token}&v={ver_vk_api}"

need_to_replace = ["TEMP_METHOD_1","TEMP_COUNT","TEMP_OFFSET","TEMP_METHOD_2","TEMP_OWNER_ID","TEMP_POST_ID","TEMP_LIKES","TEMP_METHOD_3","TEMP_OWNER_COMMENT_ID"]
element_to_replace = ["wall.get?domain={group_name}","count={count}","offset={offset}",
"wall.getComments?owner_id={owner_id}","post_id={post_id}","","","","","","","","","","","","","","","","","","","","","","",""]


ULR_TYPE_1 = domain + "TEMP_METHOD_1&TEMP_COUNT&TEMP_OFFSET&" + access_data
print(ULR_TYPE_1)

ULR_TYPE_2 = domain + "TEMP_METHOD_2?TEMP_OWNER_ID&TEMP_POST_ID&TEMP_COUNT&TEMP_LIKES&" + access_data
print(ULR_TYPE_2)

ULR_TYPE_3 = domain + "TEMP_METHOD_3?TEMP_OWNER_ID&TEMP_OWNER_COMMENT_ID&" + access_data
print(ULR_TYPE_3)

url_get_post = ULR_TYPE_1
url_get_comments = ULR_TYPE_2
url_get_comment = ULR_TYPE_3



url_string = ULR_TYPE_1

def TEMP_REPLACE(url_string,need_to_replace,element_to_replace):
    if url_string:
        for i in range (len(need_to_replace)):
            url_string.replace(need_to_replace[i],element_to_replace[i])
    return url_string




def ulrmaker(TEMP_REPLACE):
    if url_string == "":
        return "NUL STRING"
    if url_string == url_get_post:
        TEMP_REPLACE(url_string,need_to_replace,element_to_replace)
        return url_string
    if url_string == url_get_comments:
        TEMP_REPLACE(url_string,need_to_replace,element_to_replace)
        return url_string
    if url_string == url_get_comment:
        TEMP_REPLACE(url_string,need_to_replace,element_to_replace)
        return url_string
    else: 
        return "NOT DIFFEREND TYPE OF URL"