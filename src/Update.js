import React,{useEffect, useState} from 'react';
import{ useNavigate, useParams} from 'react-router-dom';
import {useForm} from 'react-hook-form';
import {getUserById} from '../Database/DBservices';
import { updateUser } from '../Database/DBservices';

const Update= ()=> {
         const {id}=useParams()
         const {register, handleSubmit,setValue}= useForm()
         const [user, setUser]=useState({})

         useEffect(()=>{
            getUserFromDB()
         },[])
         
          const navigate= useNavigate()

         const getUserFromDB=async()=>{
           const userObject= await getUserById(id)
           //console.log(userObject.data)
            setUser(userObject.data)
         }

         const getUpdateUser=(userObj)=>{
            console.log(userObj)
            updateUser(userObj)
            navigate("/display")


         }
    return(<>

        <div className='container'>
        <h1 className='text-primary'> this is User Page</h1>
         <div className='row col-md-3'>
            <form onSubmit={handleSubmit(getUpdateUser)}>

            <div className="mb-3">
              <input type="text" className="form-control"{...register("id")}
              {...setValue("id", user.id)}/>
              </div>

            <div className="mb-3">
              <input type="text" className="form-control"  placeholder="Firstname" {...register("firstname")}
              {...setValue("firstname", user.firstname)}/>
                   </div>
                      <div className="mb-3">

                   <input type="text" className="form-control" placeholder="Lastname" {...register("lastname")}
                   {...setValue("lastname", user.lastname)}/>
                    </div>

                    <div className="mb-3">
              <input type="text" className="form-control"  placeholder="Mobile" {...register("mobile")}
              {...setValue("mobile", user.mobile)}/>
                   </div>
                      <div className="mb-3">

                   <input type="text" className="form-control" placeholder="Email" {...register("email")}
                   {...setValue("email", user.email)}/>
                    </div>

                    <div className="mb-3">
              <input type="text" className="form-control"  placeholder="Username" {...register("username")}
              {...setValue("username", user.username)}/>
                   </div>
                      <div className="mb-3">

                   <input type="text" className="form-control" placeholder="Password" {...register("password")}
                   {...setValue("password", user.password)}/>
                    </div>
                    <div className="mb-3 text-center">
                        <input type="submit" className="btn btn-outline-success" value="Update register"/>

                    </div>
  
            </form>

         </div>

        </div>

        </>
    )
}
export default Update