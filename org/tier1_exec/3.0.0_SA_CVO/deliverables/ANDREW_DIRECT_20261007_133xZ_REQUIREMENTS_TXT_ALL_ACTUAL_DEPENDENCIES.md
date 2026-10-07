# ANDREW-DIRECT 2026-10-07 ~13:3xZ -- the root requirements.txt carries every actual dependency

**Channel:** typed at the `3.0.0_SA_CVO` terminal (laptop). **Recorded by:** `3.0.0_SA_CVO`.

## His words, VERBATIM

"We need to update the requirements.txt in the root of ajb_workspace with all actual dependencies needed to operate
here."

## What this seat did on it

- Replaced `requirements.txt` at the workspace root. The file it replaces (written 2026-08-07, @913e84c3b8) was an
  inventory aggregated from 61 other requirements files, by its own header "not a single installable lockfile".
- The new file is generated from a census of what the workspace's own tracked Python code imports:
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/REQUIREMENTS_CENSUS/import_census.py` (reads, executes nothing),
  its output `import_census_20261007.json`, and `build_requirements.py`.

## Not decided by these words (this seat's readings, stated as readings)

- "actual dependencies" is read as: what tracked code imports, plus the programs the gates call. It is not read as
  "everything installed on the laptop".
- "to operate here" is read as the workspace on a developer or agent box. What each Lambda bundles for AWS stays in
  that Lambda's own requirements file.
- Versions are pinned to what the laptop has installed. He named no version policy.

-- 3.0.0_SA_CVO
