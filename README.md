# Just Another Agent Management System (JAAMS-AV2)

Welcome to **JAAMS-AV2**, an advanced agent management system designed to streamline the coordination, delegation, and evaluation of autonomous agents. This system leverages agentic AI to manage complex tasks efficiently.

## Purpose

JAAMS-AV2 aims to provide a robust framework for managing multiple autonomous agents, each with specialized capabilities. The system is designed to:
- Delegate tasks to the most suitable agents.
- Monitor and evaluate agent performance.
- Collect and report results back to the user.
- Optimize task execution based on agent capabilities.
- Flexible LLM interface for easy integration with other systems, eg ollama, Groq etc.

## Architecture

JAAMS-AV2 is built using Python and follows a modular architecture. The main components include:

### Agents

- **Manager**: Coordinates tasks between agents, collects results, and reports back to the user.
- **Planner**: Plans tasks and strategies for agents.
- **Analyzer**: Analyzes data and provides insights.
- **CodeWriter**: Generates and modifies code based on given tasks.
- **FileSystemOperator**: Manages file system operations.
- **NetworkOperator**: Handles network-related tasks.
- **SystemOperator**: Manages system-level operations.

### Tools

- **AgentTaskAssigner**: Assigns tasks to agents based on their capabilities.
- **AgentEvaluator**: Evaluates agents to determine the best fit for a given task.
