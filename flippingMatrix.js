function flippingMatrix(matrix) {
    // Write your code here
    const length = matrix.length / 2;
    let max = 0;
    let total = 0;
    for ( let i = 0; i < length; i++ ){
        for ( let j = 0; j < length; j++ ){
            max = Number.MIN_VALUE;
            max = Math.max( matrix[ i ][ j ], max);
            max = Math.max( matrix[ i ][ 2 * length - j - 1 ], max);
            max = Math.max( matrix[ 2 * length - i - 1][ j ], max);
            max = Math.max( matrix[ 2 * length - i - 1 ][ 2 * length - j - 1 ], max);
            
            total += max;
        }
    }
    return total;
}