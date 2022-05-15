const Elpribor = function(name, power) {
    this.name = name;
    this.getPower = function(){
        return power;
    }
    this.turnOn = function (){
        return console.log(`${name} is on. It consumes ${this.getPower()} watts of energy.`)
    }
    this.turnOff = function (){
        return console.log(`${name} is off.`)
        }
}

const Smallep = function (name, power, size) {
    this.name = name;
    this.power = power;
    this.size = size;
    this.turnOff = function() {
        return console.log(`${name} is off. You can store it somewhere because it's ${size}.`)
    }
}

Smallep.prototype = new Elpribor();

const fridge = new Elpribor('refrigerator', 300);
const shaver = new Smallep('shaver', 100, 'small');
fridge.turnOff();
shaver.turnOff();

setInterval(() => fridge.turnOn(), 2000);
setTimeout(() => setInterval(() => fridge.turnOff(), 2000),1000)
