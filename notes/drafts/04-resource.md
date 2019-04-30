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

- Juve et al describes 3 approaches for resource monitoring:

- query

  - least intrusive, not accurate, immediately expire
  - procfs
  - stat
  - getrusage
  - psutil: abstraction for various query
  - gpu

- notifications

  - more reliable than query, immediately expire
  - wait4: getrusage
  - inotify
  - forkstat
  - ptrace: process creation and exit
  - taskstats

- interposition

  - most intrusive, most accurate

  - LD_PRELOAD or DYLD_INSERT_LIBRARIES

  - ptrace syscall: strace dtrace

  - seccomp/BPF + ptrace: less overhead (Kim and Zeldovich)

  - this might be considered if the process measured do most of the computation in the user space compared to syscalls.

  - on a side note, this can be used to achieve some degree of security.

    

    ### Reliability

    - virtualization
    - containerization
      - chroot: not safe, can *break the chroot jail*
      - docker: need superuser, although there's an ongoing effort to create a rootless container
      - linux container: user-space, a bit limited but can be sufficient

    

