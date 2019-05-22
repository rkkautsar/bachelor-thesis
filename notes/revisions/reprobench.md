> Following Johannes' review (19-05-2019)



### General Fixes & Improvement

- Kill process tree on exit
- Improve cli ux
- Improve installation and dx
  - Use conda, publish to anaconda-cloud and conda-forge
- Analysis steps should not be stored in db. Better to use the config file instead
- CLI arguments can be set in the config file
- SSH-based manager for server & worker



### Update Strategy

- Defaults to create folders under `output/[benchmark_id]`. The `benchmark_id` can be set, but defaults to current time, e.g. `20190522_105722`.

  - This way resuming existing benchmark is explicit

- Bootstrapping is implicit. It's always executed when the manager starts spawning workers.

- Bootstrapping an existing benchmark (denoted by existing `output/[benchmark_id]/benchmark.db`) updates the run

  - Insert new instances
  - Insert new tools
  - Insert new parameter groups
  - Insert new steps & observers? (might be a problem since the server need to start greenlets for the new observers)
  - Generate runs from the newly inserted (tools, parameter, instances) combination

- ...

  



### Server

- Server manages many benchmarks?

- Server should handle multiple bootstraps correctly

- Address port exposing security

  

### Publishing Benchmark

Maybe something like this? With extensible`-p/--provider` 

- `reprobench publish config -p zenodo`

- `reprobench publish config -p github`

- `reprobench publish result -p zenodo -d output/20190522_105722`

- `reprobench publish result -p zenodo -d output/20190522_105722 --include-output`

  

