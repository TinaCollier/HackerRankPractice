const squareMatrix = [[1,2,3], [1,2,3], [1,2,3]];

function diagonalDifference(arr) {
    // Write your code here
    let length = arr.length - 1;
    let rightDiagonal = 0;
    for ( let i = 0; i < arr.length; i++ ){
        rightDiagonal += arr[i][i];
    }
    let leftDiagonal = 0;
    for ( let i = 0; i < arr.length; i++ ){
        leftDiagonal += arr[i][length];
        length -= 1;
    }
    return Math.abs(rightDiagonal - leftDiagonal)
}

console.log(diagonalDifference(squareMatrix));