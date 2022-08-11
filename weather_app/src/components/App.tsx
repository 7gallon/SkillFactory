import  * as React from "react";
import "../styles/App.css";
import Header from "./header";
import Main from "./main";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    // const buttonName = "the button";
        return (
            <>
                <Header /*buttonName ={buttonName}*/ />
                <Main />
            </>
        );
}

export default App;