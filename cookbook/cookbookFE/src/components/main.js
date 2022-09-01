import React, {Component} from "react";
import axios from "axios";

import "../styles/main.css";
import LeftPanel from "./leftPanel";
import MainField from "./mainField";

function Main() {
    const [recipe, setRecipe] = React.useState([]);
    let getRecipe = (id) => {
        // if (!recipe) {
            axios.get(`http://localhost:8000/api/recipes/${id}`).then(res => {
                console.log(res.data);
                console.log("запрос");
                setRecipe(res.data);
            })

        // }
    }
    return (
        <main>
            <table>
                <tbody>
                    <tr>
                        <td id="leftpanel">
                            <LeftPanel getRecipe={getRecipe}/>
                        </td>
                        <td id="mainfield">
                            <MainField showRecipe={recipe} />
                        </td>
                    </tr>
                </tbody>
            </table>
        </main>
    );
}

export default Main;