# LRU Cache — Range Sum Optimization

This task demonstrates how an LRU cache improves performance
for repeated range sum queries over a large array.

## Problem

- Array size: 100,000 elements
- Number of queries: 50,000
- Query types:
  - Range(L, R): sum of array[L:R+1]
  - Update(index, value): update array element
- 95% of range queries target a small set of "hot" ranges
- Cache capacity: 1000 entries

## Implementation

Two approaches are compared:

1. **Without cache**
   - Each range query computes the sum directly.
2. **With LRU cache**
   - Results of range queries are cached.
   - On update, all cached ranges containing the updated index
     are invalidated using a linear scan.

## Results (example)

```
Without cache: 5.78 s
LRU cache: 2.17 s
Speedup: x2.7
```