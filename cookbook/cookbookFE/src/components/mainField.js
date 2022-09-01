import React, {Component} from "react";

import "../styles/mainField.css";

let test;

//запрос рецепта по API


function MainField(props) {
    console.log(props.showRecipe);
    if (!props.showRecipe.length) {
    test = <ul><li>.....ты точно его ел и точно неправильно</li><li>.....жидкий или твердый</li><li>.....на сытый желудок ;)</li></ul>;
    }
    else {
        test = props.showRecipe;
    }
    console.log(test);
    return (
        <div>
            {test}
        </div>
    )
}

export default MainField;