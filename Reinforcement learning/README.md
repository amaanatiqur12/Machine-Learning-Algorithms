## Reinforcement learning

[Visit Youtube => Markov Decision Process ](https://www.youtube.com/watch?v=2iF9PRriA7w)

A Markov Decision Process (MDP) is a way to model decision-making in situations where you have to make choices and the outcomes are uncertain. It helps you figure out the best decisions to make over time to maximize rewards.

Key Parts:
1. States: These represent where you are in the world (like a specific situation).
2. Actions: The choices you can make at any state.
3. Transition: After you take an action, you move to a new state, and this happens with some chance (probability).
4. Rewards: For every action you take, you get some immediate feedback or score (reward).
5. Goal: The goal is to choose actions in a way that gives you the highest total reward over time.

The "Markov" part means that what happens next only depends on where you are right now, not on how you got there. This makes the decision-making process easier because you just need to focus on the current situation.

### Exploration vs Exploitation

Exploration:
Exploration means trying new actions to discover more about the environment.
The agent takes actions that it hasn't tried enough or doesn't know much about, even if those actions might not give the best reward at the moment.
The goal is to gather more information about the environment to find potentially better rewards in the future.
Example:
Imagine you're at a new restaurant with a menu full of dishes you've never tried. You could explore by trying a dish you haven’t eaten before. It might be amazing, but it’s a risk since you don’t know if you’ll like it.

Exploitation:
Exploitation means using the knowledge the agent already has to choose the best-known action, which is expected to give the highest reward based on past experience.
The agent is focused on maximizing the immediate reward by picking the most rewarding action it has learned so far.
Example:
At the same restaurant, if you order a dish you’ve had before and know you like, you are exploiting your knowledge. You are not taking a risk, but you also miss out on discovering something new.

The Dilemma:
Exploitation focuses on immediate rewards, but if you only exploit, you might miss out on better options.
Exploration sacrifices immediate rewards for the chance of finding something better, but too much exploration wastes time on bad choices.

In RL, the agent needs a balance between exploration and exploitation to learn efficiently. Early on, it may explore more to learn about its environment, but as it gains more knowledge, it exploits more to maximize its rewards.


### policy

In reinforcement learning, a policy is the strategy or rule that an agent follows to decide which action to take in a given state. It essentially guides the agent's behavior in the environment.

Key Points:
Deterministic Policy: A policy that always chooses a specific action for a given state.

Example: If the agent is in state A, it always takes action X.
Stochastic Policy: A policy that assigns probabilities to actions, meaning the agent might take different actions in the same state based on those probabilities.

Example: If the agent is in state A, it might take action X with a 70% chance and action Y with a 30% chance.
Goal of a Policy:
The goal of reinforcement learning is to find an optimal policy, which is a policy that helps the agent maximize its total rewards over time.

In simple terms, a policy tells the agent, "When you're in this situation (state), do this (action)."

