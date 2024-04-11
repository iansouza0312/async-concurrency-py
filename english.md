# Concurrent vs. Asynchronous Programming - Python

### Main Concepts

What happens on the machine when we execute a Python script?

1 - The interpreter creates a process (Operating System)
2 - The process creates a thread

### What is "concurrency"?

Execution of multiple sequential instructions simultaneously (Computer Science)

##### Main types of concurrency:

- Asynchronous programming
- Parallel programming

##### Key points for good performance:

- Execution order
- Shared computational resources
  - Execution between instructions should share as few resources as possible
  - The more shared resources, the greater the coordination between instruction execution

_note: the execution order of instructions should not influence the final result of execution_

<hr>

# Types of Concurrency

- Asynchronous programming
- Parallel programming
- Distributed programming (more than one machine)

### Parallel Programming

It consists of performing a computational task by dividing it into small sub-tasks, which will be executed simultaneously.

_note: the division depends on the number of cores of the machine's processor where the script will be executed_

- Without parallel programming, the machine will use only 1 core to execute the task, even if it has multiple cores.

  - Capacity overload, using 100% of the capacity of a single core while others remain "inactive"

- It stands out in performing tasks that consume excessive CPU processing
  - String operations
  - Graphic processing
  - Search algorithms

_note: it is possible to use GPU cores to assist CPU processing_

### Asynchronous Programming

Used in read or write operations on I/O devices.

Certain tasks may require certain "parts" to be executed asynchronously.

- Connection with DataBase
- Connection with Server

After executing an asynchronous instruction, the instruction is delegated to a new device or thread and seeks the execution of new tasks. Without this, it would remain waiting for the execution of these tasks and would leave the remaining tasks waiting until it was completed.

- After the execution of the thread (async.), the main thread is "notified"

  - callback
  - promise
  - task

##### Main tasks where it is used:

- DataBase (read/write)
- API calls
- Data Download/Upload

<hr>
