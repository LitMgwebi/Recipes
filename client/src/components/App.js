import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";
import List from './CRUD/List'
import Delete from './CRUD/Delete'
import Detail from './CRUD/Detail'
import Update from './CRUD/Update'
import Create from './CRUD/Create'

import {
     BrowserRouter as Router,
     Routes,
     Route,
     Link
 } from "react-router-dom";

const App = props => {
     return(
          <Router>
               <div>
                    <navbar>
                         <Link to="/">Home</Link>
                         <Link to="/list">List</Link>
                         <Link to="/delete">Delete</Link>
                         <Link to="/detail">Detail</Link>
                         <Link to="/update">Update</Link>
                         <Link to="/create">Create</Link>
                    </navbar>
                    <Routes>
                         <Route path="/" element={<HomePage />} />
                         <Route path="/list" index element={<List />} />
                         <Route path="/delete/:id" element={<Delete />} />
                         <Route path="/detail/:id" element={<Detail />} />
                         <Route path="/update/:id" element={<Update />} />
                         <Route path="/create" element={<Create />} />
                    </Routes>
               </div>
          </Router>
     );
};

export default App
const appDiv = document.getElementById("app");
render(<App />, appDiv);