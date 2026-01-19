# Sliding Window Rate Limiter

This task implements a rate limiting mechanism for a chat system
using the Sliding Window algorithm.

## Problem

The system limits how frequently users can send messages
to prevent spam.

Base parameters:
- Window size: 10 seconds
- Max messages per window: 1 message per user

## Algorithm

The Sliding Window algorithm is used to track message timestamps
for each user and determine whether a new message can be sent
within the current time window.

Message history is stored using `collections.deque`.

## Implementation Details

- Each user has a deque of message timestamps
- Old timestamps are removed during each check
- If no timestamps remain, the user is removed from storage
- The limiter supports:
  - Checking if a message can be sent
  - Recording a message
  - Calculating time until the next allowed message

## Demo

A demonstration function simulates message sending from
multiple users with random delays.

The output shows:
- Allowed messages
- Blocked messages with remaining wait time

