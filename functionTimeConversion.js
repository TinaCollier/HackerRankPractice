const time = '12:45:54PM';


function timeConversion(s) {
// Write your code here

s = s.split(':');

let hours = Number(s[0]);
let minutes = s[1];
let seconds = s[2];

var militaryTime = '';

let removedAMPM = seconds.slice(0 -2);

if(removedAMPM === 'PM' && hours != 12){
    hours += 12;
}
else if(removedAMPM === 'AM' && hours === 12){
    hours = '00'
}
else if (removedAMPM === 'AM' && hours === 11){
    return hours;
} 
else if(removedAMPM === 'AM' && hours > 0 && hours < 11){
    hours = `0${hours}`;
}

const fixedSeconds = seconds.slice(0, -2)

militaryTime = `${hours}:${minutes}:${fixedSeconds}`;

return militaryTime
}

console.log(timeConversion(time));