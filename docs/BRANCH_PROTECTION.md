# Branch Protection for `main`

The `main` branch is protected so no code reaches the working system without
passing the CI backstop (`.github/workflows/pipeline.yml`).

## Rule configured on GitHub

Settings > Branches > Add branch protection rule (or Settings > Rules > Rulesets):

- Branch name pattern: `main`
- [x] Require a pull request before merging
- [x] Require status checks to pass before merging
  - [x] Require branches to be up to date before merging
  - Required check: **Build and Test** (job from *TravelBuddy CI Pipeline*)

## Workflow for every change

1. `git checkout -b feature/<name>`
2. Commit the change with its tests.
3. `git push -u origin feature/<name>` and open a Pull Request into `main`.
4. GitHub runs the pipeline on the PR. The **Merge** button stays blocked
   until *Build and Test* is green.
5. Merge once the check passes.
