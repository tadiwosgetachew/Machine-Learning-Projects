# Rock Paper Scissors ML Bot

This repository implements machine learning model that plays Rock, Paper, Scissors against four bots: quincy, mrugesh, abbey, and kris. The agent uses unsupervised learning to track and predict the opponent's strategies, adapting to maximize its win rate.

## Overview

The agent predicts and counters the opponent's next move based on their previous plays, adapting over time using unsupervised learning techniques. It starts with "Rock" and tracks patterns in the opponent's moves to refine its strategy.

## Project Structure

The project is divided into the following modules:

- **`main.py`**: Contains the `run_simulation()` function, which simulates the games against the bots and runs unit tests.
- **`RPS.py`**: Defines the agent that predicts and counters the opponent's moves using unsupervised learning techniques.
- **`RPS_games.py`**: Contains the four bots (quincy, mrugesh, abbey, and kris), each implementing a distinct strategy.
- **`test_module.py`**: Includes unit tests to verify the functionality of the agent and the bots.

## Bot Strategies

Each bot has its own strategy: quincy follows a fixed repeating cycle of Rock, Rock, Paper, Paper, and Scissors; mrugesh predicts based on the most frequent move from the last 10 plays; kris counters the opponent’s previous move; and abbey uses pattern recognition, tracking the last two moves to predict the next, making it more difficult to predict and beat.

## How the Model Works

The agent uses unsupervised learning to track opponent moves to predict the next action, selecting a counter based on historical patterns. Strategies include predicting the most frequent move or using recent history. The agent resets its state if an invalid move occurs to remain adaptable.

## Code Explanation

- **`player(prev_play)`**: Generates the next move based on the opponent’s previous play.
- **`predict_move(history, n, play_order)`**: Predicts the next move based on historical data.
- **`reset()`**: Resets the agent's internal state.
- **`run_simulation()`**: Simulates 1000 rounds against each bot, showing a **99%+ win rate** against all four bots.

## Requirements
- Python 3.x
- numpy

## Future Improvements

1. **Drop the `reset()` Function**: Allow the agent to continuously adapt without resetting, improving its long-term learning and strategy development.
2. **Reinforcement Learning**: Consider implementing reinforcement learning to enhance decision-making, where the agent learns from the outcome of each game to further refine its strategies.
3. **Add More Bots**: Challenge the agent with additional bots, introducing more complex strategies.

## Contributing

Contributions are welcome! Install the required libraries using pip:

```bash
pip install numpy random
