/**
 * @param {number[]} seats
 * @param {number[]} students
 * @return {number}
 */
var minMovesToSeat = function(seats, students) {
    let sortedSeats = seats.sort((a,b) => a-b);
    let sortedStudents = students.sort((a,b) => a-b);
    
    // console.log(sortedSeats, sortedStudents);
    let sum = 0;
    for(let i=0; i<seats.length; i++)
    {
        sum += Math.abs(sortedStudents[i] - sortedSeats[i]);
    }
    // console.log(sum);
    return sum;
};