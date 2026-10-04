# ANDREW-DIRECT 2026-10-04 ~20:3xZ -- NFRA_SPRINTWIN: MSTR~Z runs the push and the laptop integration

**Channel:** the `4.0.0_SA_CRO~Z` terminal, site Z. **Recorded by:** `4.0.0_SA_CRO~Z`, same turn.

**Andrew, verbatim:** *"Have MSTR~Z run the push and handle the laptop integration with this work"*

**Context:** his answer to this seat's two asks after H0-H4 landed on local CLOUD (@93151a0af8; origin CLOUD 2205340103 by
ls-remote at 20:3xZ): (1) his word to push CLOUD, because the cloud function clones origin; (2) the image build on the laptop,
because site Z has no Docker and the laptop built every earlier sprint image.

**Owner:** `0.0.0_AB_MSTR~Z`. Scope as given: the push, and the laptop integration "with this work" (NFRA_SPRINTWIN). This seat
does not widen or narrow it.

## What "the laptop integration" needs, for 0.0.0_AB_MSTR~Z to carry to the laptop

1. **The image, built from COMMITTED bytes** (precedent: `org/critical_paths/change_management/20260924T2013Z_daily-sprint-notes-20260924_deploy_completion.md` leg L2):
   `git archive <pushed CLOUD hash> infra/aws/lambda/daily_sprint_generator` -> `docker build --provenance=false --sbom=false --platform linux/amd64`
   -> push `313476888478.dkr.ecr.us-east-1.amazonaws.com/daily-sprint-generator:latest`. Report: the pushed digest, and the
   in-image `/var/task/lambda_function.py` git blob = `d284642a32b2530def16a361fee67807abf39fb2` (the committed bytes at
   @6c491b6e9d). The tag has ONE consumer, the function. Do NOT apply: the `safe-apply -replace` of the function, the IAM change,
   and the NEVER-2 ledger entry are this seat's (site Z).
2. **The laptop's device census, from origin/CLOUD (H1, PRD C-CENSUS)**: after `git fetch`,
   `git show origin/CLOUD:.tools/sprint-device-census.py > <temp>/sprint-device-census.py` then
   `python <temp>/sprint-device-census.py --root <laptop repo root>`. Report its two OK lines (the census line and the
   `s3://opal-data-assets/sprint/global/bronze/device_census/date=<D>/laptop.json ... etag=MATCH` line).
3. **The laptop's Scheduled Task** (15:55 ET, retry 16:02, running the origin/CLOUD copy as in 2) is the laptop MSTR's in its
   /integrate lane per the PRD -- enrichment FWD-7, not needed for tonight's QA trace.
