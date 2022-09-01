import React, {Component} from "react";

import "../styles/App.css";
import Header from "./header";
import Main from "./main";

class App extends Component {
    render() {
        return (
            <>
                <Header />
                <Main />
                <a href="http://localhost:8000/openapi">API docs</a>
            </>
        );
    }
}

export default App;