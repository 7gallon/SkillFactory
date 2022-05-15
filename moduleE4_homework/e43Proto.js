//1
Ptype = {
    z:'Last'
};

alfabet = Object.create(Ptype);
alfabet.a = 'First';
alfabet.b = 'Second';

function ownProperties(obj) {
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            console.log(key);
        }
    }
}
ownProperties(alfabet);

//2

inStr = 'f';

function isKeyName(name, obj){
    for (let key in obj) {
        return key === name;
    }
}

console.log(isKeyName(inStr, alfabet));

//3
function fNoProt() {
    return Object.create(null)
}
tmp = fNoProt();
console.log(typeof tmp)

