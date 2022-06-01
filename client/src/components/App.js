import React, {Component} from "react";
import {render} from "react-dom";

function App() {
     return <h1>Hi world</h1>
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);