def solution(id_pw, db):
    for user_id, user_pw in db:
        if user_id == id_pw[0]:     
            if user_pw == id_pw[1]:  
                return "login"
            else:
                return "wrong pw"

    return "fail"





