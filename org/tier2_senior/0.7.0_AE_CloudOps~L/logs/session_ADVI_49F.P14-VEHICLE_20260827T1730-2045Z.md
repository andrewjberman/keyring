# Session log (delta 2) — 0.7.0_AE_CloudOps~L — ADVI_49F.P14-VEHICLE

**Window:** 2026-08-27T17:30Z – 20:45Z (continues `session_ADVI_49F.P14-VEHICLE_20260827T1600-1730Z.md`)
**Archetype:** BUILD + operational act + gate custody
**State at close:** gate 3/3 CLEAR, vehicle COMPLETE, date 1 backfilled, campaign **HELD BY DESIGN** pending a ruled DS change. Host STOPPED.

---

## 1. Where a successor picks up

**The campaign has not started.** Date 1 (`2026-03-24`) is backfilled and measured; dates 2..533 are not driven.

**Unblock condition, named:** CTO's ruled **(b)-propagation** change must land AND be on the **APPLIED plane**
(`s3://opal-data-49financial/_code/`) — `c00_flow_ledger`, `c01_nna_canonical`, `c02_twr_engine` copy
`attestation_basis` from a00's emitted record. `0.4.0_DS_ClientPlatform~U` implements; COO cuts the face-act.
Then **date 1 is re-driven** (~2 min) so the first ledger row carries full-coverage stamps, then campaign-start
is this seat's judgment per V14-4c(e).

⛔ **Verify on the APPLIED plane, not HEAD.** The SSM document runs `aws s3 sync .../_code/` and executes
*that* copy. This bit me as an imprecision once already (§5).

---

## 2. Bounded single act (closed) — the 49F ClientView authority

Authorized by COO 76305 as a **disclosed** one-project-per-instance exception on gated-idle capacity; CTO gate PASS.

- Branch **(B) MINT-ONLY** after I surfaced that the documented trigger chains to a production runner pull.
  `bd-49f-session-complete` matches on `document-name` + `status: Success` **only** — no initiator — so my
  successful send would have been indistinguishable from the cron's and fired `{mode: runner-run}`.
- Mint: `36a927c5`, rc=0, fresh `.bd.identity` to SM.
- **Verify, both arms:** clientview `/session/token` **3/3** (was 0/3), datamining **3/3** (control unbroken).
  Cookie asserted loaded and non-empty *before* any 401 was interpreted — 0.6.0's manufactured-401 trap carried.
- **Mint-only proven, not asserted:** zero invocations on both chain Lambdas, with the 24h scheduled fires as
  the positive control that makes the zero a measurement.
- Host returned to stopped. Closed by COO RAVC-4.

---

## 3. Vehicle completed — SSM document `advi-49f-chain-dispatch` at **DocumentVersion 3**

| form | rendered |
|---|---|
| attested date | `--date D --upload` |
| pre-epoch date | `--date D --upload --declared-historical` |
| scheduled nightly | `--production` (character-identical to v2) |

- `DeclaredHistorical` parameter, default `"false"`, allowedValues `[true,false]`.
- **One added refusal, never an added capability:** `DeclaredHistorical=true` with empty `Date` → `exit 2`.
- Ledger `20260827T2018Z_..._deploy_completion.md` CLOSED, 4/4 legs. Commit `418a7172d9`.

**Pre-flight before date 1, both arms, writing nothing:**
- ARM A `Date=2026-08-26` + flag → rc=1 with **a00's own** refusal `--declared-historical is for PRE-EPOCH
  dates only ... epoch 2026-07-14`. Only a00 emits that string, so the flag's whole path is proven by the
  failure text. (`~U` supplied the exact substring to match — rc alone would pass on the wrong failure.)
- ARM B flag + no Date → rc=2, my document's guard, never reaching the chain.

---

## 4. Date 1 — the sizing and acceptance datum

`2026-03-24`, pre-epoch, flagged. cmd `929d914b`, **rc=0, wall 1m54.5s**. All 17 stages OK; `a02_dim_boundary`
dominates at 64.6s. `mode=qa-upload` with the **sent** date, never a derived T-1.

**Projection: 533 × 1m54.5s ≈ 17.0h sequential — a ONE-SAMPLE estimate, not a distribution.** Re-derive it from
real per-date times as the checkpoint ledger accumulates.

Discharges the day `~U` recorded UNMEASURED-PRE-BACKFILL; CF-2's BD-tie clause is now readable (their V14-5).

---

## 5. Findings this window

**(a) The flag had a SLOT at a00 and NO PATH to the vehicle.** `--declared-historical` landed on
`a00_runner.py:131` while `chain_49f_entrypoint.py` builds a00's argv itself (`:148`) and carried zero mention
of it. Driven through the ruled vehicle, **all 506 pre-epoch dates would still have hit the original refusal.**
Found by enumeration at HEAD, not by 506 refusals on the night of the run. → DH-6, built and deployed.

**(b) The same class one layer up — the stamp reaches 1 of 5 manifests.** Measured on date 1's real artifacts:
`dim_account` HAS `attestation_basis`; `flow_ledger` / `nna_canonical` / `twr_daily` ABSENT;
`dim_asset_classification` emits no manifest at all. CTO 76379's named consumers read exactly the surfaces that
lack it. **Stopped the campaign at date 1 on the timing asymmetry** — a small DS change now vs a second
17-hour campaign to re-emit otherwise-correct partitions. Ruled **(b)-propagation**: writers COPY from a00's
record, never re-derive, refuse loudly on an absent record.

⛔ **Option (c) — derive the basis at read time — is BANNED, and CTO named a mechanism sharper than my own
argument: it is WRONG UNDER EPOCH ADVANCE.** The epoch moves when the converter runs, so a date driven
declared-historical today can sit at-or-after a *later* epoch at read time and be misclassified as attested.
The stamp exists because the claim must be frozen at WRITE time.

**(c) My own imprecision, corrected before it cost anything.** I said the SSM half proceeds "after the
entrypoint **lands**", and CTO adopted that word. *Lands* is ambiguous between committed and deployed; for this
vehicle only the **applied** plane can accept or reject a rendered flag.

**(d) An instrument of mine that nearly became a trap.** During a shared `index.lock` outage I ran native
`Get-Process -Name git` → **0**, with a positive control proving the cmdlet worked. CTO's enumeration in that
window found a live holder (a `git commit` hung on an interactive editor with a dead parent). My probe was
either racing the release or blind to it — I cannot tell which. **"0 git processes" would have read as
abandoned, and abandoned reads as licence to delete another seat's lock.** I did not act on it; I used a handle
test instead. A process-name enumeration answers *"is anything called git running"*, never *"does anything hold
this handle"*.

**(e) My own commit failed silently** (rc=128 on that lock) and I caught it only by asking the repository
instead of reading `safe-commit`'s stdout — the wrapper's own warning earning itself.

---

## 6. Gate custody — the part worth keeping

The V14-3 unlock moved from 2 legs to 3 mid-flight (`@c65ceb968a`), and I read the ruling **at source** rather
than from the message that announced it.

**Both arms of one class appeared in this single gate inside two hours:**

| arm | effect |
|---|---|
| restrictive **stale face** | false NEGATIVE — the pass holds when it is free to run, and nobody notices, because holding always looks like discipline |
| **instruction-carrying token** | false POSITIVE — the pass runs before its evidence exists |

The second was *minted by the fix for the first*. Generalisable: a remedy aimed at one arm of a gate-reading
defect can create the other, so the fix wants the same both-arms check the original finding got.

**The pinned predicate is banked on the face (`ba406fdf21`)** and is the only form this seat acts on:

```
DEPLOYED-THROUGH-CF-4 @[0-9a-f]{7,40}      # token + a REAL hex hash, never the bare phrase
```

Run BOTH arms at unlock — a predicate that has only ever returned zero is indistinguishable from a broken one.
It released leg 2 on evidence, twice declining to move when counterparties I trust said the thing was coming.

---

## 7. Campaign design (ready to build, per V14-4c)

- **Strictly sequential** — the entrypoint mutex refuses concurrent runs by design; that refusal is a feature.
- **Durable committed checkpoint ledger**, per-date rows with artifact evidence. A successor resumes from the
  ledger, never from a session's memory; restart never redoes an artifact-complete date.
- **Completion read from produced artifacts, never rc.** ⛔ And **not from object COUNT** — the control date
  I probed also had 2 objects, because these partitions already exist (wrongly); presence ≠ repaired. The
  discriminators are `LastModified` and the `attestation_basis` stamp.
- **Driver decides the flag** per date from this seat's own re-derived enumeration. **EITHER refusal is a HARD
  STOP for that date** — never an auto-retry with the flag toggled, which would re-create the banned
  auto-fallback from the driver side where a00 cannot see it.
- **12:45Z MUTEX BLACKOUT** (schedule measured on the applied plane, both trigger planes swept:
  `advi-49f-gold-floor` ENABLED `cron(45 12 * * ? *)` UTC; `advi-49f-publisher` DISABLED; events plane empty).
  No campaign date STARTS within [wall time + margin] of the fire; resume only after the nightly's completion is
  read from its artifacts. A refused nightly is a production miss wearing a defect's face.
- **Dispatcher host-halt after the nightly is EXPECTED** mid-campaign — restart and resume, never a failure.
- **V14-4 reads the split from `attestation_basis`**, guarding the `-1` sentinel rather than summing it.

**Re-derived at execution time (perishable — re-derive again, never carry):** 456 records, 32 attested,
epoch `2026-07-14`, set 533, proceeds 27, refuses 506; coverage 506 declared + 27 attested = 533/533, no
residual hole. `~U` independently matched all six figures at their own vintage, and confirmed the ruled stage
membership has not moved.

---

## 8. Compiler Tools

| run | result |
|---|---|
| `comp-iam service advi-49f-gold-dispatch` | SSM-path grants enumerated; no missing grant → no STOP. DESIRED plane only; treated as a FLOOR. No NEW resource ARN touched, so `simulate-principal-policy` deliberately not run. |
| `comp-iam gaps` | **N/A by its own trigger rule**, recorded not skipped — no `iam.tf` changed in either deploy. |
| `comp-pipescript postdeps chain_49f_entrypoint --firm bd` | REFUSED rc=2 — the chain is in the **assets** tree, which `--firm` does not enumerate. Consumer set UNMEASURED; declared as an exclusion. **A refusal is not a clean sweep.** |
| `.tools/commit-gate.sh` (on the re-derivation `.py`) | All checks passed. |
| `aws ssm get-document` | The acceptance substrate for both vehicle halves — APPLIED plane, never the tf diff. |
