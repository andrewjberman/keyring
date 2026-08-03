# Wave-1 closes: F2, T5.A, WS-1 + the rulings they forced (2110-2225Z)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, DIAGNOSE

Delta since `go_wave1_t2ab_t3a_ovp_tranche1_rulings_1905-2110Z.md`. Every census workstream of the
five-task plan closed in this window; the implementation half is authored and gated.

## Closes validated (RAVC-4 at my level, evidence re-derived not accepted on report)

| item | close | what I verified MYSELF |
|---|---|---|
| T1.A trigger census | ACCEPTED | read census.yaml schema; disposition total reconciles 59/59; per-surface `pages_walked` recorded |
| T5.A delta census | ACCEPTED | verdict RETIRES-WHOLE=CONDITIONAL-YES{C1,C2}; re-derived the item-4 falsification independently |
| OVP WS-1 (39 rows) | ACCEPTED | re-derived the denominator from live S3: 7/7 vendor trees + every sub-path represented |
| F2 half-landed deploy | CLOSED | read CI run 30857702939 myself: SUCCESS, headSha 6cc8b9cd0e, previously-failing pair now OK |
| T1.C rows 4+7 | validated | deployed md5==ETag 44db6559; exclusion enumeration COMPUTED not hand-listed |

## Rulings issued

1. **F2: COMMIT ALL, APPLY NOTHING.** Grounded on the live function config I read (deployed env carries
   only legacy keys) -> the unapplied increment is INERT-but-ARMING. Applying it would have advanced a
   STOOD-DOWN workstream on the partner-rebate chain under a records mandate. Divergence DECLARED
   (marker + commit + ledger), not silent. The half-landed NEVER attaches to the deploy that was BEGUN.
2. **T1.C row-4: (b) PURE CANONICAL + (b+) declaration rider.** Decisive ground COO understated: the
   global axis is a UNION of feeder axes, so admitting non-trading dates in cot propagates Saturdays into
   the GLOBAL series -- never a cot-local choice. Excluded measured points enumerated, never vanished.
3. **T2.C clock: timezone-anchor coherence redline -> v2 MANDATED.** Fixed-UTC vs ET-anchored inputs
   inverts produce->publish across DST. DS's measured 14:16Z Orion landing decided it (44min summer
   margin, winter eats 60). v2 close DERIVED from the landing table; held 7/7 on the week.
4. **Floor-gate + THE GLOBAL RIDER (the highest-value ruling of the window).** Deleting the hard-DEFER
   for floor fires: endorsed. Honest-None per channel: endorsed (grounded on the plane's OWN declared
   `honest_none` contract, not preference). **RIDER: the global aggregate may never emit a silent SUM
   over a partial channel set** -- it would understate Opal aggregate AUA by the missing channel's
   magnitude: a confidently wrong client-facing number, worse than a freeze. Participation carried on
   every point; carry BOUNDED (2 trading days, BD_MAX_LAG precedent) with 3 labeling requirements.
5. **C1 = RE-SOURCE is the default**; droppable requires a VALUE-LEVEL diff (droppable is a CONTENT
   claim). `_latest_key` silent-aging closes with it. **C2 dispatched now, exercise required.**
6. Registry: U-5 RETIRED-BY-SUPERSESSION + row-13 SUPERSEDED, both with the zombie-writer and
   not-a-deletion-warrant riders. OVP vocabulary ratified + seal-decay rule + s.3.2a recoverability class.

## Two errors of mine, both caught by lanes, both owned on the record

- **Item-4 underscore-reader claim: FALSE.** I re-verified: `aggregate-mdpf` occurs EXACTLY ONCE in the
  estate -- the `aum.ts:474` comment stating the route still REQUIRES a redeploy. I read an intended
  architecture, in a comment naming its own unmet precondition, as a live reader. Corrected
  supersede-in-place @96fb06ca0b. *A source comment is a claim about an intended vintage, not a live fact.*
- **The parity CI I certified to Andrew as CLOSED had never passed.** Log-verified failure since 15:01Z
  (`MISSING_VENDORED` on an uncommitted file). Not a silent failure -- a LOUD one with no reader.
  Standing consequence set: **a gate is accepted on an observed green run with run-id cited, never on the
  commit that authored it.** Now green, first time ever.

## Findings that outlived their workstream

- **44% of the estate is unrecoverable on a missed pull** (17/39 feeds `current-state-no-date`). Schedule
  reliability is the ONLY control for those feeds -- this is why OVP and MDPF_GLOBAL are one program.
- **Dependency inversion at C1:** the CANONICAL emitter base-reads the chain slated for retirement.
  Retiring first would have silently starved those rows; no reader-count predicts it.
- **A second latent half-landed artifact** (AE, in passing): the never-applied v1 rule's dangling
  queue-policy reference had been silently blocking any clean full apply of the mdpf root.
- **Phantom instruments in the shared census** (CVO corollary): comp-estate AND comp-blast both carry a
  freshness family that does not exist live -- one census defect, two instruments.

## Compiler Tools

| tool | result |
|---|---|
| live AWS primitives (lambda get-function-configuration, s3 ls x9, s3api head-object, gh run view x3) | PASS -- every acceptance re-grounded; two claims falsified by them (mine + the reader claim) |
| git show/diff/grep spot-checks of cited lines | PASS -- cites verified before each acceptance |
| python yaml reads of census.yaml + vendor_asof_registry.yaml | PASS -- denominators + field completeness re-derived independently |
| comp-* | none this window: every question was live-state or content, which the comp-tools' own headers disclaim (DESIRED/census-vintage). Recorded rather than run for form. |

## Open at close

Apply gated: emission-schema convergence -> Lambda change -> source-map proof -> publisher migration ->
safe-apply -> 3-day per-stage evidence. T5.B gate set {CANON PROVEN, C1, C2} in motion. T4.A running.
Nothing owed by CTO.
