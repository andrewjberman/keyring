# ANDREW-DIRECT 2026-09-25 ~16:5xZ -- the Trade Submission Vident-model fix ships to DEV and, narrowly, to PROD

**Channel:** the 1.0.0_SA_CTO terminal. **Recorded by:** 1.0.0_SA_CTO, same turn. **Context:**
- 4.0.0_SA_CRO msg 100973 carries Andrew's word "trade submission needs the path for the new format".
- The backend half, `trade-submission-handler`, is deployed from CLOUD @`1aabca225a`, ledger
  `trade-vident-model-20260925` closed.

## The question, verbatim

"Lauren's fix: the Trade Submission page now accepts the new Vident model file and submits it for approval. The
backend half is live. The page change is one commit (6 files, 7 new tests passing, typecheck clean). How should it
ship?"

The options offered:
- "DEV + narrow PROD now (Recommended)" -- "Push to DEV, and apply just this one commit on PROD. Lauren can upload
  today, and nothing else from DEV (e.g. the Investor Reporting round 3) reaches PROD.";
- "DEV only for now".

## The answer, verbatim

"DEV + narrow PROD now (Recommended)"

## What it binds

- **DEV:** 0.0.0_AB_MSTR fast-forwards portal DEV from `8242412d` to `a886aeb4` (branch `trade-vident-model-upload`).
- **PROD, narrowly:** PROD `a0690a03` receives ONLY that commit, by cherry-pick; never a DEV merge and never a rebase.
  The six Trade Submission files are byte-identical on PROD and DEV (the scope read, 2026-09-25), so the pick applies
  clean. VALGATE and CI run on both pushes.
- **Nothing else moves to PROD:** no other DEV commit, the IRPT round 3 included.
