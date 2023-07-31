# 0x05. Processes and Signals

![Author](https://img.shields.io/badge/Author-AzukaUteh-blue.svg)


This directory contains information and examples related to processes and signals in the context of operating systems and programming. It aims to provide a comprehensive guide to understanding processes, how they are managed, and how signals can be used to communicate with processes.

## Table of Contents

1. [Introduction to Processes](#introduction-to-processes)
2. [Process Management](#process-management)
3. [Creating and Terminating Processes](#creating-and-terminating-processes)
4. [Process States](#process-states)
5. [Interprocess Communication](#interprocess-communication)
6. [Introduction to Signals](#introduction-to-signals)
7. [Sending Signals](#sending-signals)
8. [Handling Signals](#handling-signals)
9. [Signal Handling Strategies](#signal-handling-strategies)
10. [Signal Examples](#signal-examples)
11. [Best Practices](#best-practices)
12. [Glossary](#glossary)

## Introduction to Processes

### What is a Process?

A process is an executing instance of a computer program. Each process has its own memory space, program counter, registers, and system resources such as file descriptors. The operating system (OS) manages processes to achieve multitasking, allowing multiple programs to run concurrently.

### Process Identification

Each process is assigned a unique identifier called a Process ID (PID). The PID is a non-negative integer used by the OS to track and manage processes. PIDs are essential for sending signals and managing process relationships, such as parent-child relationships.

### Process Hierarchy

Processes can be organized into hierarchies, where a parent process can create child processes. This creates a parent-child relationship, and child processes can, in turn, create their child processes, forming a tree-like structure. This hierarchy allows processes to share information and work together in a coordinated manner.

### Process Management in Operating Systems

The OS is responsible for managing processes efficiently. Key aspects of process management include process creation, process scheduling, context switching, and process termination. Let's explore some of these concepts further.

## Process Management

### Process Creation

Processes can be created using system calls like `fork()` and `exec()` on Unix-like systems. The `fork()` system call creates a copy of the calling process, resulting in a parent and a child process. The child process inherits the parent's address space and resources. On the other hand, the `exec()` system call loads a new program into the current process's memory space, replacing the current program.

#### Example - Creating a Child Process with `fork()`

```c
#include <stdio.h>
#include <unistd.h>

int main() 
{
    pid_t pid = fork();
    if (pid == 0) 
{
        printf("This is the child process.\n");
    } else if (pid > 0) 
{
        printf("This is the parent process. Child PID: %d\n", pid);
    } else 
{
        printf("Error occurred during fork().\n");
    }
    return (0);
}
```

### Process Scheduling

The OS scheduler is responsible for allocating CPU time to processes. Scheduling algorithms, such as round-robin, priority-based, and multilevel feedback queues, determine the order in which processes are executed. Scheduling aims to achieve fairness, efficiency, and responsiveness.

### Context Switching

When the CPU switches from executing one process to another, it performs a context switch. The context of a process includes its register values, program counter, and other essential information. Context switches introduce overhead, and efficient scheduling minimizes the number of context switches.

### Process Termination

Processes can terminate voluntarily or involuntarily. Voluntary termination occurs when a process completes its task or explicitly calls the `exit()` system call. Involuntary termination happens due to errors, signals, or the termination of a parent process.

## Creating and Terminating Processes

### Creating Processes with `fork()` and Executing a New Program

The `fork()` system call allows the creation of a child process, and then the child process can execute a different program using the `exec()` system call. This combination is often used to execute external programs from within a C program.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() 
{
    pid_t pid = fork();
    if (pid < 0) 
{
        perror("Fork failed");
        exit(1);
    } else if (pid == 0) 
{
        // Child process
        execlp("/bin/ls", "ls", "-l", NULL);
        perror("Exec failed");
        exit(1);
    } else 
{
        // Parent process
        wait(NULL); // Wait for the child process to complete
        printf("Child process finished.\n");
    }

    return (0);
}
```

### Handling Process Termination

The parent process can use the `wait()` or `waitpid()` system calls to wait for the child process to terminate. By doing this, the parent process ensures that it doesn't continue execution before the child process has finished.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() 
{
    pid_t pid = fork();
    if (pid < 0) 
{
        perror("Fork failed");
        exit(1);
    } else if (pid == 0) 
{
        // Child process
        printf("Child process executing...\n");
        sleep(3); // Simulate some work
        printf("Child process finished.\n");
        exit(0);
    } else 
{
        // Parent process
        int status;
        wait(&status); // Wait for the child process to terminate
        if (WIFEXITED(status)) 
{
            printf("Child process exited with status: %d\n", WEXITSTATUS(status));
        } else 
{
            printf("Child process did not terminate normally.\n");
        }
    }

    return (0);
}
```

## Process States

Processes can exist in various states throughout their lifecycle. Common process states include:

1. **Running**: The process is currently being executed on the CPU.
2. **Ready**: The process is waiting to be assigned CPU time for execution.
3. **Blocked/Waiting**: The process is waiting for some event (e.g., I/O) to occur before it can proceed.
4. **Terminated**: The process has finished its execution and has been removed from the process table.

The OS scheduler determines which process transitions between these states based on scheduling algorithms.

## Interprocess Communication

Processes often need to communicate with each other. Interprocess Communication (IPC) provides mechanisms for exchanging data and information between processes. Some common IPC mechanisms include:

1. **Pipes**: A unidirectional communication channel where data can be written by one process and read by another.
2. **Message Queues**: A queue-based mechanism that allows processes to send and receive messages.
3. **Shared Memory**: A region of memory shared between two or more processes for efficient data exchange.
4. **Sockets**: Network sockets enable communication between processes on different machines over a network.

Each IPC mechanism has its advantages and use cases. Selecting the appropriate mechanism depends on the nature of data exchange and the processes involved.

## Introduction to Signals (continued)

Signals are a fundamental form of interprocess communication used in Unix-like operating systems. A signal is a software interrupt delivered to a process, notifying it of an event or requesting a particular action. Signals are asynchronous, meaning they can be sent at any time, and the receiving process must handle them appropriately.

### Common Signals

Unix-like systems have a set of predefined signals, each identified by a unique integer value. Some common signals include:

- **SIGINT (2)**: Interrupt signal, often generated when the user presses Ctrl+C in the terminal.
- **SIGTERM (15)**: Termination signal, used to request a graceful termination of a process.
- **SIGKILL (9)**: Kill signal, used to force termination of a process.
- **SIGSTOP (19)**: Stop signal, used to pause a process temporarily.
- **SIGCONT (18)**: Continue signal, used to resume a stopped process.

### Signal Handling

Processes can handle signals using signal handlers. A signal handler is a function that processes a signal once it is received by the process. By default, many signals cause the process to terminate, but custom signal handlers can override this behavior.

### Sending Signals

Signals can be sent to processes using the `kill()` system call. Although the name may suggest termination, `kill()` can be used to send any signal to a process, not just to kill it.

### Example - Sending SIGINT Signal to a Process

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void sigint_handler(int signum) 
{

    printf("Received SIGINT signal. Exiting...\n");
    exit(0);
}

int main() 
{
    // Register SIGINT handler
    signal(SIGINT, sigint_handler);

    printf("Running. Press Ctrl+C to interrupt.\n");
    while (1) 
{
        // Do some work
    }

    return (0);
}
```

### Handling Signals

When a signal is sent to a process, it can be handled in one of several ways:

- **Default Action**: The default action for most signals is to terminate the process. Some signals, like SIGCHLD, are ignored by default.
- **Ignoring Signals**: A process can explicitly ignore certain signals, preventing their default actions.
- **Blocking Signals**: A process can block specific signals temporarily, preventing their delivery until they are unblocked.

### Signal Handling Strategies

Signal handling requires careful consideration to ensure that processes respond appropriately to signals they receive. Some strategies include:

- **Ignoring Irrelevant Signals**: Ignore signals that are not relevant to the process to prevent unwanted interruption.
- **Graceful Termination**: Handle SIGTERM and other termination signals to clean up resources before exiting.
- **Blocking Critical Signals**: Block critical signals during critical sections of code to avoid unexpected interruptions.

## Signal Examples

### Example - Handling SIGUSR1 and SIGUSR2 Signals

In this example, we create a simple program that handles custom signals, SIGUSR1 and SIGUSR2. The program increments a counter when it receives SIGUSR1 and decrements the counter when it receives SIGUSR2.

```c
#include <stdio.h>
#include <signal.h>

volatile int counter = 0;

void sigusr1_handler(int signum) 
{

    counter++;
    printf("Received SIGUSR1. Counter: %d\n", counter);
}

void sigusr2_handler(int signum) 
{
    counter--;
    printf("Received SIGUSR2. Counter: %d\n", counter);
}

int main() 
{
    signal(SIGUSR1, sigusr1_handler);
    signal(SIGUSR2, sigusr2_handler);

    printf("Running. PID: %d\n", getpid());
    while (1) 
{
        // Keep the program running to handle signals
    }

    return (0);
}
```

### Sending Signals from the Command Line

You can send signals to a process from the command line using the `kill` command (on Unix-like systems). To send a signal with a specific signal number (e.g., SIGUSR1) to a process with a known PID (e.g., 12345), use the following command:

```bash
kill -SIGUSR1 12345
```

## Best Practices

When working with processes and signals, keep the following best practices in mind:

- Always handle critical signals like SIGINT and SIGTERM to allow for graceful termination.
- Avoid using blocking system calls within signal handlers to prevent unexpected behavior.
- Use signal-safe functions in signal handlers to ensure reentrancy and avoid data corruption.
- Minimize the work done in signal handlers to keep them as short and efficient as possible.
- Document the signals used and their corresponding actions to improve code readability and maintainability.

## Glossary

- **Process**: An executing instance of a program with its own memory space and system resources.
- **PID**: Process ID, a unique identifier for a process.
- **Process Hierarchy**: The parent-child relationship between processes, forming a tree-like structure.
- **Context Switching**: The process of switching the CPU from one process to another.
- **IPC**: Interprocess Communication, mechanisms to allow processes to exchange data and information.
- **Signal**: A software interrupt used for interprocess communication and handling specific events.
- **Signal Handler**: A function that processes signals received by a process.
- **kill()**: A system call used to send signals to processes.
- **Default Action**: The action taken by the OS when a signal is not handled explicitly.
- **Blocking Signals**: Temporarily preventing the delivery of certain signals.
- **Graceful Termination**: A clean process termination with appropriate cleanup of resources.
