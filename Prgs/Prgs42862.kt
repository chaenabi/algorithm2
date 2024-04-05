
// 체육복
// https://school.programmers.co.kr/learn/courses/30/lessons/42862
// kotlin 

class Solution42862 {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        val a = IntArray(n + 1) { 1 }
        val stlist: Set<Int> = lost.intersect(reserve.toSet())
        lost.forEach { e -> a[e] = 0 }
        reserve.forEach { e -> 
          if (!stlist.contains(e)) {
            a[e] = 2 
          } else {
            a[e] = 1
          }
        }

        for (i in 1 until a.size) {
          if (a[i] == 2) {
            if (i > 0 && a[i - 1] == 0) {
              a[i - 1] = 1
              a[i] = 1
            } 
            if (i < a.size - 1 && a[i] == 2 && a[i + 1] == 0) {
              a[i + 1] = 1
              a[i] = 1
            }
          }
        }

        return a.filter { it > 0 }.size - 1 // 0번째 인덱스 제외를 위한 -1
    }
}

fun main() {
    val lost = intArrayOf(1, 2, 4)
    val reserve = intArrayOf(1, 3)
    val solution = Solution42862()
    println(solution.solution(5, lost, reserve))
}