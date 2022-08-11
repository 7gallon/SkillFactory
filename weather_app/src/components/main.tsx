import * as React from "react";
import Forecasts from "./forecasts";
import Alerts from "./Alerts";

import "../styles/main.css"
import {Component} from "react";
import axios from "axios";


function Main()  {
    const [lat, setLat] = React.useState(null);
    const [lng, setLng] = React.useState(null);
    const [city, setCity] = React.useState(null);
    const [district, setDistrict] = React.useState(null);
    const [curTemp, setcurTemp] = React.useState(null);
    const [curFeel, setcurFeel] = React.useState(null);
    const [mainWeather, setMainWeather] = React.useState(null);
    const [curWind, setCurWind] = React.useState(null);
    const [curGust, setCurGust] = React.useState(null);
    const [curPres, setCurPres] = React.useState(null);
    const [curHum, setCurHum] = React.useState(null);

    navigator.geolocation.getCurrentPosition((position) => {
        setLat(position.coords.latitude);
        setLng(position.coords.longitude);
    });

    if (!city && !district) {
        const url_ = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${lng}&localityLanguage=en`;
        // console.log(url_);
        axios.get(url_).then(res => {
            // console.log(res.data);
            console.log(res.data.locality);
            setCity(res.data.city);
            setDistrict(res.data.locality);
        });
    }

    if(!curTemp) {
        const api_key = "515a1d0a66987e7fccc5c6907645a4ca";
        const url_ = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&units=metric&appid=${api_key}`;
        // console.log(url_);
        axios.get(url_).then(weather => {
            console.log(weather.data.weather[0].main);
            setcurTemp(weather.data.main.temp);
            setcurFeel(weather.data.main.feels_like);
            setMainWeather(weather.data.weather[0].main);
            setCurWind(weather.data.wind.speed);
            setCurGust(weather.data.wind.gust);
            setCurPres(weather.data.main.pressure);
            setCurHum(weather.data.main.humidity);
        });
    }

    // использовать переменную {geolocation} из Geolocation API
    let alertText = <b>you're currently in <h2>{city} : {district}</h2>[{lat} : {lng}]   change it here: [выпадающий список]</b>;

    // let curTemp = curWeather.children.main
    return (
        <main>
            <div>
                <Alerts>{alertText}</Alerts>
                <Forecasts Temp ={(curTemp)}
                           Feel ={(curFeel)}
                           Main ={mainWeather}
                           WindSpeed ={curWind}
                           WindGust ={curGust}
                           Pres ={curPres}
                           Hum ={curHum}
                           lat ={lat}
                           lng ={lng}
                />
            </div>
        </main>
    )

}

export default Main;