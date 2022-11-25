import React from "react";
import User from "./User";
import Update from "./Update";
import Display from "./Display";
import Home from "./Home";
import About from "./About";
import {NavLink, Routes, Route} from 'react-router-dom'

function App () {
  return (
    <>
     <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
  <div className="container-fluid">
    <a className="navbar-brand" href="#">Navbar</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarNav">
      <ul className="navbar-nav">
           
      <li className="nav-item">
        <NavLink to="about" className="nav-link">About</NavLink>
        </li>   
      <li className="nav-item">
        <NavLink to="home" className="nav-link">Home</NavLink>
        </li>
        <li className="nav-item">
        <NavLink to="display" className="nav-link">Display</NavLink>
        </li>
        <li className="nav-item">
        <NavLink to="Update" className="nav-link">Update</NavLink>
        </li>
        <li className="nav-item">
        <NavLink to="user" className="nav-link">User</NavLink>
        </li>
      </ul>
    </div>
  </div>
</nav>

    
         <Routes>
            <Route path="/home" element={<Home/>}></Route>
            <Route path="/about" element={<About/>}></Route>
            
            <Route path="/display" element={<Display/>}></Route>
             
             <Route path="/editUser/:id" element={<Update/>}></Route>
            <Route path="/" element={<Home/>}></Route>
            <Route path="/user" element={<User/>}></Route>

            
         </Routes>
  
        </>
    )
}export default App
