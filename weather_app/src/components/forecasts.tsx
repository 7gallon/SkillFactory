import * as React from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import {YMaps, Map} from "@pbe/react-yandex-maps";
import Hforecasts from "./hforecast";
import Wforecasts from "./weekcasts";

import "../styles/forecasts.css"




function Forecasts(props) {
    // console.log(props)
    const [forecast, setForecast] = React.useState([]);
    const [weekcast, setWeekcast] = React.useState([]);
    const timestamps = 16;

    if(!forecast.length) {
        const api_key = "515a1d0a66987e7fccc5c6907645a4ca";
        const url_ = `https://api.openweathermap.org/data/2.5/forecast?lat=${props.lat}&lon=${props.lng}&cnt=${timestamps}&units=metric&appid=${api_key}`;
        axios.get(url_).then(res => {
            // console.log(res.data.list);
            setForecast(res.data.list);

        });
    }

    if(!weekcast.length) {
        const api_key = "515a1d0a66987e7fccc5c6907645a4ca";
        const url_ = `https://api.openweathermap.org/data/2.5/forecast?lat=${props.lat}&lon=${props.lng}&units=metric&appid=${api_key}`;
        axios.get(url_).then(res => {
            // console.log(res.data.list);
            setWeekcast(res.data.list);

        });
    }

    return (

        <Table striped bordered hover>
            <thead><tr>
                    <th colSpan={3}>
                    <YMaps>
                        <div className="map">
                            <Map defaultState={{ center: [props.lat, props.lng], zoom: 9 }} width="100%" />
                        </div>
                    </YMaps>
                </th>
            </tr>
            <tr><th>At this moment</th><th>Next two days (3hrs interval)</th><th>Next five days (3hrs interval)</th></tr></thead>
            <tbody>
            <tr>
                <td className="nowWeather">
                    <table>
                        <tbody>
                            <tr>
                                <td><span className="names">temp [°C]</span><h1>{props.Temp}</h1></td>
                                <td><span className="names">wind speed [m/sec]</span><h1>{props.WindSpeed}</h1></td>
                                <td><span className="names">sky</span><h1>{props.Main}</h1></td>
                            </tr>
                            <tr>
                                <td><span className="names">feel [°C]</span><h1>{props.Feel}</h1></td>
                                <td><span className="names">wind gust [m/sec]</span><h1>{props.WindGust}</h1></td>
                                <td><span className="names">P atm. [mmHg]</span><h1>{(props.Pres/1.333).toFixed(2)}</h1></td>
                                <td><span className="names">Humidity [%]</span><h1>{props.Hum}</h1></td>
                            </tr>
                        </tbody>
                    </table>
                </td>
                <td>
                    {forecast.map(hourlyForcast =>  <Hforecasts key={hourlyForcast.main.temp_min}
                                                                dt_txt = {hourlyForcast.dt_txt}
                                                                temp = {hourlyForcast.main.temp}
                                                                main = {hourlyForcast.weather[0].main} />)}
                </td>
                <td>
                    {weekcast.map(weeklyForcast =>  <Wforecasts key={weeklyForcast.main.temp_min}
                                                                dt_txt = {weeklyForcast.dt_txt}
                                                                temp = {weeklyForcast.main.temp}
                                                                main = {weeklyForcast.weather[0].main} />)}

                </td>
            </tr>
            </tbody>
        </Table>
    );
}


export default Forecasts;
