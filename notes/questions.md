- besides the client/server, is the whole architecture okay?
- client/server
  - should the sqlite be mandatory? or should we support other db?
- ~~evaluation phase — still no idea; there's papermill for parameterized python notebooks~~
  - ~~should we just focus on the runs?~~
- should we use git to track source code? then store the current HEAD to database for each run? — add timestamp too
- executors / resource limiter: currently only `psmon`
  - runsolver
- cross platform? i.e. windows support? currently with `psmon` we can support both linux and mac os — reprozip, for example, supports windows — maybe no
- task sources: should we add more? — ok for now
- tool support: currently only simple executable — nice to have
- what strength should we emphasize for this project?
  - extensibility?
  - reproducibility?
  - sharing?



---

## Johannes' Review, 20-05-2019 

- Q (3.2.1, p.10): Is it always called querying or mostly sampling?
  A: I follow the definition used by Juve et al. as is. It took the perspective of interaction: the user actively querying the system for info. But I agree sampling makes more sense, since it also widely use in other field of science. I'll try adding a remark here.

- Q (3.2.1, note): The topic of I/O seems to be missing? Can we somehow measure certain parameters for the (mean?)? Cache hit? Is there something more interesting? If yes why, if no why not?
  A: I think I'll do further research for this. Our use case mostly doesn't use I/O as measurement (or helping other measurement).

- Q (3.2.1, p. 11): How does it effect processes? If you only invoke a thread, not fork a process?
  A: I think for single processes it will work just fine since the thread is contained in the process and the OS accounts all the threads resource usage e.g. in `proc` 

- Q (3.2.2, p. 11): Is there performance loss when using (ptrace)? Negligible? Major?
  A: It depends on the number of syscall made by the program. For most computation-heavy program I think it's fairly negligible since the syscall is mostly I/O related. For example Kim and Zeldovich reports ptrace adds 36.5% overhead to `zip`, but only 0.1% to matrix calculations benchmarks. 

- Q (3.2.2, p. 11): How about dtrace?
  A: Yes, dtrace is similar to ptrace but uses kernel probes instead. Actually Juve et al. also mentions these probes-based tool but in the interposition mechanism. 
  While this means the overhead is much less (see https://www.kernel.org/doc/ols/2007/ols2007v1-pages-215-224.pdf), kernel-based tracing tool also need superuser privilege and dealing with kernel means we have to be very careful not to make mistakes.
  Might be better to also mention it.

- Q (3.2.2, p. 12): Why is this (watching fs changes and executes query) interesting for use? Are we measuring files?
  A: Actually I think I forgot to add reference for this part, sorry. Here's where I got the idea: https://github.com/DominicBreuker/pspy. I think this is interesting because if we know how the solver writes to the fs, we can use this as a trigger for query.

  For example, a sudoku solver writes a `.cnf` file before spawning a SAT solver. We can monitor the creation of this file to then scan the process tree for this SAT solver. This is better (less resource consuming) than polling the process tree again and again.

- Q (3.2.3, p. 12): What's the difference (between interposition) to VMs? If the VM just wraps the calls?
  A: Here's an interesting read: https://stackoverflow.com/a/25485159/9314778
  The hypervisor receives the guest OS syscall and then either translate it to the host OS syscall, or execute its own implementation of the syscall. So maybe a VM can also be seen as a huge tool using this interposition mechanism? Might be interesting to make a remark about this.

- Q (3.2.3, note B): It feels slightly like this has been taken from some where and not put into the new context . Did you take excerpts of content from Juve et al. ? [ also because the language suddenly changes here ]
  A: It's mostly from Juve et al. with additional examples here and there, like DYLD_INSERT_LIBRARIES, secomp/bpf (seccomp/bpf is a fairly new feature, I think that's why they don't cover it). But I can confirm there's no direct excerpts in any way. In what way do the language suddenly changes?

- Q (3.2.3, p. 13): What does this mean? Ref needed
  A: Yeah sorry I think I get this remark from somewhere else, will try to remember where (might even be from stackoverflow..) and add the reference.

- Q (3.3.2, p. 14): (Docker) means you always have to use the same kernel. What if the kernel is slow?
  A: If the kernel is slow then the docker itself will also be slow? Is this different from VM?

- Q (3.3.2, p. 14): What was in the container?
  A: I guess just an empty OS. The referenced paper only mentions that there is no applications initialized after the boot up.

- Q (3.4.1, p. 15): (regarding runsolver overhead when using interposition). Did you run some experiments yourself in order to see if claimed overhead is reproducible (still)?
  A: I can't seem to find v2 of runsolver, might be just an internal implementation. But as I mention above, the overhead depends on the number of syscall.

- Q (3.4.2, p.16): (regarding runexec)
  A: The installation requires setting up the cgroups pseudo fs as a root for a given user. This might be the tool to use in the future when it's possible to set up (fairly straightforward if sudo access is provided), but I think we might also want to check if interposition's overhead is negligible for most computational-heavy use case. Haven't yet done a benchmark for this.

- Q (3.4.5, p.17): Up to which degree? did you make experiment on the overhead? Are these experiences?
  A: 

  - I think I'll rephrase the sentence.
  - I don't seem to get which overhead?
  - Yes I myself am the one asking in their repo regarding the issue of measurement report, and only get response from other user forking the project to have that feature. The maintainer only seem to be interested in this as a security tool (for now).

- Q (3.4.5, p.17): Can this (syscall filtering) be interesting for benchmarking environments?
  A: I think it's mostly interesting for executing untrusted programs, this is relevant for implementing of online benchmarking tools (starexec, optil) I don't even know how they handle it for now, maybe with containers?

- Q (3.4.6, p. 17): (regarding setuid)
  A: Yes. That's why setuid is scary if misconfigured. But it can be OK if used correctly. In short, it's like the superuser has given the program the pass for executing in superuser privilege. A program that executes arbitrary code will be a disaster in this case. Btw, even the seemingly innocent `ping` is a setuid binary.
  This is a commonly tested security hole (e.g. see https://www.hackingarticles.in/linux-privilege-escalation-using-suid-binaries/)
  From wikipedia: While the `setuid` feature is very useful in many cases, its improper use can pose a security risk[[2\]](https://en.wikipedia.org/wiki/Setuid#cite_note-oreilly-2) if the `setuid` attribute is assigned to [executable](https://en.wikipedia.org/wiki/Executable) programs that are not carefully designed. Due to potential security issues,[[3\]](https://en.wikipedia.org/wiki/Setuid#cite_note-3) many operating systems ignore the `setuid` attribute when applied to executable *shell scripts*. The presence of `setuid` executables explains why the `chroot` system call is not available to non-[root](https://en.wikipedia.org/wiki/Superuser) users on Unix. See [limitations of `chroot`](https://en.wikipedia.org/wiki/Chroot#Limitations) for more details.

- Q (3.4.7, p. 18): (regarding psmon and its originality)
  A: No it's not a copy. I developed it for my own personal use (i.e. to be able to run in Mac OS, no need to compile, etc). You can see the code here: https://github.com/rkkautsar/psmon.It's just a simple polling resource monitor with plugable watchers. I mentioned it as similar to runsolver because the idea is similar: poll both the process tree and resource usage, but the implementation differs. It only achieves to be more flexible and more cross-platform-y (by using psutil) but the accuracy is indeed inferior to runsolver (though not tested yet). Might be better to rephrase it then.

- Q (3.4.7, p. 18): Measuring the energy consumption? Is this possible?
  A: Yeah, runexec implements this. I think it's only possible in Intel CPU. https://github.com/sosy-lab/cpu-energy-meter (huh, it's also setuid)

  

