# TravelBuddy

A small trip-planning helper (trip cost totals, cost splitting, currency conversion) used to
demonstrate a Continuous Integration pipeline with GitHub Actions for SWE6301 Week 10.

## Run the tests locally

```
pip install -r requirements.txt
pytest -v
```

## CI pipeline

`.github/workflows/pipeline.yml` runs on every push and pull request to `main`:

1. Ubuntu runner (`ubuntu-latest`)
2. Checks out the code (`actions/checkout@v4`)
3. Sets up Python and installs dependencies (`pytest`)
4. Runs the full test suite with `pytest`

See [docs/BRANCH_PROTECTION.md](docs/BRANCH_PROTECTION.md) for the protection rule on `main`
and [docs/REFLECTION.md](docs/REFLECTION.md) for the Phase 5 answers.
