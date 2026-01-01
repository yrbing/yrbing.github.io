---
date: '2026-01-01T17:22:51+08:00'
draft: false
title: 'Reverse Thinking With Fixed-Length Sliding Window'
tags: ['Algorithm', 'Sliding Window', 'Reverse Thinking']

math: true

cover:
  image: 'images/cover-backward-thinking-slide-window.svg'
  alt: 'math typesetting' # alt text
  caption: '<text>' # display caption under cover
  hidden: false # only hide on current single page
---

We previously learned about the fixed-length sliding window technique, which typically involves sliding one element at a time. For a detailed explanation, refer to the article ------ 📝[How to Solve Fixed-Length Sliding Window Problems](/posts/fixed-length-sliding-window). Now, we encounter a new problem that also appears solvable with a sliding window, but with a slight twist🔗.

## A Tricky Problem

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `cardPoints` and the integer `k`, return the maximum score you can obtain.

**Example:**

> **Input:** cardPoints = [7,2,3,4,5,6,1], k = 3
>
> **Output:** 14
>
> **Explanation:** The optimal strategy is to take the first card on the left (7) and the two cards on the right (1 then 6), resulting in a score of 7 + 1 + 6 = 14.

**Constraints:**

- $1 <= cardPoints.length <= 10^5$
- $1 <= cardPoints[i] <= 10^4$
- $1 <= k <= cardPoints.length$

This problem aligns with the three key characteristics of fixed-length sliding window problems: Constant Window Size, Sequential Movement, and Efficiency Goal.

The only challenge is that the k elements are not necessarily consecutive in the original array. It's tricky to track `k` elements that can be taken from either end.

## Reverse Thinking

Since forward thinking isn't straightforward, we can try **reverse thinking**.

Let `m = cardPoints.length - k` (note that `m` can be `0`). We take `k` cards, leaving `m` cards.

Since the total points are fixed, _maximizing the points taken is equivalent to minimizing the points left_. Because we can only take from the ends, the remaining cards must be consecutive. Thus, the problem becomes:

**Find the minimum sum of a contiguous subarray of length m**,

which can be efficiently solved with a fixed-length sliding window.

```javascript
const maxScore = (cardPoints, k) => {
  const n = cardPoints.length
  const m = n - k // Cards to leave in window (can be 0)
  let windowSum = 0

  // Step 1: Calculate initial window sum (cards 0 to m-1)
  for (let i = 0; i < m; i++) {
    windowSum += cardPoints[i]
  }

  let totalSum = windowSum // Will become sum of all cards
  let minWindowSum = windowSum // Track minimum window sum found

  // Step 2: Slide the window
  for (let i = m; i < n; i++) {
    // Update total sum with current card
    totalSum += cardPoints[i]
    // Slide window: add new right element, remove left element
    windowSum += cardPoints[i] - cardPoints[i - m]
    // Record the minimum window sum found so far
    minWindowSum = Math.min(minWindowSum, windowSum)
  }

  // Max points = Total points - Minimum window sum
  return totalSum - minWindowSum
}
```

We can also use the [**In-Update-Out** pattern](/posts/fixed-length-sliding-window/#the-fixed-length-sliding-window-pattern), with a special condition to handle the case when the window size is zero (i.e., when n equals k).

```javascript
const maxScore = (cardPoints, k) => {
  const n = cardPoints.length
  const m = n - k
  let totalSum = 0
  let windowSum = 0
  let minWindowSum = Infinity

  for (let i = 0; i < n; i++) {
    totalSum += cardPoints[i]

    // Step 1: In
    windowSum += cardPoints[i]

    const left = i - m + 1
    if (left < 0) {
      continue
    }

    // Step 2: Update
    minWindowSum = Math.min(minWindowSum, windowSum)

    // Step 3: Out
    windowSum -= cardPoints[left]
  }

  // If n equals k, we take all cards, so return totalSum
  // Otherwise, return totalSum - minWindowSum
  return n === k ? totalSum : totalSum - minWindowSum
}
```

**Complexity Analysis**

- Time complexity: O(n), where n is the length of cardPoints.
- Space complexity: O(1)

## Alternative Approaches

### 1. Forward Thinking

While the reverse-thinking approach is more intuitive, forward thinking can also be applied directly.

The key insight is that the optimal solution must be one of the following `k + 1` combinations:

| Left Cards | Right Cards | Window Composition            |
| ---------- | ----------- | ----------------------------- |
| k          | 0           | First k elements              |
| k-1        | 1           | First (k-1) + last 1 element  |
| k-2        | 2           | First (k-2) + last 2 elements |
| …          | …           | …                             |
| 1          | k-1         | First 1 + last (k-1) elements |
| 0          | k           | Last k elements               |

**Approach 1: Backward Sliding Window**

We can slide the window backward, starting with all k cards from the left, and gradually replace left cards with right cards.

This looks like the window slides backward through the virtual concatenated array _[last k elements] + [first k elements]_.

```javascript
const maxScore = (cardPoints, k) => {
  let windowSum = 0
  // Initial window: first k elements (all from left)
  for (let i = 0; i < k; i++) {
    windowSum += cardPoints[i]
  }

  let maxSum = windowSum
  // Slide backward: replace one left card with one right card at a time
  for (let i = 1; i <= k; i++) {
    // Replace the (k-i)th card from the left with the ith card from the right
    windowSum += cardPoints[cardPoints.length - i] - cardPoints[k - i]
    maxSum = Math.max(maxSum, windowSum)
  }
  return maxSum
}
```

**Approach 2: Forward Sliding Window**

Similarly, we can slide forward by starting with the last k cards and gradually replacing right cards with left cards.

```javascript
const maxScore = (cardPoints, k) => {
  const n = cardPoints.length
  let windowSum = 0
  // initial window: last k elements (all from right)
  for (let i = n - k; i < n; i++) {
    windowSum += cardPoints[i]
  }

  let maxSum = windowSum
  // Slide forward: replace one right card with one left card at a time
  for (let i = 0; i < k; i++) {
    windowSum += cardPoints[i] - cardPoints[n - k + i]
    maxSum = Math.max(maxSum, windowSum)
  }
  return maxSum
}
```

Alternatively, we can explicitly **simulate** sliding through the virtual concatenated array _[last k elements] + [first k elements]_:

```javascript
const maxScore = (cardPoints, k) => {
  const n = cardPoints.length
  let maxSum = 0,
    windowSum = 0

  for (let i = n - k; i < n + k; i++) {
    let index = i % n
    windowSum += cardPoints[index]

    if (i < n - 1) {
      continue
    }

    maxSum = Math.max(maxSum, windowSum)

    windowSum -= cardPoints[(i - k + 1) % n]
  }

  return maxSum
}
```

**Complexity Analysis**

- Time complexity: O(k) - Each approach processes at most 2k elements
- Space complexity: O(1)

Building on the sliding concept from forward thinking, we can use a more direct method: **create the concatenated array directly**.

This method clearly demonstrates that selecting `k` cards from the ends is equivalent to finding the maximum sum of `k` consecutive elements in the array _[last k elements] + [first k elements]_.

```javascript
const maxScore = (cardPoints, k) => {
  const n = cardPoints.length
  // Construct concatenated array: [last k elements] + [first k elements]
  const concatenated = cardPoints.slice(n - k).concat(cardPoints.slice(0, k))
  let maxSum = 0,
    windowSum = 0

  for (let i = 0; i < k * 2; i++) {
    windowSum += concatenated[i]

    if (i < k - 1) {
      continue
    }

    maxSum = Math.max(maxSum, windowSum)

    windowSum -= concatenated[i - k + 1]
  }

  return maxSum
}
```

**Complexity Analysis**

- Time complexity: O(k) - Processes 2k elements
- Space complexity: O(k) - Creates a new array of size 2k

Now you’re ready to **slide into** your next coding challenge with confidence. Happy coding! ✨
