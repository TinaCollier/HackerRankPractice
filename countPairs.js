const array = [1, 2, 1, 2, 1, 3, 2];
console.log(array);

function sockMerchant(n, ar) {
    let pairs = 0;
    let arr = [...ar].sort();

    for ( let i = 0; i < arr.length; i++ ) {
        if ( arr[i] == arr[i + 1] ) {
            pairs++;
            arr.shift();
        }
    }
    return pairs;
}



console.log(sockMerchant(array.length, array));