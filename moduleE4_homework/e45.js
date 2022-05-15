class Elpribor {
    constructor(name, power) {
        this.name = name;
        this.power = power;
    }
        getPower() {
            return this.power;
        }
        turnOn() {
            return console.log(`${this.name} is on. It consumes ${this.getPower()} watts of energy.`)
        }
        turnOff() {
            return console.log(`${this.name} is off.`)
        }

}

class Smallep extends Elpribor {
    constructor(name, power,size) {
        super(name, power);
        this.size = size;
    }
    turnOff() {
        return console.log(`${this.name} is off. You can store it somewhere because it's ${this.size}.`)
    }
}


const fridge = new Elpribor('refrigerator', 300);
const shaver = new Smallep('shaver', 100, 'small');
fridge.turnOff();
shaver.turnOff();

setInterval(() => fridge.turnOn(), 2000);
setTimeout(() => setInterval(() => fridge.turnOff(), 2000),1000)
