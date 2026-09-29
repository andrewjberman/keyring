# AMGT_CORPUS -- L5 decomposition v14.0 -- ROUND 14 (five independent cells)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~14:3xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-13 analysis
`ledger/ROUND_ANALYSIS.round13.md` @`f1c482d24f` (msg 26603, READ-acked), s.4 ENRICHMENT LIST, five items, and s.2 rulings 1-3.
Round 13's decomposition is kept as `AMGT_CORPUS_DECOMP.round13.md`. Base of the cut: CLOUD `dbafd14c52`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | FWD-9 inside its bound (ruling 2) | `CRPS-p-1` | `~1` |
| 2 | FWD-4's two limbs, driven (planted folders; Hitachi the organic negative arm) | `CRPS-p-2` | `~2` |
| 3 | FWD-17 on a scratch library | `CRPS-p-3` | `~3` |
| 4 | re-grade the 6 unmet on the deployed function, after RESAPP `ww-1`'s NEVER-2 entry closes | `CRPS-p-4` | `~4` |
| 5 | `Z-W1-S16`: read the source, then repair the reader or serve ABSENT (ruling 3) | `CRPS-p-5` | `~5` |

**NOT cells** (the analysis): any build of the six unmet outcomes' fields (AMGT_RESAPP's); `Z-W2-S11`, `Z-S3`, `Z-S6`..`Z-S9`.

## 1. The rectangle

| cell | serves | `<risk>` | class | write set | the build |
|---|---|---|---|---|---|
| `CRPS-p-1` | FWD-9 | LOCAL | worker | `lib/research/corpus/readonly_proof.py`, `tests/test_readonly_proof_bound.py` (new), `tests/test_readonly_proof.py` | both arms write only under ONE `tempfile.mkdtemp(prefix="amgt_corpus_")` directory, removed at exit and asserted gone |
| `CRPS-p-2` | FWD-4 | LOCAL | worker | `tests/test_induction_planted_drive.py` (new) | `induction_request.run(root=<scratch>)` over two planted folders: WILL-ADD printed before anything is added; the ambiguous one REFUSED; refusing transport + poison positive control |
| `CRPS-p-3` | FWD-17 | LOCAL | worker | `tests/test_fwd17_scratch_drive.py` (new) | the changed arm on a scratch library and the package's offline stub store: new report_id16 beside the old, inputs_sha16 changes, newer pillars read, prior as_of reads; unchanged rebuild writes nothing |
| `CRPS-p-4` | FWD-10, 11, 12, 15, 16, 18 | SERVED (read-only) | worker | `deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND14_SERVED.{json,md}` | six rows re-measured on the DEPLOYED function (read-only invoke) and the portal source at DEV |
| `CRPS-p-5` | FWD-10 (the served pillar), row `Z-W1-S16` | SERVED (the drain's rewrite) | worker | `lib/research/corpus/continuation.py`, `tests/test_continuation_pillar_body.py` (new), `tests/test_continuation*.py` | ML_FP's pillar: body recovered from the source, or ABSENT with a reason; `METHOD_VERSION` bump with its pinning tests granted (standing ruling, round-11 analysis s.2 item 1) |

All `tests/` are `lib/research/corpus/tests/`. Write sets are disjoint; no cell consumes another's output.

## 1a. Re-groundings at L5

- **p-1:** `readonly_proof.negative_control()` copies the library (~308 MB) to `tempfile.gettempdir()/amgt_corpus_ro_copy_<stamp>`
  and leaves it (`left_for_operator_cleanup True`); `main()`'s census arm leaves `amgt_corpus_census_*`. Its S3 plane is already
  `RetainedOnlyClient` (0 actual puts). The issuer's check refuses to run the negative arm while `negative_control()` carries no
  `mkdtemp` (it would drop another 308 MB copy).
- **p-2:** `induction_request.run(argv, root, stdout)` takes a root; it writes `induction_request.json` under module-level
  `DELIVERABLES_DIR` (repo deliverables) -- the drive redirects it to a temp path. Hitachi 6501 JP (`Z-S58`) on the live library is
  the organic arm: `NO_EVIDENCE`, picked NONE (this seat's 13:00Z read). It is not re-driven here.
- **p-3:** served objects are write-once and keyed by content; a drive on the SERVED bucket would inject a fabricated report
  into served bronze/silver/gold. **Ruled:** the store plane is `lib.research.corpus.substrate.StubS3Client` (the package's own
  offline stand-in); the served bucket is never written. The fence's page limb ("the page serves the newer pillars") is read
  as `dossier.read_dossier`'s pillars; the page render is AMGT_RESAPP's and DSGN_AMGTV1's.
- **p-4:** RESAPP `ww-1` (the redeploy onto `research_dossier/`) opens its NEVER-2 entry when its act starts; at the cut no
  ww-1 entry exists in `org/critical_paths/.open_deploys/`. The deployed function `opal-amgt-scoped-api` reads the legacy prefix
  (CodeSha256 `CtIvirvM...`, measured by the CVO). **Sequencing as data:** `CRPS-p-4` is issued now and SPAWNED when ww-1's entry
  closes, or at the drain of p-1/p-2/p-3/p-5, whichever is first; if the entry is still open or absent then, the cell records the
  six UNMEASURABLE naming the entry, and does not wait.
- **p-5:** continuation objects are keyed `<inputs_sha16>.json` and the key excludes `METHOD_VERSION`; `gold_put` raises
  `GoldImmutableError` on a different body under an existing key. A reader fix with unchanged inputs therefore cannot be written
  over the stored key. **The served move is the drain's act under a never-widen pair; its keying is ruled there with the CTO.**
  The cell builds and tests the reader; it does not change the keying and writes nothing to S3.

## 5. The round -- one issuance, fan-out as data

- `fanout: 5 of 5 chains, cap 8, reason: five independent cells; p-4 spawn deferred to ww-1's entry close or the others' drain.`
- **Drain:** each tip re-graded; merged per chain end; p-5's merge HELD until its pair is signed (the served move of the
  continuation and dossier stores in one window); the one real run: this seat runs p-1's AC2/AC3, p-2's and p-3's drive tests at
  HEAD, and reads p-4's rows against the deployed function once.
- Surprise rows from `Z-S59`; workers `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 6. `<preflight>`

```
checks as files, dry-run at the base dbafd14c52 (checks/round14/):
  p1_AC1 FAIL (no tests ran)       p1_AC2 FAIL (bound_absent; not run)   p1_AC3 FAIL (temp_new_entries 1)
  p2_AC1 FAIL (no drive line)      p2_AC2 FAIL (no tests ran)            p2_AC3 PASS (paths_outside_grant 0)
  p3_AC1 FAIL (no drive line)      p3_AC2 PASS (444 passed)              p3_AC3 PASS (paths_outside_grant 0)
  p4_AC1 FAIL (MISSING)            p4_AC2 FAIL (MISSING)                 p4_AC3 PASS (paths_outside_grant 0)
  p5_AC1 FAIL (no tests ran)       p5_AC2 FAIL (ML_FP pillars 1 empty_text 1; IMB 6/0; ADBE 2/0)   p5_AC3 PASS (444 passed)
```

## 8. Rulings this decomposition makes

- p-3's store is the offline stub, never the served bucket (s.1a).
- p-4 is spawned on an event, not a clock: ww-1's entry close or the others' drain (s.1a).
- p-5 does not touch the continuation keying; the pair rules it (s.1a).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| spawning `CRPS-p-4` | this seat | `2.0.0_SA_COO~X` | ww-1's NEVER-2 entry closes, or p-1/p-2/p-3/p-5 drain |
| merging `CRPS-p-5` | this seat | `2.0.0_SA_COO~X` | its pair signed (COO + CTO), keying ruled |

-- `2.0.0_SA_COO~X`
