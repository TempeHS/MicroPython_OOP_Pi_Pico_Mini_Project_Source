# Lecture 7

## Lecture 7 concepts

- Open & Closed Loop Control Systems
- Open Loop State Machine
- Implement an Open Loop State Machine

## Open & Closed Loop Control Systems

Open and closed loop control systems are two fundamental types of control systems used in engineering, automation, robotics, and other fields to manage the behavior of devices or processes.

### Open-Loop

An open-loop control system is a type of system in which the control action is independent of the desired output or the actual system output.

How it works:

- The system receives an input (command or reference signal).
- The controller processes this input and sends a control signal to the actuator.
- The actuator executes the control action, affecting the system or process.
- There is no feedback mechanism to compare the output with the input.

Example:

A microwave oven: You set the cooking time, and the microwave runs for that duration regardless of how hot the food actually gets.

### Closed-Loop

A closed-loop control system (also called a feedback control system) is a system in which the control action is dependent on the desired output and the actual system output.

How it works:

- The system receives an input (desired value or setpoint).
- The controller processes this input and sends a control signal to the actuator.
- The actuator operates on the system.
- A sensor measures the actual output.
- The output is fed back and compared with the input (setpoint).
- The difference (error) is used to adjust the control action to reduce the error.

Example:

A home thermostat works by allowing the homeowner to set a desired temperature. The system then measures the actual room temperature and adjusts the heater or cooler to reach and maintain the set temperature. As the system approaches—or overshoots—the desired temperature, it modifies its output accordingly.

## State Machine

A state machine (also known as a finite state machine or FSM) is a computational model used to design and describe systems that can be in one of a finite number of states at any given time. It transitions between these states in response to external inputs or events such as time, button presses of sensor values.

Key concepts:

- States: Distinct modes or conditions in which the system can exist.
- Transitions: Rules that define how and when the system moves from one state to another, often triggered by events or inputs.
- Events/Inputs: External actions or signals that cause state transitions.
- A State Machine can be open or closed

## Implement an Open Loop State Machine

## Usage: Controller Class (State Machine Example)

