# Risk-Reward Calculator

This small command-line program compares the possible loss and gain for one planned trade. It works for long and short setups and reports the reward-to-risk ratio and the win rate needed to break even before fees.

## Usage

Pass the entry price, stop price, and target price in that order:

```bash
python3 projects/risk-reward-calculator/main.py 100 95 110
```

The output is:

```text
Direction: long
Risk per unit: 5.00
Reward per unit: 10.00
Reward-to-risk ratio: 2.00:1
Break-even win rate: 33.33%
```

For a long trade, the stop must be below the entry and the target must be above it. For a short trade, the target must be below the entry and the stop must be above it. Every price must be finite and greater than zero.

## Tests

```bash
python3 -m unittest discover -s projects/risk-reward-calculator -p 'test_*.py'
```

## Limitations

The calculator uses the three prices you provide. It does not include position size, trading fees, slippage, taxes, partial exits, or the chance that an order is not filled. The break-even win rate is a mathematical threshold, not a prediction or trading recommendation.
