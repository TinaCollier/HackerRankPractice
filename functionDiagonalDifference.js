function diagonalDifference(arr) {
    let mainSum = 0, secondarySum = 0;
    for (let row = 0; row < arr.length; row++) {
        mainSum += arr[row][row];
        secondarySum += arr[row][arr.length - row - 1];
    }
    let diff = mainSum - secondarySum;
    return Math.abs(diff);

}