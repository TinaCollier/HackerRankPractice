// finds the ratio of positive, negative, and zero numbers in an array.

const array = [1, 1, 0, -1, -1];

function plusMinus(arr) {
    // Write your code here
    let posNum = 0;
    let negNum = 0;
    let zeroNum = 0;
    const length = arr.length;
    arr.forEach((num) => {
        if(num > 0){
            posNum++
        }
        else if(num < 0){
            negNum++;
        } else {
            zeroNum++;
        }
    }
    )
    // to the sixth decimal point
    console.log((posNum/length).toFixed(6));
    console.log((negNum/length).toFixed(6));
    console.log((zeroNum/length).toFixed(6));
}


console.log(plusMinus(array));