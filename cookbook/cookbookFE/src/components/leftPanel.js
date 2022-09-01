import React, {Component} from "react";
import axios from "axios";

import "../styles/leftPanel.css";


function LeftPanel(props) {
    console.log(props)
    // const [recipe, setRecipe] = React.useState([]);
    // let getRecipe = () => {
    //     if (!recipe.length) {
    //         axios.get("http://localhost:8000/api/recipes/").then(res => {
    //             console.log(res.data);
    //             console.log("запрос");
    //             setRecipe(res.data);
    //         })
    //
    //     }
    // }

    return (
        <div>
            <ul>
                <li onClick={props.getRecipe(1)}>#БöтеRБроtt --></li>
                <li onClick={props.getRecipe(2)}>#суП? --></li>
                <li onClick={props.getRecipe(3)}>#ужиN --></li>
            </ul>
        </div>
    )
}

export default LeftPanel;
