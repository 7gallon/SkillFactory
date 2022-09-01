import React from "react";
import ReactDOM from "react-dom";

import App from "./components/App";

// const cors = require('cors');
// const corsOptions ={
//     origin:'http://localhost:8080',
//     credentials:true,            //access-control-allow-credentials:true
//     optionSuccessStatus:200
// }
// App.use(cors(corsOptions));

// let cors = require('cors')
//
// App.use(cors())

ReactDOM.render(<App/>, document.getElementById("root"));
