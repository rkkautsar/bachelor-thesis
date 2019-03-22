0. Front matter

1. Introduction
   1. Overview
   2. Contributions
   3. Methods?
   4. Research Scope
   5. Outline
2. Requirements
   1. ...
3. Existing works and why they don't fulfill the requirements
   1. benchmark-tool
   2. benchexec
   3. compbench
   4. optil?
   5. starexec?
   6. ...
   7. various other non-benchmarking tool (computational experiment helper)
4. Methods for limiting resource usage
   1. Runsolver (rlimit + linux specific /proc/stat polling and prctl subreaper)
   2. Runexec (cgroup + container)
   3. psmon (unix-compatible process stat polling)
5. Packing tools dependencies
   1. Reprozip
   2. Docker
6. Implementation of the new benchmarking tool
   1. Tool description
      1. Architecture
      2. System requirements
   2. Benchmarking process
      1. Configuration
         - pcs files: http://aclib.net/SMAC/papers/10-TR-SMAC.pdf
      2. Orchestrating and executing runs
      3. Evaluating results
      4. Sharing benchmarks
   3. How it fulfills the requirements above
7. Conclusion & future works

