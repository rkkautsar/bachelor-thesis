0. Front matter

1. Introduction
   1. Overview
   2. Contributions
   3. Methods?
   4. Research Scope
   5. Outline

2. Experimental work in algorithmics

   1. Why experiments
   2. Experiment methods
   3. Requirements

3. Existing works and why they don't fulfill the requirements

   - groups & matrix

   1. benchmark-tool
   2. benchexec
   3. benchkit
   4. compbench
   5. jube
   6. optil?
   7. starexec?
   8. ...
   9. various other non-benchmarking tool (computational experiment helper)

4. Measuring & limiting resource usage

   1. Runsolver (rlimit + linux specific /proc/stat polling and prctl subreaper)
   2. Runexec (cgroup + container)
   3. psmon (unix-compatible process stat polling)

5. Implementation of the new benchmarking tool
   1. Tool description
      1. Architecture
      2. System requirements
   2. Benchmarking process w/ example
      1. Configuration
         - pcs files: http://aclib.net/SMAC/papers/10-TR-SMAC.pdf
      2. Orchestrating and executing runs
      3. Evaluating results
      4. Sharing benchmarks
   3. How it fulfills the requirements above
   4. Takeaways
      1. Performance overhead? latency etc.

6. Packing tools dependencies [?]

   1. Reprozip
   2. Docker

7. Conclusion & future works

---

1. Introduction
2. Experimentation & Benchmarking
3. Resource monitoring
4. Existing Benchmarking Tools
5. Implementation
6. Evaluation
   1. case studies
   2. requirements evaluation
   3. performance analysis
      1. performance breakdown
      2. microbenchmarks for overhead
7. Conclusion & Future works

