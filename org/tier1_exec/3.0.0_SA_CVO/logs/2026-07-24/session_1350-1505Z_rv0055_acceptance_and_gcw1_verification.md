# 3.0.0_SA_CVO — session 2026-07-24T1350Z..1505Z

**archetype:** VALIDATE

Main-fabric CVO, spawned 1350Z on CTO's authorization (134926Z) to close RV-0055 F-6 — main CVO
absent while main-fabric verify had no verifier and a governance review had no constitutionally
independent acceptor. Two verdicts delivered, both pushed and verified on `origin/CLOUD`.

## Startup

Registered PID 25160 (unique — no identity conflict; the `~Z` watcher at 13:04 is a different serial
and was left alone). Session serial file written per LD-0290. Persistent inbox Monitor armed
(`bmuzze9x1`). **Zero crons** (LD-0175). Owned-paths hook already wired; `audit-archive-invoker` ran
clean (`rc=0, 0 findings, baseline=2026-07-24T130625Z`). Adopted the main-CVO row as written —
**SYSPARITY not adopted**, no parity check at load, LD-0318 cron not armed (that is `~Z`'s).

## 1 — RV-0055 ACCEPTED-CVO (`831ebab30`, addendum `aaf28cc59`)

MSTR filed PENDING-INDEPENDENT-ACCEPTANCE, three-times proxy-ineligible, and asked explicitly not to
be rubber-stamped and not to have its counts carried. I re-derived rather than read: two engines
(python `re`, then `awk`), my own boundary predicate, positive control (the 3 itemized overrides all
hit) and negative control (650 pre-window BLOCKs excluded).

**Reproduced exactly:** 738 commits, 18 serials, per-agent roster line-for-line, tag resolution, both
endpoint UTC conversions off a −04:00 host, watermark genuinely held, ledger-hook 745/5/0, and every
OVERRIDE axis on the commit-scope log. F-1 discharged at the artifact, F-7 exact. Its "best result"
claim was **understated** — 120 tracked files across 9 snapshot dirs, 7 cited.

**Two corrections filed:**
- **CV-1** — BLOCK 9 filed / **15** measured. Non-material (BLOCK is the gate holding, not a bypass;
  every bypass axis was exact) but inside a sentence asserting a completed field-2 walk. MSTR tried to
  falsify it twice, both hypotheses died, then diffed outputs and found the cause: **`grep` silently
  enters binary mode on these logs and truncates its own output, exit 0.** Only BLOCK was hit because
  BLOCK records carry the long embedded violation text where the invalid bytes live — **the corrupted
  axis was the boring one nobody re-checks.** Conceded; amendment 2.
- **CV-2** — F-3's leak population 25 filed / **322–334** measured across three non-grep methods with
  the denominator printed. Routed to CTO, who was sizing the `send_message` gate that hour. MSTR read
  its own matcher and confirmed: it keyed on the **opening** `<invoke name=` token, and **321 of 322**
  instances carry none — structurally blind to ~100% of the defect it was built to count.

**I corrected my own verdict** (`aaf28cc59`): my binary-trap hypothesis for the F-3 census was
**falsified** by the control I asked for (`grep -rl` 33 == `grep -arl` 33 — `-l` only needs "does this
file match"), and I had **under-called** CV-2 at 43% when it is ~100%.

Outcome: watermark 0049 → 0050, tag `mstr-review-0050` @`67ea1930e` — verified present, pushed, and
the RV-0055 header stamped, all read at the artifact rather than taken from the custody report.

## 2 — GC-W1 PASS/VALIDATED (`6e6c8af47`)

Andrew re-pointed MDPF counts PRIMARY-through-to-VALIDATED (~1432Z), so this verdict is what makes
"validated" true; CTO rules W-2 off it and W-3/W-6 gate behind that.

Re-measured every headline from the four served artifacts myself, on a provably identical vintage
(global ETag `55a8b379…` byte-matched DS~A's). **All acceptance criteria reproduced**, including the
full §4A model-axis distribution cell-for-cell. The 05-21 exercised case holds (Global `None` on 5 of
5 core models while 49F serves 6,788 real core accounts). The residual sweep's control passes — it
detects an injected discrepancy, so it is not reporting silence.

**All four of DS~A's self-named soft joints closed or narrowed.** The one that mattered: my first
residual sweep used DS~A's own predicate, which proves arithmetic and not the *choice*, so I re-ran
core-keys-only — same single date, +7 instead of +92, delta exactly the SMA preserve. **Predicate-robust.**

**Two sharpenings to CTO, neither blocking:** the mechanism clause is refuted too (cottonwood's
provenance @07-22 is `measured`; the `frontier_stamp` is 49F's and Global's, so Cottonwood does not
enter via the frontier stamp), and on the frontier date Global's core cells are **overwritten** by
`ad_frontier` — **stamped, not composed** — so a "sum what is present" law does not reach them.

**Near-miss worth recording:** I first verified a 247-line draft; the submitted version is 310 lines
and adds §4A, the most decision-critical section, written after the Andrew re-point. I caught it only
because DS~A's cover note referenced claims I had not seen — luck, not mechanism. Surfaced to COO as a
convention gap: an amended deliverable needs a re-notify with the new commit-ish.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-surface-check` (auto via `safe-commit`) | OK — no critical surface | 3 commits, all confined to my own deliverables tree |
| `comp-pulse diff` risk-reflex (auto) | REFLEX CLEAN | denominator printed: 1 file vs 1,511 danger nodes, each commit |

**Why no other comp-tool ran:** both work items were *artifact-measurement verification*, not estate
search or traversal — the questions were "what do these served bytes say" and "what does this audit
log count," which no comp-tool models. Retrieval was `s3api get-object` (operational data-plane,
explicit-Z, never `aws s3 ls`) and `git show` at pinned commit-ishes, both off-rail by the
graph-presence principle. **This is the honest reason, not a skipped step** — and the session's own
central finding is that routing a census through the wrong instrument is how you get a plausible wrong
number.

## Carried forward

- CV-2 with CTO for `send_message` gate sizing: **~325, not 25**, and the closing-tag-only class is
  the majority case needing a named test.
- P2 candidate (endorsed by MSTR, routed not built): a comp-tool emitting the field-2 census for a
  window range with denominator **and predicate** printed.
- P2 unknown-unknown to CTO: nothing in W-1..W-7 measures whether the frontier stamp is *correct*.
  `ad_frontier` handles ABSENT (honest-None) but has no answer for PRESENT-BUT-STALE.
- Open in my scope, unstarted: PORTAL_AUTHHARD W2+, smartx first-conversion.

**The line worth keeping from today:** a window MSTR *could* have self-accepted would have shipped
both errors unexamined — and those are precisely the low-stakes windows nobody looks at twice.
Proxy-eligibility gates on stakes; the measurement defects were uncorrelated with stakes.

— 3.0.0_SA_CVO
