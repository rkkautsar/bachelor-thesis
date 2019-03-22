## Past works



### [benchmark-tool][1]

- lesson learnt from using it for sudoku sat competition:
  - pretty helpful, but:
  - minimum documentation
  - the setup is cumbersome; a lot of copying and hardcoding
  - centralized in the repo (with branches etc.)
  - a bit hard to share the benchmark, e.g. to be run by others; need to also push the programs etc.
  - installation takes a while:
    - no requirements.txt (dependencies not stated)
    - can't be run natively in linux (runsolver)
  - a bit confusing to extend, i.e. for running in slurm

- tried refactoring it
  - yaml runscript
  - decentralized
  - ability to download from zenodo
  - documentation on https://benchmark-tool.readthedocs.io
  - export import (just packing it in a tar.gz since the benchmark is now decentralized)
  - hard to further refactor since it will probably needs many  architectural refactoring



### [tplp-planning-benchmark][2]

> Planning benchmarks for the extended TPLP journal version of the plasp paper

- A simple one-time benchmark
- Auto commit & push to git
- Uses [timeout][3]; not reliable (rlimit)
- No parallel runs
- No documentation



### [BenchExec][4]

> 1. Measure and Limit Resources Accurately
>
> 2. Terminate Processes Reliably
>
> 3. Assign Cores Deliberately
>
> 4. Respect Nonuniform Memory Access
>
> 5. Avoid Swapping
>
> 6. Isolate Individual Runs
>
>    — [Requirements for reliable benchmarking][5]

- Focuses on reliable benchmarking: uses linux-specific cgroup feature for accurate process resource limiting
- Also support optional container with linux namespace
- But it needs root setup (for cgroup)
- The evaluation is also tightly coupled with their SVCOMP competition, i.e. with predefined properties etc.

### [compbench][6]



### Reproducible Experiments

Sacred Infrastructre:

- configure, organize, log and reproduce computational experiments
- no resource limiting

Sumatra

- tool for managing and tracking projects based on numerical simulation and/or analysis, with the aim of supporting reproducible research

Future Gadget Laboratory

- machine learning dashboard, designed to make prototyping experiments easier. Experiment details and results are sent to a database, which allows analytics to be performed after their completion
- 



---

[1]: <https://github.com/daajoe/benchmark-tool>
[2]: <https://git.luehne.de/patrick/tplp-planning-benchmark>
[3]: <https://github.com/pshved/timeout>
[4]: <https://github.com/sosy-lab/benchexec>
[5]: <https://www.sosy-lab.org/research/pub/2019-STTT.Reliable_Benchmarking_Requirements_and_Solutions.pdf>
[6]: https://github.com/StephanGocht/experimentRun