# MDPF_COTREMEDIATION — cottonwood pair decomposition fix: COO ratification of CTO 72604, and the pre-registered acceptance bar

**Author:** `2.0.0_SA_COO` · **2026-08-26T17:0xZ** · **Executing seat:** `0.4.0_DS_ClientPlatform~T`
**Operative instruction:** `1.0.0_SA_CTO` msg 72604 (2026-08-26T16:50:35Z) — **NOT superseded by this document.**
**Clock:** the 2026-08-27 13:30Z scheduled fire.

---

## 0. WHAT THIS IS, AND WHY IT IS NOT A TASK ORDER

⛔ **THIS IS A RATIFICATION AND AN ACCEPTANCE RECORD. IT IS NOT A NEW TO, AND IT DOES NOT
RE-CUT CTO 72604.** `1.0.0_SA_CTO` 72598 recorded that the issuer ratifies on wake; this is that
ratification. Scope, fix shape and guards in 72604 stand VERBATIM. Re-cutting a complete brief 20
hours from the fire would cost the executing seat a re-read and add no evidence.

⚠ **AND THE FILING IS ITSELF A CORRECTION.** I first wrote this as a task order in the `~T` lane.
`safe-commit`'s gate refused it on two counts, both correct: a NEW TO carries no `<proof_of_spec>`,
and `MDPF_COTREMEDIATION` is PIPELINE-REGISTERED so a new TO must name a stage-3 decomp run and the
cells it discharges — **and no such decomp exists for this repair.** The gate's own text says that
is a pipeline failure to surface, not a reason to cut the TO without one. **The right reading is
that this was never a TO: it is a ratification of an existing GO plus a durable acceptance bar, and
minting a TO to carry it would have manufactured pipeline debt to hold a table.** Recorded rather
than quietly re-filed, because the next seat with a bar to preserve will reach for a TO too.

**What it adds is exactly one thing.** The pre-registered recovery figures arrived in
`0.6.2_AE_PartnerETL~A`'s 72622 — a message. **The message scrolls, the artifact persists.** A fix
graded tomorrow against a number nobody can still find is graded against recollection.

⛔ **NO NEW GATE IS CREATED HERE.** No approval step, no sign-off, no hold that did not already
exist. The one decision reserved in s.4 is a SERVE decision that was already Andrew's.

---

## 1. THE FIX — scope unchanged from 72604

Fix `data/assets/scripts/gold/build_cottonwood_mdpf_pair.py` so the decomposition sees what the dim
sees. **Do not touch the dim, the lambda bundle, or any served object. Do not touch the identity
gate** — it refused loudly, wrote nothing, and is the only reason a ~$44.6M mis-split never reached
a client surface.

Root cause, source-confirmed and exercised by `0.6.2_AE_PartnerETL~A` (72583 / 72593 / 72622):
`:133 opal_assigned = assigned[assigned.model_id.isin(opal_ids)]` filters on the DIRECTLY-ASSIGNED
PARENT's opal-ness before the blend descent at `:159`. Accounts assigned to non-Opal containers
holding Opal children are dropped before `decompose` ever runs. `MODEL_DETAIL_SCOPE="all"`
(WSE_COTMDL, correct, landed 2026-08-25T10:38:32Z) took the blend 19/8 -> 46/17 parents/children and
made a pre-existing filter defect reachable for the first time. **A correct change made a latent
defect reachable; WSE_COTMDL is CLEARED — measured, not assumed.**

⛔ **THE BARE FIX IS A TRAP, and it is the half a reader skims.** Removing `:133` alone routes Opal
leaves into `by_model` correctly and sends every non-Opal leaf to `sleeves`, which is DROPPED —
**silently destroying `Client - Opal Supervised`, the named L1 segment Andrew identified at 16:34Z.**
Both halves or neither. Classify the segment FROM the D1 registry / taxonomy per
`org/tier1_exec/1.0.0_SA_CTO/deliverables/MP_TAXONOMY_COMPILED_REFERENCE_20260826.md` @966d26d717 —
**never a predicate minted inside this repair.** The F2 sleeve-drop stays correct for `by_model`
specifically; `by_model` is simply no longer the residual's only consumer.

---

## 2. ⛔ PRE-REGISTERED ACCEPTANCE — registered BEFORE the edit

Source: `0.6.2_AE_PartnerETL~A` 72622 s.3. That seat's independent reimplementation reproduces the
production figure `model=$140,410,927.00` **to the cent**, and the discarded side then accounts for
the entire gate delta — which is what moves this from *a* cause to **the** cause, itemised.

| # | Measure | Expected AFTER the fix |
|---|---|---|
| A1 | Opal Conservative Growth recovered | **$23,337,850.45** |
| A2 | Opal Ultra Short-Term Income recovered | **$11,896,309.76** |
| A3 | Opal Fixed Income recovered | **$8,442,396.91** |
| A4 | **TOTAL recovered** | **$43,676,557.12** — the identity-gate delta, to the cent |
| ~~A5~~ | ~~`Client - Opal Supervised` residual~~ | ~~$2,869,379.04~~ **SUPERSEDED -- see A5a/A5b** |
| **A5a** | `Client - Opal Supervised` (unallocated-weight portion) | **$1,476,313.07** |
| **A5b** | `SMAs` (L0) -> `DIVZ` (L1) -- the Opal SMA sleeve | **$1,393,065.98** |
| A6 | decomposed total | $147,047,720.63 -> **$190,724,277.75**, matching dim opal EXACTLY |
| A7 | identity gate | **FAIL -> PASS** |
| A8 | `by_model` key count | 5 -> **6** (gains `Fixed Income`) |
| A9 | ad-hoc `{"qa_local": true}` on `mdpf-gold-lambda` | `a4_objects_built` 6/12 -> **12/12**, `errors{}` empty |

**Pre-registered before the edit is the whole point: a pass is then a prediction met, not a number
tuned to.**

---

## 2a. AMENDMENT 2026-08-26 ~17:5xZ -- A5 SPLITS IN TWO ON A SOVEREIGN RULING

**Andrew-direct 17:42/17:45Z (recorded by `1.0.0_SA_CTO` @9261c99991, relayed 72806).** Two things happened and only one of them changes a number:

**(1) THE BASIS SURVIVED SOVEREIGN VERIFICATION.** He bet that ~$22M of the Anna accounts sat outside named Opal Models, then **looked at the accounts himself and withdrew his own bet** -- *"you have the correct approach... your estimate of 2.87m checks out."* The blend-weight arithmetic is confirmed at account level by the sovereign. **A1-A4 and A6-A8 are UNTOUCHED.**

**(2) THE BUCKETING OF ONE SLEEVE WAS WRONG.** The `DIVZ SMA` sleeve in *9237 is an **OPAL SMA**. It buckets to **SMAs (L0) -> DIVZ (L1)**, NOT to `Client - Opal Supervised`. The original A5 and the landed re-cut `4e0410825e` both carry that $1,393,065.98 inside the residual label. **The prior classification of the sleeve as NON-Opal is the defect.**

⛔ **A5a AND A5b ARE PRE-REGISTERED HERE BEFORE EITHER VALUE EXISTS** -- same discipline as A1-A9, and committed for the same reason: the message scrolls, the artifact persists.
⚠ **A5a + A5b = $2,869,379.05 against the original A5's $2,869,379.04.** One cent, float. **Stated NOW so a 1c gap at grade time reads as a met prediction rather than a discrepancy someone has to chase.**

⛔ **THESE ARE EXPECTATIONS TO BE CONFIRMED BY MEASUREMENT, NOT ASSUMED** (CTO's own condition). **A5b is a re-bucket BETWEEN TWO OPAL BUCKETS -- firm AUM does not move. If it moves, that is a finding, not a rounding story.**

**THE BUCKETING IS NOW THREE-WAY AND COMPLETE ON HIS WORDS:** Opal Models -> Models (Primary/Custom) · Opal SMAs -> SMAs (by strategy) · remainder -> `Client - Opal Supervised`.

**PRECEDENT, so this joins a bucket rather than minting one:** the served `by_model` union already carries `opal_div_sma` as a key on 49financial. Classify from that precedent and the D1 registry -- **never a predicate minted in this repair, and implement it as a ROUTING BRANCH, not a module-level dependency** (that instruction is what produced the import edge the first time).

**SEQUENCING RULED (i) at 72819:** the apply was measured NOT LANDED (lambda still 15:29:34Z / `3/897ecG...`, and `0.6.2_AE_PartnerETL~A` had deliberately not opened a NEVER#6 ledger across the hold), so the DIVZ re-cut folds into the SAME pin and the bundle is applied ONCE.

⚠ **A5 CARRIES A CORRECTION, AND THE SUPERSEDED FIGURE MUST NOT BE USED.**
`0.6.2_AE_PartnerETL~A` corrected itself at 72622 s.1: the residual is **$2,869,379.04**, NOT the
**$38,103,539.26** appearing in its own 72591 / 72593 / 72594, in `1.0.0_SA_CTO`'s 72596 / 72604,
and in `2.0.0_SA_COO~X`'s 72602. The earlier figure subtracted only the Fixed Income slice and
called the remainder residual, when ~90% of it is OTHER OPAL MODELS. **Those citations are STRUCK.**
The $8,442,396.91-vs-$8,442,396.91 exact tie-out is a weighted slice against the dim, is unaffected,
and stands. **A derived figure produced in passing and quoted onward by two Tier-1 seats within
minutes is how a wrong number acquires authority it never earned** — it was caught by its own author
before any lane built on it.

**A9 is the DAY's acceptance and is not a production acceptance.** That remains tomorrow's 13:30Z
scheduled fire: an ad-hoc run is a legitimate QA instrument and its artifacts are never production
evidence. The `qa_local` run writes ZERO S3 objects, so it costs nothing and leaves tomorrow's
acceptance signature intact.

---

## 3. GUARDS — as 72604 stated them

- Rule 14 commit-gate on every `.py` edit; `safe-commit.sh` under the executing lane's own author line.
- Deploy per the DS cycle (`safe-deploy`). **NEVER#6:** open a deploy-completion ledger entry in
  `org/critical_paths/change_management/` at deploy-start and CLOSE it in-session.
- ⚠ `comp-pipescript deployed` can false-STALE on a CRLF working-tree file against an LF S3 object
  (fixed @739c1ad8f9). **A `STALE` on a file just deployed is suspect; `MATCH` is trustworthy — the
  instrument is one-directional.**
- Identity-gate acceptance instrument: `recon_predicate_control.py` (5 arms).
- Surprise channel: one line to `3.0.0_SA_CVO`, cc `2.0.0_SA_COO`; executing seats do not write
  `org/surprise_channel/**`. OBSERVATION never interrupts; BLOCKING routes same-turn to the issuer.

---

## 4. ⛔ WHAT IS **NOT** AUTHORIZED — the expensive half

**A green ad-hoc run is NOT authorization for the corrected split to SERVE at tomorrow's 13:30Z
fire.** The change moves a client-facing model/non-model split by ~$44.6M. **That serve decision is
Andrew's and is already an open call at him**, raised by `2.0.0_SA_COO~X`. It is written down here
so that a seat reading a green 12/12 does not read it as a release.

**Land the fix, exercise it, report. Do NOT gate on the serve answer** — the fix is right whether it
serves tomorrow or the day after, and holding the code for the decision would waste the very clock
this record exists to protect.

---

## 5. REPORTING

ACK to `1.0.0_SA_CTO` + `2.0.0_SA_COO` + `3.0.0_SA_CVO`. Coordinate directly with
`0.6.2_AE_PartnerETL~A`, which holds the diagnosis, is LIVE, and has finished the itemisation
(72622 s.5 — nothing outstanding from that seat). **Report each of A1-A9 with its OBSERVED value
beside the expected one, whether it matched, and the evidence pointer.**
