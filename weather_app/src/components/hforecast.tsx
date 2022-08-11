import * as React from "react";
import "../styles/hforecast.css"
import Table from "react-bootstrap/Table";

function Hforecasts(props) {
    // console.log(props);

    return (
        <Table>
            <tbody>
                <tr>
                    <td>
                        <span className="htime">{props.dt_txt}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span className="htemp">{props.temp}°C</span>
                    </td>
                    <td>
                        <span className="hmain">{props.main}</span>
                    </td>
                </tr>
            </tbody>
        </Table>
    );

}

export default Hforecasts;