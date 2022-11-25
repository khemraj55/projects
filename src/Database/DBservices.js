import axios from "axios"

let url="http://127.0.0.1:8088/user"
export const registerUser=(userObject)=>{                        // to store user id in db
    return axios.post(url,userObject)
}

export const getAllUser=()=>{                           // to get all user from db
    return axios.get(url)
}

export const userDeleteById=(userId)=>{               // to delete user based on id
    return axios.delete(url+"/"+userId)                // http://127.0.0.1:8088/user/2
}

export const getUserById=(userId)=>{
    return axios.get(url+"/"+userId)
}

export const updateUser=(userObject)=>{                     //to update user based on id
    return axios.put(url+"/"+userObject.id, userObject)
}