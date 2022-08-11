import * as React from "react";

import "../styles/weekcasts.css"
import Table from "react-bootstrap/Table";

function Wforecasts(props) {
    // console.log(props);

    return (
        <Table>
            <tbody>
                <tr>
                    <td>
                        <span className="wtime">{props.dt_txt}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span className="wtemp">{props.temp} °C</span>
                    </td>
                    <td>
                        <span className="wmain">{props.main}</span>
                    </td>
                </tr>
            </tbody>
        </Table>
    );

}

export default Wforecasts;