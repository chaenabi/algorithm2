// 접근
// commands 배열 순회
// commands 인수값에 따라 array 자르고, 정렬. 
// k값에 위치한 값 리턴
class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        return commands.map { command ->
            array.copyOfRange(command[0] - 1, command[1]).sorted()[command[2] - 1]
        }.toIntArray()
    }
}
// 배열 접근 ArrayOutOfIndex 잡는 것이 더 어려웠던 문제.

fun main() {
    val array = intArrayOf(1, 5, 2, 6, 3, 7, 4)
    val commands = arrayOf(
        intArrayOf(2, 5, 3),
        intArrayOf(4, 4, 1),
        intArrayOf(1, 7, 3)
    )
    val solution = Solution()
    println(solution.solution(array, commands).toList())
}