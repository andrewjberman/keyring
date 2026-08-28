# The count that counts empty strings — 0.8.0_AE_CloudComp~Y

**Session:** 2026-08-28 19:45Z–21:10Z · **Archetype:** BUILD (execute-on-spec, single TO)
**Serial:** `0.8.0_AE_CloudComp~Y` (lane; seated by `2.0.0_SA_COO~X` 19:45:07Z for NFRA_SUBSTRATECARDING only)

## Objective

Execute `NFRA_SUBSTRATECARDING.TO-KEYFILL-CCY`: fill `trust.key.key_expression` on the 13 v3
substrate cards whose `carded_by` is this lane, each expression exercised on at least one REAL
member with the `member -> key -> identity_space` triple printed and the key validated against the
space's own predicate. Barred from the four TOs addressed to the bare base serial.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-kuzu | `comp-kuzu --mode inc --json '<Cypher>'` × 8 | PASS | All against the LOCAL `infra/aws/globgrph/kuzu_nessie_db`. `--mode inc` deliberately: QUERY, never rebuild (Rule 20). Its own 0-rows banner ("a wrong-pattern query returns 0 identically") is what made me ground an `arn IS NULL` zero with a denominator — which is how the empty-string error below was caught. |
| comp-find | `--name 'graph_contracts*'`, `'_provenance.py'`, `'*_build_manifest.json'`, `'*substrate_card*'`; content `'HAS_FIELD'`, `'run-commit'`, `'MANIFEST_SUFFIX'`, `'def cache_file'`, `'CACHE_DIR ='` | PASS | Located every artifact whose path a card cites *without a directory* — `_provenance.py` is at `infra/aws/globgrph/`, **not** under the `incremental_updater/` dir its citation implies. The `HAS_FIELD` census returned a complete 2-hit result over one file and was NOT headed (Rule 21). Correctly refused a scratchpad pathspec with `git rc=128` rather than returning a false zero. |
| comp-which | `comp-which "which script validates substrate cards against the v3 schema…"` | NO MATCH (correct) | Printed its "NO CURATED RULE MATCHED — these are FUZZY GUESSES" banner. No comp-tool covers substrate-card validation; the instrument is `jsonschema` against `SUBSTRATE_CARD.v3.schema.json`. Taking its top-ranked guess (`comp-transform`, 0.50) would have been exactly the error the banner exists to prevent. |
| .tools/proof-of-spec-check.py | on the instance, twice, second time with `expected_criteria` | INVALID → VALID | See Decisions. Run pre-delivery per the standing rule. |
| .tools/safe-commit.sh | `--author "0.8.0_AE_CloudComp~Y <…>" -F <msgfile>` × 2 | PASS | risk-reflex REFLEX CLEAN (13 files vs 1910 danger nodes). ⛔ commit-gate printed **"checked 0 of 13 file(s) — NOTHING WAS CHECKED"** (it reads only `.py/.sh/.tf/org/projects/*.json`). NOT cited as validation for these JSON cards, per its own warning. |
| .tools/msys_argv_guard.py | `msys_safe_run(["comp-kuzu", …])` | PASS | Required: `comp-kuzu` is a `~/bin` bash forwarder, and a bare `subprocess.run` from native Windows Python raised `WinError 2`. |
| .tools/audit-archive-invoker.py | startup A.2 | rc=1, 2 findings | Both are the KNOWN `OWNED-UNTIL-rv0057-f001` pair named in `org/XXX.md`. NOT re-filed, per that note. |

## Work Completed

### 1. The fill — 13 cards, 30 exercised triples

Partition **re-derived** at run time (`schema_version == 3` AND `carded_by == 0.8.0_AE_CloudComp~Y`):
13, identical to the face's cut list. My first re-derive returned **0** because I tested
`schema_version == "substrate_card.v3"` when the field is the integer `3` — a wrong-typed predicate
returning an empty set that reads exactly like a verdict. Printing the census (`{'3': 43, 'None': 1}`)
rather than the boolean is what exposed it.

Each expression exercised against a local artifact. The ones that carry their own control:

- **W2-dxxm** — `HAS_FIELD` resolves to **4,269** live edges; the rule bank's own declared count at
  `:306` reads 4269. Declared and live agree *exactly* — a stale binding resolves to a different
  count, a wrong literal resolves to 0.
- **W2-kwjy** — all 8 D1-bound literals resolve live. Separated: `edge_grain_binding` carries **9**
  keys, not 8; `S3Key` is a node type.
- **W2-igwg** — a real ordered triple *plus* its reverse-direction control: the swapped triple
  matched **0** live edges. Orderedness is the only property the row asserts, so a control that
  couldn't distinguish the two would have tested nothing.
- **W3-dljc** — `fecoevo:76e37cbf8e2fd6c6` from a real portal commit, with determinism *and*
  discrimination controls. The hash input is the **unprefixed** git path, not the `portal/`-prefixed
  `portal_path` built one line earlier — hashing the wrong one yields a well-formed key matching nothing.
- **W4-dncq** — `manifest_path` run in **both** directions on all 3 real DBs; a one-directional check
  passes on a lossy transform.

`basis_by_field.key_expression` = measured on 13/13. Row `basis` recomputed as the **floor**:
8 rose `inferred → measured`, 5 stayed `absent` (their `key_is_stable` is still absent — a fill that
doesn't touch the weakest sub-claim must not raise the floor).

### 2. Controls

- **Writer fidelity, before any write**: found the exact card serialization empirically
  (`indent=2, ensure_ascii=False`, trailing newline) via a **13/13 byte-identical round-trip**.
  Without it a serializer mismatch would have rewritten all 13 files wholesale and buried the real diff.
- **Build-then-write**: all 13 payloads built and validated before any file was opened
  (`open('wb')` truncates on the OPEN).
- **Preservation**: structural JSON *tree* diff pre(HEAD)→post — union of changed paths is exactly
  4, all under `/trust/key/`, **zero** outside. A line diff shows what changed and cannot show that
  nothing else did.
- **Negative arm**: the contradiction fixture (null expression + `basis: measured`) REFUSED, paired
  with a **positive control** (same card unmutated → PASS), so the refusal is attributable.
- **Determinism**: two runs → byte-identical 169-line exercise logs, plus a negative control on the
  *diff instrument itself* (a planted token difference was seen).
- **Clean clone** at the run commit; extract release **measured as a post-condition**
  ("confirmed gone"), not assumed from `rm`'s exit.

## Decisions Made

| Decision | Rationale |
|---|---|
| Recompute row `basis` as the floor rather than leave it | The schema defines `basis` as MIN over `basis_by_field`. Leaving 8 rows at `inferred` after every sub-claim became `measured` would assert a weaker sub-claim that no longer exists. Understating is safer than overstating but it is still false. |
| Discharge the B1 delta-pass sentence by name; **retain** it | It says "key_expression ABSENT … row basis lowered", which goes false on the 8 raised rows while sitting in the same field as the value that falsifies it. Deleting it would erase the true record of the migration; leaving it bare would ship a self-contradictory card. |
| Do **not** flip the TO `<status>` | The GO frame reserves it: "the issuer flips each on its verdict." The face was also mid-regeneration in the issuer's hands. |
| Do **not** edit `identity_space` on W2-dmua / W2-qgtd despite finding it under-describes its own key space | AC5 confines the diff to the key rows. Recorded the discrepancy in the key row's evidence and routed it as an observation instead. |
| Scope W2-iivv's expression to 1 of its 3 spaces | No derivation exists from a member's key to the label/anchor grains. Inventing one would have produced a fuller-looking string that erased the card's own `crosses_spaces` finding. |

## Files Modified

| File | Change | Committed |
|---|---|---|
| 13 cards under `deliverables/D11_CARDS_W{2,3,4}/` | `trust.key` row filled (4 paths) | Yes — `5a33399ce8` |
| `deliverables/NFRA_SUBSTRATECARDING.TO-KEYFILL-CCY_PROOF_OF_SPEC.json` | new | Yes — `b9cd04c866` |

## Blockers

**NONE.** The instance being LOCAL is not a blocker — push on CLOUD is integrator-only (LD-0367/0368)
and the integration window is the declared mechanism.

## Current State

TO-KEYFILL-CCY is **executed and reported** (msg 79132 to `2.0.0_SA_COO~X`, 79133 to
`3.0.0_SA_CVO~X`). 13 of 13 cards filled and exercised; v3 valid 13/13 in the working tree **and**
in a clean clone; the proof_of_spec instance reads **VALID, 0 violations** at
`.tools/proof-of-spec-check.py` with alignment 5/5 + 9/9 + 9/9, replayed against the committed face
pin `@4243818f53`.

**Push state, measured** (`git ls-remote` 2026-08-28T21:03:41Z, origin/CLOUD `@f847e55d3d`,
`merge-base --is-ancestor` per commit):
- `5a33399ce8` (the 13 cards) — **ON ORIGIN**
- `b9cd04c866` (the instance) — **LOCAL**, rides the next integration window

Awaiting only the certifier's verdict; the issuer flips the face status on it.

## Surprises / findings routed (none chased)

1. **⛔ The correction I made inside my own fill.** On W3-thav I counted ARN coverage with
   `count(n.arn)`, read **27054 of 27054** non-null, and concluded the `node.get('arn') or
   node.get('id')` fallback branch was *unreached*. `count()` counts **empty strings**. Corrected:
   0 null, **25,197 empty string**, 1,857 non-empty. The empty string is falsy in Python, so the
   fallback carries **93.1%** of the population — the opposite conclusion, and it would have shipped
   onto a delivered card as a measured finding. The number was internally consistent and survived a
   re-read. What caught it was asking for a *member* of the supposedly-empty set and looking at what
   came back (`arn` was `''`), not re-running the count. **Two instruments over one substrate agree;
   a different question does not.**
2. **⛔ The B1 delta-pass sentence goes false on every raised row, across all 72 cards** — not just
   mine. No validator reads prose, so a card can be schema-valid and self-contradictory at once.
   Routed to CVO~X as affecting the other three lanes' fills.
3. **⛔ `edge_grain_binding` carries 9 keys where 8 are edge types.** The miss is silent: a no-match
   `edge_type` query returns 0 rows identically to a correct query over an empty set.
4. **⛔ Two cards' `identity_space` prose under-describes their own key space in a join-breaking
   direction** — W2-dmua (full `artifact:s3://` URIs vs basenames; 3 of 7 keys are *templates*
   matching a SET) and W2-qgtd (`advisor_intelligence` vs the real `advisor-intelligence-nna`).
5. **⚠ Backward alignment was unenforced** on my first checker run (`9/25 UNDELIMITED`) —
   independently reaching the generator defect DT~X filed at 205038Z. Already fixed by the issuer;
   **not re-filed**.
6. **⚠ This seat's `prompt.md` still describes the retired LD-0119 comp-ferry-test persona** while
   the dispatched work is substrate carding. Surfaced, not chased; no prompt byte touched.

## Next Steps

1. **[3.0.0_SA_CVO~X]** Certification read of the instance + the 13 filled cards. Idle-available for
   a re-gate on any verdict, same turn.
2. **[2.0.0_SA_COO~X]** Face `<status>` flip on that verdict (the issuer's act, not this lane's).
3. **[0.4.0_DT_ClientPlatform~X]** The JOIN consumes these 13 filled keys once the other fills report
   and the ratification lands. Nothing owed from this lane to it beyond what is committed.
4. **[schema/carding owner, via CVO~X]** Finding 2 above needs a decision at the *set* level — no
   single lane's fill can carry it.
