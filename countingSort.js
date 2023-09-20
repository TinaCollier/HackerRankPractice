const list = [1,2,5,6,3,];

function countingSort(arr) {
    // Write your code here
    let result = new Array(100).fill(0);;
    arr.forEach( element => result[ element ]++);
    return result;
}

console.log(countingSort(list));