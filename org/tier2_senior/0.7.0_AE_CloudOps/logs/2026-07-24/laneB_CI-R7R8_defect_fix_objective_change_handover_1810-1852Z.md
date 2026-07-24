# 0.7.0_AE_CloudOps~B — a defect in my own landed code, an objective that moved, and a handover

**archetype:** MIXED

**Session:** 2026-07-24 18:10Z–18:52Z · lane `~B` · TO `MDPF_CHANNEL_INDEPENDENCE.CI-R7R8`
**Continues:** `laneB_CI-R7R8_roster_and_divergence_1722-1810Z.md` (rows 7+8 delivered @`fd6e92faa`).
**Landed this window:** `9f0214122` (defect fix), `2bf7dd5e1` (roster `gate_policy`). Committed, not pushed.

---

## 1. A peer lane found a real defect in code I had already called verified

`0.7.0_AE_CloudOps~A` (manifest lane) reproduced a hole in `divergence()` at 182648Z: an **UNKNOWN channel is
excluded from `known`, therefore from the spread, and nothing put it back into the signal** — so a dark
partner channel published `signal=False`.

**I reproduced it before fixing, and it was worse than reported:** with **all three** channels dark, `spread`
is `None` and the signal *still* read `False`. The entire estate unmeasurable, published as healthy.

**The part worth keeping:** `channel_lags` was already correct — `lag` stays `None`, never `0` — and I had
written the principle into that very docstring (*"an unknown rendered as 0 is the shape that lets a frozen
channel read healthy"*). **The roll-up one layer up did not honour it.** A correct principle written next to
code that does not implement it is not a control. My mutation pass the hour before had tested five things and
not this one; mutation testing bounds what you thought to break, not what you failed to think of.

Fix: three **named** limbs — `spread` / `rising` / `unmeasured-channel` — plus `signal_reasons` on the face of
the output, so a reader never infers *why* it fired and **a quiet signal never implies all three limbs ran.**
Tests 17 → 20; deleting the new limb drops the suite to 18/20, so the regressions bind.

`~A` was running a correctly-constructed labelled interim overlay and asked the right question rather than
only patching around it. Told them to drop it — one definition, in the module.

---

## 2. The governing objective moved mid-edit, and I was in the wrong file when it did

COO `[STOP]` 183817Z. **Andrew ~1832Z: MDPF migrates to the `opal-data-assets` monolith ENTIRELY.** CTO
corrected the PRD's governing objective @`6b69efc57` and expanded the closure set **12 → 16**. The freshness
gate reading the bd tree is **M1 — THE SIX-DAY FREEZE — and is a path to DELETE, not a literal to
parameterise.**

I had measured M1 independently at 183442Z, ~8 minutes before the census landed: the gate reads
`opal-data-bd/schwab/silver/rps` while the producer reads
`opal-data-assets/schwab/08242234/silver/fact_rps_s2` — different bucket, prefix **and** date-format
convention, with nothing structurally coupling them. Routing it instead of building against it is the only
reason that time was not wasted.

**I reverted my uncommitted trigger edit immediately.** Two reasons, and the second is the durable one.

---

## 3. The collision — and why it was NOT an objective problem

While I was editing `mdpf-daily-trigger/lambda_function.py` for row 7, the **base `0.7.0_AE_CloudOps` lane
committed row 10's scheduled floor into the same file** (@`5c3ca9e7fc`). Two lanes of the same serial family
live in one file with no coordination.

**The `[STOP]` stopped me for the objective reason; the collision was independent of it and would have
survived a correct objective.** I only noticed because the editor warned me the file had changed under me —
and **"the editor happened to warn me" is not a control.** COO has taken it as a routing failure (his) and a
gate candidate (CTO's); same shape as DS~A's "the author happened to notice" earlier today.

Recommended the file get **one owner**. COO routed rows 10+13+16 to the base lane — already in the file,
already holding the deploy-completion ledger, and `safe-apply` on a live client-facing gate wants one applier,
not a merge. I handed over the roster interface at 185044Z and am not editing that file.

---

## 4. The coupling that COO escalated as a defect in CTO's own acceptance criteria

**Rows 13 and 7 must land in the same change.** Row 13's acceptance — *"gate config shows no `opal-data-bd`
prefix"* — is **satisfiable with monolith paths written as literals**: row 13 passes, row 7 is re-broken at a
new address, two closure rows green and the defect intact. The migration is the one moment the
parameterisation is free, because the read path is being rewritten anyway.

COO's framing: *that is the easiest-pass test failing on a row in the document that introduced the
easiest-pass test.* Asked CTO to amend row 13 to assert the paths are **roster-derived**, not merely bd-free.

---

## 5. What I put in the handover so the base lane does not re-measure it

- **The trigger role has ZERO grants for BOTH buckets row 13 needs** — no `opal-data-assets` (feeds), no
  `opal-data-mdpf` (roster key). Enumerated all 10 Sids. **Rule 22a bites hard**: `comp-iam` will report
  GRANTED for an `opal-data-assets` prefix this role has never held, because it models `(action)` only.
- **They cannot `import` my module** — `files[]` is `source_dir`-scoped and the import-closure gate refuses a
  zip whose imports are not registered. They vendor `trading_calendar` for row 10, so vendoring is their path,
  but vendoring the roster reader would make a **second reader**. Recommended reading the JSON's data fields
  inline: the definition stays in one place, no reader forks.
- **Cadence ≠ tolerance.** The roster states the basis explicitly (`expected_last_trading_day`, offset 0 — the
  basis the gate already uses). Deriving max-lag from cadence instead would take 49F from 2 → 1 and start
  deferring on healthy days.
- **The legacy schwab path uses `date=YYYYMMDD`; the monolith uses `date=YYYY-MM-DD`** — the partition parser
  changes with the re-point, not just the prefix. Passes review, fails at runtime.
- **Row 13 makes inflection and cottonwood visible to this gate for the first time** — a behaviour change
  beyond a re-point, and both will show real lags on day one.

---

## 6. Two findings I logged and did not act on

- **A backfill is invisible to every partition-date reader we have, including mine.**
  `opal-data-bd/silver/fees`: 8 partitions (07-15..07-22) all LastModified **`2026-07-23 18:20:54`, the same
  second**. `~A` measured the identical shape in cottonwood (10 partitions in one minute). A partition-date
  gate reads it as healthy daily delivery. It is the PRD §3.1 as-of/process-time split used as a diagnostic:
  the **gap** carries it, neither field alone. Offered to `~A` to build once rather than twice; awaiting their
  call on ownership.
- **`/mdpf/custody_source` reads `schwab`** — the cutover has already flipped, so the path row 13 deletes is
  the LIVE one.

---

## Compiler Tools

| Tool | Command | Result | Value |
|---|---|---|---|
| `comp-glob` | `**/build-and-upload*` | 2 files | Found the packaging gate that makes a `_shared` import unbuildable — the finding that shaped the handover |
| `comp-grep` | (prior window) | — | Not re-run this window; the work was source reads of known files plus live AWS state |
| `.tools/commit-gate.sh` | 2 `.py` files | All checks passed | Rule 14, before `9f0214122` |
| `.tools/safe-commit.sh` | `-F` body, `~B` author | `9f0214122`, `2bf7dd5e1` | Rule 14a + `-F`-not-`-m` |
| `comp-surface-check` / `comp-pulse` | auto via safe-commit | PASS / REFLEX CLEAN | denominators printed (2 files vs 1511 danger nodes) |

**Raw `aws s3 ls` + `ssm get-parameter` used for live state** (operational reads, not gated inspection):
partition frontiers per feed, the fees write-time clustering, and `/mdpf/custody_source`. `comp-freshness`
would have answered "is it stale" but not "do the gate and the producer read the same object", which was the
actual question — and that question is what found M1.

**`comp-iam` still not run:** no new boto3 call is deployed by anything I committed. It moves to the base lane
with row 13, where I have flagged that it is **necessary but not sufficient** for the two new buckets.

---

## Open at others

1. **[2.0.0_SA_COO]** push `9f0214122` + `2bf7dd5e1` (`fd6e92faa` + `05af353d7` confirmed on `origin/CLOUD`).
2. **[1.0.0_SA_CTO]** amend row 13 to assert roster-derived paths (COO escalated); the partner-#4/IAM wording;
   the pluggable layout resolver (item c); the trading-calendar convergence (row 8 prerequisite).
3. **[0.7.0_AE_CloudOps base]** rows 10+13+16 in the trigger; handover delivered 185044Z.
4. **[0.7.0_AE_CloudOps~A]** who owns the backfill/write-lag discriminator.

## Caution carried forward (COO, measured)

**The mdpf gold code running in production is 51,999 bytes from 2026-07-21T17:42:40Z against a 119,499-byte
repo HEAD — 20 commits and +67,500 bytes behind**, and the runner has not reported telemetry since 07-18
(five trading days; 07-18 was a Saturday, so this is not a weekend artifact). **Rows landing as
`data/mdpf/**` Python are TRUE-BUT-NOT-LIVE until `s3://opal-data-mdpf/code/` is refreshed.** My rows 7/8 are
not in that class — but nobody should report a row in this tree closed off a repo state without asking where
it runs.
