---
date: '2025-12-24T16:55:18+08:00'
draft: false
title: 'How to Solve Fixed-Length Sliding Window Problems!'
tags: ['Algorithm', 'Sliding Window']

cover:
  image: 'images/cover-sliding-window.svg'
  alt: 'fixed length sliding window' # alt text
  caption: '<text>' # display caption under cover
  relative: false # when using page bundles set this to true
---

## One Classic Problem

Given an integer array `nums` consisting of `n` elements, and an integer `k`, find the **maximum sum** of any contiguous subarray of size `k`.

**Example:**

> Input: arr = [2, 1, 5, 1, 3, 2], k = 3
>
> Output: 9
>
> Explanation: Subarray [5, 1, 3] has the maximum sum 9

**Constraints:**

- `n == nums.length`
- `1 <= k <= n <= 105`
- `-104 <= nums[i] <= 104`

### Brute Force Approach

The simplest solution checks each subarray independently:
![](images/sliding-window-brute-force.png)

```javascript
const findMaxSum = function (nums, k) {
  // Initialize maxSum to the smallest possible number
  // Using -Infinity ensures it works with negative numbers
  let maxSum = -Infinity

  // Loop through all possible starting positions
  // Last valid starting position is nums.length - k
  for (let i = 0; i <= nums.length - k; i++) {
    let currentSum = 0

    // Calculate sum of k elements starting at i
    for (let j = 0; j < k; j++) {
      currentSum += nums[i + j]
    }

    // Update maxSum if current sum is larger
    maxSum = Math.max(maxSum, currentSum)
  }

  return maxSum
}
```

This approach uses nested loops. The outer loop runs from `0` to `n - k` (`n - k + 1` iterations), and for each starting position, the inner loop calculates the sum of the next `k` elements. The variable `maxSum` tracks the maximum sum found.

**Complexity Analysis:**

- **Time Complexity**: O(n × k)
  - Outer loop: O(n) iterations
  - Inner loop: O(k) iterations per outer loop
- **Space Complexity:** O(1) - Only a few variables are used regardless of input size

**Why is this inefficient?** Many elements are summed multiple times. For example, in the array `[2, 1, 5, 1, 3, 2`] with `k = 3`:

- Element at index `2` (value `5`) is summed in:
  - Window starting at 0: `2+1+5`
  - Window starting at 1: `1+5+1`
  - Window starting at 2: `5+1+3`

The brute-force approach recalculates each subarray from scratch, resulting in redundant computations. Can we compute each element's contribution only once and calculate subarray sums in O(1) time?
**Yes**—this is where the sliding window technique shines.

### The Sliding Window Technique

**Fixed-length sliding window problems** involve analyzing **a sequence (array or string)** using a "window" of **constant size** that **moves sequentially** from start to end. Imagine looking through a fixed-width frame that shifts one position at a time. The goal is to efficiently compute metrics (sum, average, maximum, etc.) for every consecutive segment of that exact length.

**Key Characteristics:**

- **Constant Window Size (k):** The subarray/substring length remains fixed
- **Sequential Movement:** The window advances one element at a time—one element exits (left) and a new element enters (right)
- **Efficiency Goal:** Avoid recalculations by updating computations **incrementally** based on the single element entering and the single element leaving

**Applying Sliding Window to Our Problem** -
Observe that when the window slides, only one element changes: a new element enters on the right, and the leftmost element exits. Instead of recalculating the sum for each window (O(k) per window), we can update it in O(1) by:

1. Subtracting the element that just left
2. Adding the new element that just entered

![](images/sliding-window-two-loop.png)

{{ $image := resources.Get "images/sliding-window-two-loop.png" }}

```javascript
const findMaxSum = function (nums, k) {
  // Calculate the sum of the first window (elements 0 to k-1)
  let currentSum = 0
  for (let i = 0; i < k; i++) {
    currentSum += nums[i]
  }

  // Initialize maxSum with the sum of the first window
  let maxSum = currentSum
  // Slide the window across the rest of the array, one element at a time
  for (let i = k; i < nums.length; i++) {
    // Update the window sum:
    // Add new element (entering) and subtract old element (leaving)
    currentSum += nums[i] - nums[i - k]

    // Update maxSum with the larger value (current window sum or previous max)
    maxSum = Math.max(maxSum, currentSum)
  }

  return maxSum
}
```

This is the sliding window solution. We first **Calculate the sum of the first window** (elements `0` to `k-1`), then **Slide the window** one element at a time:

- Subtract the element leaving the window (leftmost)
- Add the element entering the window (rightmost)
- Update the maximum sum

**Why is it efficient?**
You maintain a running count or state. When the window slides:

1. You **remove** the effect of the element that just left the window.
2. You **add** the effect of the new element that just entered.

This update is typically an O(1) operation, making the whole algorithm O(n). This redundant calculation of brute force is what the sliding window technique eliminates!

The algorithm achieves the optimal time complexity for this problem. The sliding window technique is the most efficient approach for finding maximum sum/average of fixed-size contiguous subarrays.

### Optimized Single-Loop Implementation🍎

The original code uses two loops: one to calculate the first window and then a loop to slide the window. We can actually do this by using a single loop that goes from `0` to `n-1`. Even with a single loop, we still complete the first window before sliding.

```javascript
// The two-loop solution can be condensed into a single loop that builds and slides the window simultaneously:
const findMaxSum = function (nums, k) {
  let maxSum = -Infinity
  let currentSum = 0

  for (let i = 0; i < nums.length; i++) {
    // Expand the window by including the current element
    currentSum += nums[i]

    // Check if the window has reached size k
    // left represents the start index of the current window
    let left = i - k + 1
    // If the window hasn't reached size k yet, skip updating maxSum
    if (left < 0) {
      continue
    }

    // Update maximum sum
    maxSum = Math.max(maxSum, currentSum)

    // Prepare for the next window by removing the element that's about to slide out
    currentSum -= nums[left]
  }

  return maxSum
}
```

**Complexity Analysis:**

- **Time Complexity:** O(n) - Single pass through the array with constant-time operations per element
- **Space Complexity:** O(1) - Only a few variables used

### **The Fixed-Length Sliding Window Pattern🤩**

This single-loop implementation can be summarized in three steps: **In - Update - Out**.

1. **In:** The element at index `i` enters the window. Update the relevant statistics. If the window's left boundary `i − k + 1` is negative, the first window is not yet complete. Repeat step 1.

```javascript
// 1. In
currentSum += nums[i]

let left = i - k + 1
if (left < 0) {
  continue
}
```

2. **Update:** Update the answer, typically by comparing the current window's value (e.g., maximum or minimum) with the stored result.

```javascript
// 2. Update
maxSum = Math.max(maxSum, currentSum)
```

3. **Out:** The element at index `i − k + 1` leaves the window. Update the relevant statistics to prepare for the next iteration.

```javascript
// 3. Out
currentSum -= nums[left]
```

The above three steps are applicable to all fixed-length sliding window problems.

**Q&A**

- **Q:** Why is the left endpoint `i - k + 1` when the right endpoint is at index `i`?
- **A:** For a window `[L, R`] (inclusive), the element count is `R - L + 1`. For a window of size `k`, we have `R - L + 1 = k`. Solving for `L` gives `L = R - k + 1`. Thus, when the right endpoint is `i`, the left endpoint is `i - k + 1`.

### Fixed-Length Sliding Window: Common Use Cases

The sliding window technique is widely used to efficiently process sequential data by maintaining a fixed-size subset.

1. Common Problem Types

- **Aggregations:** Finding the maximum, minimum, or average value (e.g., sum, average) of all contiguous subarrays of a fixed size k.
- **Pattern Matching:** Checking for duplicates, specific sequences, or anagrams within any window of length k.
- **Constrained Search:** Finding a window of size k that meets a certain condition (e.g., a sum less than a target value).

2. Real-World Applications

- **Finance:** Analyzing the highest profit or volatility over any k-day period.
- **Systems Monitoring:** Tracking peak bandwidth, server load, or errors in any k-minute interval.
- **Data Streams:** Calculating moving averages or detecting trends in real-time sensor or time-series data.
