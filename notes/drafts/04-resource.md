# Measuring and Limiting Resource

## Outline

- Overview
- Approaches
  - query
  - notifications
  - interposing
- Improving reliability
  - Virtualization
    - virtual machine
  - Containerization
    - chroot
    - docker
    - linux namespace
- Implementations
  - runsolver
  - runexec
  - google/nsjail
  - ioi/isolate
  - kickstart
  - resource_monitor
  - psmon

## Draft

### Overview

- Measuring resource is often the entire point of benchmarking.
  - Beyer et al. even designed almost the whole accurate and reliable benchmarking method around its measurement and limiting method (runexec).
- Objective measurement gives birth to objective comparison.
- And resource consumption is one obvious measurement for computational tasks.
- These can include processes, threads, computation, memory, input/output, and files information. (Juve et al, 2015)
- It is often also necessary to limit the resource consumption to some reasonable unit.
  - Selecting data
  - Job scheduling submission
  - Competition
  - Iterative optimization algorithm



### Approaches

- Juve et al describes 3 approaches of resource monitoring:
- query
  - least intrusive
  - not accurate
  - immediately expire
- notifications
  - more reliable than query
  - immediately expire
- interposition
  - most intrusive
  - most accurate

