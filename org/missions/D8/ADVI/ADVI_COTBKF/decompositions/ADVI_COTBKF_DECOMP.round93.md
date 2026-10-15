# ADVI_COTBKF decomposition -- ROUND 93 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-15) -- the CRM job takes its key from the grant record, so a second window needs no code change

**Status: DRAFT -> ISSUED in one issuance.**

**Numbering.** Round 93 is this pre-build; the second CRM window itself (new never-widen pair, grant, job, withdrawal) becomes round 94 and issues when Andrew's exact key arrives (CTO msgs 6235 and 6248).

**Cut on:** Andrew-direct 2026-10-15 ~20:5xZ (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md` @cb7075dd11), call `bccc`, VERBATIM: "Call bccc: Yes it was there to be super secret, i can break glass just let me know what to do for that." The zip WAS uploaded, so round 88's `head_object` 403 was a wrong key, a wrong place, or a refusal (a missing key also reads 403 to a role with no List). The CTO ruled (msg 6235) that the second window is a new pair binding the new key literal plus a key parameter in the job module. The round-88 job fixes its key as the module constant `KEY = opal_naming.key(...) + "/CRM_CottonwoodCapitalAdvisors.zip"` (`cotbkf_crm_match_job.py` L54) and its gate compares the grant's `policy_resources` to that constant (L467), so a different key needs a code change at the moment of the window. This cell removes that: the job reads its ONE key from the grant record (the artifact `0.7.0_AE_CloudOps~<seat>` writes from the signed pair), so the key flows one way, pair -> grant -> job, and the window is a record, not a commit. It does not need Andrew's key, so it is built now.

**Rule 24.** Domain: msgs 6235/6248 and the `bccc` record. Subtraction: the key parameter -> CB-co-1; the new pair, the grant, the job's run and the withdrawal -> round 94 (they need the key); a bucket parameter -> excluded (the bucket `opal-data-cottonwood` is the firm bucket named in register exception X15 and the signed pair; a different bucket is a different pair). Uncovered here: none.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-co-1` | `cotbkf_crm_match_job.py` derives its key and its session name from the grant record and validates them (one object, under the restricted CRM prefix, a `.zip`, no wildcard; session name `cotbkf-crm-match-<digits>`); the module constant is removed; the gate still demands the grant's single `policy_resources` entry equal the derived key; proven on stubs; no S3 | FWD-8, FWD-9 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~183` |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
