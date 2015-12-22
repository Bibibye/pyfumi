# pyfumi
A Python implementation of the game Rock-Paper-Scissors.

As a reminder :

- Rock (R) beats Scissors (S)
- Scissors (S) beat Paper (P)
- Paper (P) beats Rock (R)

The optimal mixed strategy (named `mixed`) for this game is
known and consists in randomly playing R, P or S with
probabilities of :

```
p(R) = p(S) = p(P) = 1/3
```

However, that strategy is optimal if you play against an
opponent who also tries to play optimaly. Hence, we can
improve the strategy to win more often against dummy
opponents.

This program proposes an improved strategy based on Hidden
Markov Models (named `markov`). It remembers the `n` last
games, and plays according to the statistics of the opponent.

Tests show that `markov` is at least as efficient as `mixed`.

Against `mixed`, `markov` converges to `mixed`.

Against `dummy`, `markov` converges to a `dummy` strategy which
wins every time (as long as `n` is big enough).
