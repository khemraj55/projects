import React from 'react'
import {useForm} from 'react-hook-form'
import {registerUser} from '../Database/DBservices';

function User() {
    const {register, handleSubmit,reset}=useForm()

    const getRegisterUser=(userObj)=>{
        console.log(userObj)
        registerUser(userObj)
        reset()
        
    }
    return(
        <>
        <div className='container'>
        <h1 className='text-primary'> this is User Page</h1>
         <div className='row col-md-3'>
            <form onSubmit={handleSubmit(getRegisterUser)}>
            <div class="mb-3">
              <input type="text" className="form-control"  placeholder="Firstname" 
              {...register("firstname",{required:"this field is required..."})}/>
              
                   </div>

                      <div className="mb-3">

                   <input type="text" className="form-control" placeholder="Lastname"
    {...register("lastname",{required:"this field is required...",
                    minLength:{
                        value:3,
                        message:"minium 3 character required"
                    },
                    maxLength:{
                        value:15,
                        message:"minium 15 character required"
                    } })}/>
            
                    </div>

                    <div className="mb-3">
              <input type="text" className="form-control"  placeholder="Mobile"
               {...register("mobile",{required:"this field is required..",
                   pattern:{
                          value:/^[6789]{1}[0-9]{9}$/,
                          message:"invalid mobile number"
                   }          
            })}/>
        
                   </div>
                      <div className="mb-3">

                   <input type="text" className="form-control" placeholder="Email" {...register("email")}/>
                    </div>

                    <div className="mb-3">
              <input type="text" className="form-control"  placeholder="Username" {...register("username")}/>
                   </div>
                      <div className="mb-3">

                   <input type="text" className="form-control" placeholder="Password" {...register("password")}/>
                    </div>
                    <div className="mb-3 text-center">
                        <input type="submit" className="btn btn-outline-success" value="Register"/>

                    </div>
  
            </form>

         </div>

        </div>
        </>
    )
}
export default User