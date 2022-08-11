import * as React from "react";
import "../styles/header.css"


function Header(props) {
    // let [counted, setNewCounted] = React.useState(0);
    // const handleClick = () => {
    //     setNewCounted(counted + 1);
    //     console.log("Hello");
    // }
    return (
        <header>
            this is your forecast
            {/*<button className="btn" onClick={handleClick}>*/}
            {/*    {props.buttonName} clicked: {counted} times*/}
            {/*</button>*/}
        </header>
    )

}

export default Header;