# /self-drive D2 — tick 124

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~16:5xZ
**Ticks covered:** 121–124 · **Carrier:** `org/XXX.md:633` @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO`

```
COMPLETION: 2 of 10 -> NOT DONE     ledger: 39 (committed @96b1565942)     open_tos: 17
MOVEMENT: 12 seats / 44 commits.  POSITIVE CONTROL FIRES: 1.0.0_SA_CTO = 2
OPEN CALLS: 0 adjudicable, 0 new reserved.  ALL-RESERVED tell did NOT fire (queue empty, not reserved)
```

---

## 1. The gate came to this seat and was EXERCISED, then the apply was VERIFIED independently

`0.7.0_AE_CloudOps~R` filed a Terraform IAM apply under the pre-existing per-apply sign-off. **I did
not sign on the filing; I signed on one field.**

- The first simulate run came back in the **false-deny shape with THREE missing context keys**. The
  confirming run was described as *"control-proven on both keys."* **Two is not three.**
- Answer: all three supplied, missing-context list **EMPTY** — ⭐ **and the emptiness was FALSIFIED,
  not assumed.** That seat dropped one key and the field **reappeared naming that key.** A positive
  control **on the rendering itself**, which is the arm missing from every IAM verdict produced today.
- The misreading, named: *"both keys"* meant the two **silver feeds**, never the context keys. **A
  noun did two jobs in one sentence.** Cost of the challenge: one turn. Cost of the alternative,
  measured earlier today: an authorized grant, revoked.

**SIGNED @92248.** Applied 16:2xZ: saved plan file (so what landed is byte-for-byte what was
reviewed), one address, 0 added / 1 changed / 0 destroyed, eleven pre-existing Sids set-identical by
symmetric difference, and **a sibling prefix that still DENIES** — never-widen proven, not asserted.

## 2. ⛔ Verifying my own signature found a 27-DAY estate outage

```
  comp-iam reconcile, first attempt:  census 2026-08-05, AGE 664.2h, TTL 24h -> REFUSED
  "nothing was compared, so nothing can be concluded"
```

**My first grep of that output returned EMPTY — and empty would have read as NO DRIFT.** The tool's
own refusal text is the only thing that stopped a false clean.

>> **Andrew pointed the fabric at `comp-iam` this afternoon. Its DESIRED surfaces answered. Its
   APPLIED surface had been REFUSING since 2026-08-05 because nobody ran it. A tool that refuses
   correctly still fails the estate if nothing ever triggers the refusal.** <<

Refreshed at 16:35:34Z (216 roles). Reconcile then ran: the applied grant appears as drift in **neither
direction**. ⚠ Stated limit: **absence from a drift list is not proof of presence** — `~R`'s read-back
remains the stronger evidence for that limb.

## 3. A peer's retraction applied to MY finding, and I chased it three ways

`0.7.0_AE_CloudOps~R` retracted one clause: its run predated my refresh, so a role was absent because
**uncovered, not clean.** My own coverage finding was measured two hours pre-refresh — **same risk.**

| attempt | result |
|---|---|
| borrow `~R`'s 0→270 arm | **arm later disclosed CONFOUNDED** — that seat's apply landed between the runs |
| run gaps against the OLD census | ⛔ **flag does not exist** — command errored, and my three counts came back `0,0,0`. **THE ERROR'S ZEROS.** |
| grep the census for source paths | ⛔ **POSITIVE CONTROL RETURNED ZERO** (`RoleName` vs `role_name`) — control dead, measurement VOID, discarded |

**The structural answer, on the parsed object:**

```
  POSITIVE CONTROLS   role_name 216 · arn 216
  SOURCE TOKENS       scripts/gold 0 · runners_49f 0 · .py 0 · data/assets 0 · black_diamond 0
```

>> **The census carries NO source paths, file names or tree information. It cannot determine which
   trees a call-site scanner walks, because it does not know trees exist. My zero CANNOT be a census
   artifact.** Structural, not empirical — independent of the refresh, the apply, and the confound. <<

**STANDS:** the assets gold tree — every 49F runner — is outside `comp-iam`'s call-site population.
NOT a Lambda-vs-EC2 issue; EC2 roles are covered 243 rows deep in the other tree. **NOT measured:** how
many files that hides. Said when filed, not upgraded now.

## 4. ⭐ Three self-corrections in four minutes, all on one root cause

`0.7.0_AE_CloudOps~R`, `0.7.0_AE_CloudOps~M` and `2.0.0_SA_COO` each corrected their own claims within
four minutes — **all on runs that predated the census refresh, where absence read as cleanliness.**
That is a correction PROPAGATING rather than being rediscovered per seat.

⭐ **And the instrument property worth keeping:** the gaps headline totals were **byte-identical**
across pre- and post-refresh runs (14 missing / 292 deny-present / 2 resource-mismatch) while the body
went from 0 to 270 mentions of a role. **A SUMMARY INVARIANT TO A COVERAGE CHANGE CANNOT WARN YOU THAT
COVERAGE CHANGED.**

⭐ **A confound known to the author and absent from the filing is invisible to every reader.** `~R` had
it in its own memory file, noticed the asymmetry, and corrected a claim standing unchallenged and
load-bearing for someone else's conclusion. **It cost my arm and saved my finding.**

## 5. And I nearly reported a false stall on my own truncation

Tick 123's movement census ran through `head -5`; my seat was not in the visible five — **which reads
exactly like the positive control failing.** Unbounded: 11 seats, my own two commits present.
**I `head`'d a census while running the control that exists to catch a false stall** — the rule I have
cited at other seats all day.

## RESERVED cards still at Andrew

- D3's order relative to D8 · whether the flow-ingestion defect widens the ruled 22.
- The PERFRP publish card, ONE card TWO limbs: (a) did 08:5xZ narrow the 04:0xZ ratification;
  (b) PER-FAMILY or PER-SET (per-set unsatisfiable by construction).

## Compiler Tools

`git log --format=%aI` derived cursor + FULL unbounded movement census · `directives-check.py --json`
· `comp-iam reconcile` / `refresh-census` / `gaps` (243-row and 270-row positive controls) · parsed
census structure via python (216/216 controls) · `safe-commit` with post-commit STATE verification.
**No `head` on any census in this tick.**

**PUSH STATE, MEASURED:** `96b1565942`, `7e97154c34` + earlier LOCAL/on-origin mix; this log LOCAL.
`origin/CLOUD` last read `c85701ebca` — **perishable and stale, an integration window has run since.**

**State:** `ARMED` · next tick on the cron.
