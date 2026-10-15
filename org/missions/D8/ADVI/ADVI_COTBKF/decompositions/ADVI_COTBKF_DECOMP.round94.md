# ADVI_COTBKF decomposition -- ROUND 94 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the CRM job takes the grant record's PATH as an argument

**Status: DRAFT -> ISSUED in one issuance.**

**Numbering.** Round 94 is this second and last pre-build; the second CRM window (new pair, grant, job, withdrawal) is round 95 and issues when Andrew's exact key arrives (CTO msgs 6235, 6248).

**Cut on:** the finding of round 93's worker `~183`, row `ADVI_COTBKF-D1-W183-S1`, and my own read at the merge (@3ede2bbc46): round 93 made the job take its KEY and SESSION NAME from the grant record, but the record's PATH is still the module constant `GRANT_REL` (`cotbkf_crm_match_job.py`, `_load_grant`), which points at round 88's record in `deliverables/0.7.0_AE_CloudOps~CB1/`. The second window's grant record is a different file (the first is committed history and must not be overwritten), so without this cell the job order of the window would begin with a code change under time pressure. Andrew's word, call `bccc` (record @cb7075dd11): "Yes it was there to be super secret, i can break glass just let me know what to do for that."; the CTO (msg 6235): a new pair plus a key parameter in the job module, "cut as round 91 after C-S3" (renumbered by the rounds since).

**Rule 24.** Domain: the row's one defect. Subtraction: the grant-record path as an argument -> CB-cp-1; everything else in the window (pair, grant, job run, withdrawal) -> round 95. Uncovered here: none.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cp-1` | `cotbkf_crm_match_job.py` takes `--grant PATH` (a repo-relative path to a grant record, under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/`, ending `GRANT_RECORD.json`, no `..`, an existing file) with the round-88 path as the default; the run record names the grant file it used; the key still comes ONLY from that record | FWD-8, FWD-9 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~184` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
