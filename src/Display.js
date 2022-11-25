import React, {useEffect, useState} from 'react'
import { getAllUser, userDeleteById } from '../Database/DBservices'
import {NavLink} from 'react-router-dom'

function Display() {
    const [users, setUser]=useState([])

    useEffect(()=>{
        getUsersFromDB()
    })

    const getUsersFromDB=async()=>{
        const resp= await getAllUser()
        console.log(resp.data)
        setUser(resp.data)
    }
    const deleteUser=(userId)=>{
        alert("user for delete:"+userId)
        userDeleteById(userId)
    }
    return(
        <>
        <h1 className='text-primary'> this is Display Page</h1>
        <table className="table table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">firstName</th>
      <th scope="col">lastname</th>
      <th scope="col">mobile</th>
      <th scope="col">email</th>
      <th scope="col">username</th>
      <th scope="col">Password</th>
      <th scope="col">Edit</th>
      <th scope="col">delete</th>
    </tr>
  </thead>
  <tbody className="table-info">
         {
            users.map(u=>{
                return(<>
                  <tr>
                         <th scope="row">{u.id}</th>
                          <td>{u.firstname}</td>
                            <td>{u.lastname}</td>
                                <td>{u.mobile}</td>
                                <td>{u.email}</td>
                            <td>{u.username}</td>
                                <td>{u.password}</td>
                               <td>
                                <NavLink to={`/editUser/${u.id}`}>
                               <i class="bi bi-pencil-square text-primary"></i>
                               </NavLink>
                               </td>
                               <td>
                               <i class="bi bi-trash text-danger" onClick={()=>deleteUser(u.id)}></i>
                               </td>
                                    </tr>

                </>

                )
            }

            )

        }
   
    
  </tbody>
</table>

        </>
    )
}export default Display