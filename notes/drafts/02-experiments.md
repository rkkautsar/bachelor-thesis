# Outline

should be about 4-6 pages?

- Brief history of experiment

  - why it's used: prove theories, prove practicality despite bad in theory etc
  - where it's used: physics, machine learning
  - the popularity over time
  - about reproducible experiments
    - how many are reproducible
    - why it's still low
    - while it's not possible to achieve strict reproducibility (like any physical experiments), comparison can achieve the weaker form; hence benchmarking

- Experiment methods

  - the general methods
  - benchmarking & the need for a tool

- The requirements of a good benchmarking tool

  - personal opinion; based on experiencing benchmarking a mini competition(s) and from johannes, who have done lots of benchmarks for his research

    

  - Extensible & Configurable

  - Properly documented

  - Minimum effort to setup

  - Accurate and reliable measures

  - Easy to share -- reproducible

---

# Draft

1. Science & Experimentation
   - Science aims to understand *why* things happen as they do in the natural world. [Carey, 2012]
   - Investigating these *why* questions is achieved by following what is known as the scientific method, or what Karl Popper has defined as the hypothetico-deductive method, a combination of inductive and deductive reasoning [Walliman, 2010]. Walliman further defines this method as:
     - identification or clarification of a problem;
     - developing a hypothesis (testable theory) inductively from observations;
     - charting their implications by deduction;
     - practical or theoretical testing of the hypothesis;
     - rejecting or refining it in the light of the results.
   - Science can be seen to advance by the means of trial and error: theory is rejected (falsified), another is proposed and tested until the most fitting theory is accepted [Walliman, 2010].
   - Experiment is one way to test the theories or hypotheses in that method.
   - More accurately, experiments can falsify a theory and corroborate it, but not proofing that the actual theory is true. [Tichy, 1998] 
   - Thus, experiments can be seen as just another way of proofing theories by *reductio ad absurdum*, like what proof by contradiction is used in mathematics.
   - Experiments has been used in practice since long ago to achieve great advancement in science. Examples includes:
     - Galileo Galilei famous thought experiment of tying two bodies of object, one lighter and one heavier and dropping if from a top of tower. If, like many believed in that time, heavier object will fall faster as such the case with a heavy metal ball and a feather, the lighter one will pull the heavier one and slow down the fall. But these tied objects makes an object of heavier than either and thus should fall faster, this makes it a contradiction [Gower, 2012]. 
     - This example also points out that external factors which are not taken into account can effect the result of an experiment in a bad way, such as air resitance in this case.
     - The rather extreme case of measuring weights of human soul by Duncan MacDougall, MD [Ryan, 2007]
     - Issac Eddington's validation 100 years ago to prove Einstein's theory that gravity bends light [Tichy, 1998]
     - This are further supported by the recent advancement in astronomy, EHT (event horizon telescope) successfully imaging black hole, an object predicted by Einstein's general theory of relativity.
   - The objectives of experimentation includes: [Montgomery, 2013]
     - Factor screening or characterization
     - Optimization
     - Confirmation
     - Discovery
     - Robustness
2. Experiment Methods
   - Montgomery (2013) defines a guideline in designing an experiment:
     1. Recognition of and statement of the problem
     2. Selection of the response variable
     3. Choice of factors, levels, and ranges
     4. Choice of experimental design
     5. Performing the experiment
     6. Statistical analysis of the data
     7. Conclusions and recommendations
3. Reproducible Benchmarks
   - Reproducibility
     - The term reproducibility is often intertwined with the term replicability. Drummond (2009) argues that replicability is the impoverished version of reproducibility which albeit the great effort to achieve it, its purpose is only for preventing fraud.
     - Goodman et al. (2016) suggests to define new terminologies for reproducibility to avoid the inconsistencies between replicability and reproducibility:
       - Methods reproducibility
       - Results reproducibility
       - Inferential reproducibility
     - Gundersen and Kjensmo (2018) also suggest three degrees of reproducibility. While these are defined as specific in the Artificial Intelligence field, it can be applied to computational science in general:
       - R1: Experiment Reproducible
       - R2: Data Reproducible
       - R3: Method Reproducible
     - They also reported that no papers are fully reproducible by any degree defined above, and the degree of reproducibility of each paper (measured by the number of required variables documented) is only in the 24-26% range.
     - Collberg and Proebsting (2016) reported in another research, the degree of reproduciblity in computer science is only up to 54% even after considerable effort in contacting the authors.
     - They mention some of the reasons as licensing issues, no version tracking, the code is not ready for public, no backup, obsolete dependencies, and so on.
   - Benchmarking
     - Beyer et al. (2019) defines benchmarking as a performance evaluation method that is used for comparing different tools of the same domain, evaluating and comparing different features or configurations of the same tool, or finding out how a single tool performs on different inputs or during regression testing.
     - Simplified process of benchmarking maps closely to designing an experiment, except in computational science the perform and collection phase can (and should) be automated:
       - Planning
       - Performing benchmarks & collecting results
       - Analysis (and re-iterate if needed)
       - Conclusion (i.e. presentation)
     - Benchmarking is definitely an option for an experiment if the design chosen is comparative or variance analysis.
     - It is also a good way to simplify repeated experiments [Tichy, 1998]
     - By packing an experiment as a benchmark, the experiment can be repeated as much as needed because the process is automated, hence achieving results reproducibility.
     - Of course more efforts are needed for sharing the automated benchmark itself to be run in another environment, i.e. to be shared to other people
     - Others can also extends the benchmarks with their own tool and compare it with the original benchmarks. This can be easily achieved if the benchmarks are properly documented.
     - I believe a good benchmarking setup — with documented hardware, software, configuration, and results — is a good way to invite researchers to embrace reproducible research.
4. The ideal benchmarking tool
   - Through my own experience and feedbacks from supervisor (Johannes), I identified these requirements that need to be addressed in order to create the ideal benchmarking tool that will help people embrace reproducible research:
     - Extensible & Configurable
     - Properly documented
     - Minimum effort to setup
     - Accurate and reliable measures
     - Reproducible
     - Parallel runs?