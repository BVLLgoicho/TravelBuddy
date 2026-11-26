# Phase 5 – Reflection: Impact of CI/CD on Team Scaling and Software Stability

## 1. "The first one to check in wins, everybody else merges." How does an automated CI pipeline reduce the pain of these merges for a large team?

Merge pain grows with the time between integrations. If developers work in isolation for days,
their branches drift further from `main`, and whoever checks in second has to reconcile a large,
unfamiliar set of changes. A CI pipeline encourages, and makes safe, small and frequent
check-ins. Each push is built and tested within minutes, so every merge is small and the
differences to reconcile are recent and easy to understand.

The pipeline also takes the guesswork out of a merge. After resolving conflicts, the developer
does not need to hope that nothing broke. The full test suite runs on the merged result and
gives an objective pass or fail. Because `main` is protected and always green, everyone merges
against a known-good baseline. When a merge does break something, the failing test points
straight at the problem while the change is still fresh, which keeps the cost of being "second"
low even on a large team.

## 2. How does an automated pipeline support the Agile principle of maintaining a Sustainable Pace indefinitely?

A sustainable pace depends on not building up hidden work. Without automation, every release
needs long manual regression testing, integration problems pile up until late in the iteration,
and teams end up working overtime to stabilise the system before a deadline. The automated
pipeline removes that repetitive effort. Thousands of checks run on every push without any human
time spent on them.

Because the system is never allowed to stay broken for long, defects are found minutes after
they are introduced, while they are still cheap to fix. They do not grow into end-of-sprint
emergencies. The green build also lowers stress: developers can refactor and add features
confidently, knowing the backstop will catch regressions. The team can keep a steady, predictable
rhythm iteration after iteration instead of swinging between calm periods and crunch. This is the
idea that "high quality is the key to high speed".

## 3. Why is it vital that the pipeline runs the *entire* test suite on every push, rather than just the tests related to the new code?

Software components are coupled in ways that are not always obvious. A change to one module can
break behaviour somewhere else through shared functions, data formats, configuration or
dependencies. For example, changing how `total_trip_cost` rounds values could silently break
budget-splitting or currency features that rely on it. If only the tests "related" to the new code
were run, these regressions would slip through, and the system would start "backsliding to a lower
level" of quality without anyone noticing.

Running the whole suite each time makes every push prove that the *whole system* still works end
to end, which is what Continuous Integration promises. It also supports Collective Ownership. Any
team member can change any part of the code, because the full suite protects behaviour that other
people wrote and that the person making the change may not know well. Finally, a developer's guess
about which tests are relevant is exactly the kind of human judgement that fails under pressure.
Running everything removes that risk, and the suite is fast enough that the cost is small compared
with the cost of a regression reaching `main`.
