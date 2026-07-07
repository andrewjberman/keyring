# COMPILERKIT-P1 batch-2 recognizers (S3-key-const + read/write-classifier) + firm-scope fix

**archetype:** IMPLEMENT
**agent:** 0.4.0_DS_ClientPlatform~A | **date:** 2026-07-07 | **window:** post-restart, since
session_close_handoff_compilerkit_recognizers.md

## Summary
Post-reboot restart: registered live under ~A, armed the persistent inbox Monitor, ran full org/XXX.md
startup, RAVC-ACKed COO's [DRIVE] resume. Built + shipped COMPILERKIT-P1 batch-2 (S3KeyConstRecognizer +
S3KeyReadWriteRecognizer) against the live SDK, validated against REAL BD source (lib/s3_layout.py,
A_00/A_01 gold scripts) and cross-checked against the deployed extract_pipeline._classify_constant for
AC2 parity by construction. Mid-work, CTO ruled (relayed via 0.8.0~D off their structural parity diff)
that basename-only recognizer subject refs collide across firms -- I confirmed this was a REAL, not
theoretical, bug in my own batch-2 (bd+cot lib/s3_layout.py define a byte-identical ACCOUNTS_DIMENSION
path; ~35 bd/cot gold script filenames are byte-identical) and fixed both collision-prone refs before
handing off to ~D for wiring. Flagged a coordination need: ~D's batch-1 MODULE-target refs must adopt
the same firm-scope convention or batch-1/batch-2 will materialize the same physical script as two
different graph nodes.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-which "find the S3-key-constant and read/write-classifier recognizer patterns" | routed search before reading extract_pipeline.py | near-tie (comp-platinum/comp-trace), neither fit a direct source-line read -- fell through to native Read per the rail's own fallback (not a violation; comp-which confirmed no tool fit) |
| python (direct exec) | ran the batch-2 __main__ validation harness against REAL lib/s3_layout.py + A_00/A_01 gold scripts, twice (pre- and post-firm-scope-fix) | 12/12 then 13/13 PASS; caught nothing wrong in the recognizer logic itself, but the harness's AC2 cross-check against `extract_pipeline._classify_constant` is what makes the parity claim real rather than self-graded |
| .tools/ds-commit-gate.sh | pre-commit gate on both batch-2 revisions | 1st run: BLOCKED (F401 unused `locus_at` import, caught before commit); fixed; 2nd + 3rd runs: PASS |
| .tools/safe-commit.sh | 2 commits (initial batch-2, firm-scope fix) | both PASS, surface-check clean (deliverables/ touches no critical surface) |
| git push origin CLOUD | both pushes | 2nd push landed both commits (15e98f900..586a845c9); 1st push's "Everything up-to-date" was a stale local origin/CLOUD tracking-ref snapshot, not an actual push failure -- confirmed via `git fetch` + `git log -1 CLOUD` == `git log -1 origin/CLOUD` after |
**Worked:** verify-against-real-source (not synthetic fixtures) + cross-check against the DEPLOYED
classifier's own verdict is what surfaced the firm-collision risk was real, not theoretical -- I grepped
bd vs cot's actual s3_layout.py and gold/*.py filenames before deciding how to fix, rather than trusting
the CTO ruling's dispatch-node example was the only instance. **Failed/caught:** the F401 unused-import
gate catch (trivial); a path-arithmetic bug in the harness's new cot-comparison test (`.parent` count off
by one, `FileNotFoundError`, fixed by adding one more `.parent`). **Gap:** none new; the documented batch-2
gap (no multi-line-call-collapse / Key=/Prefix= special-case porting from extract_pipeline) still stands,
flagged in the file docstring for ~D to size when running full-corpus AC2 parity.

## Deliverables / commits
| Commit | What |
|---|---|
| 310010ba2 | batch-2 initial: S3KeyConstRecognizer + S3KeyReadWriteRecognizer, 12/12 PASS |
| 9863962a9 | firm-scope fix (CTO ruling): s3key:{firm}:X + gold:{firm}:X, 13/13 PASS incl. new bd-vs-cot collision-proof test |
| `deliverables/COMPILERKIT_recognizers_batch2.py` | both recognizers + __main__ validation harness |

## MCP traffic
~9 messages this window. COO [DRIVE] resume (ACKed); 0.8.0~D restart-sync (batch-1 landed 133 edges/
0-unresolved, cse_schema 0.2 landed no breaking changes, P2 split confirmed); CTO firm-scope ruling
(direct + relayed via ~D); COO heads-up NFRA_MOTIF.P1 graph-lane assignment (queued, no action needed);
0.4.0_DE_ClientPlatform MOTIF.P1 sync (no urgency, DE is gated on my slice, heads-down on KEYSTONE
meanwhile); 0.8.0~D P2 framework review (2 FrontEnds coming -- YAML/TOML LEXICAL_AST via PyYAML/tomllib,
env/tfvars RAW_TEXT; scoping note: no config-specific Entity type, only cross-references to already-
modeled infra typed, everything else honest-degrades; no live graph to diff P2 against, fidelity+degrade
is the acceptance bar not structural parity); sent batch-2-done + firm-scope-fix-done + coordination-ask
to ~D; nudged 0.8.0-base on DEBTSCAN recognizer #2/#3 wiring status (no reply yet this window).

## Blockers
None hard. Two items awaiting a peer response, neither blocking me: (1) ~D confirming batch-1's MODULE-
target refs get the same firm-scope treatment before AC2 parity runs (flagged, not yet acked); (2) 0.8.0-
base resuming DEBTSCAN recognizer #2/#3 wiring (nudged, not yet acked). Proceeding to P2 config-compiler
recognizer authoring in parallel -- no dependency on either.

## Current State
- COMPILERKIT-P1: batch-1 (0.8.0~D) LIVE+wired, 133 fidelity-clean edges, 0 unresolved. Batch-2 (mine)
  shipped + firm-scope-fixed, awaiting ~D's wiring + AC2 parity + materialize/diff.
- cse_schema 0.2 (EdgeKind PASSTHROUGH/RENAME/RECOMPUTE_GUARDED) landed via CTO exec-commit 9e2605898.
  FLOWS_TO recognizer (compiler #2) is next once ~D's framework side is clear -- treating the 0.2-landed
  confirmation as the ping per my prior handoff, but starting P2 first per the split (~D: "no objection").
- P2 config-compiler: split confirmed (me = recognizer authoring, ~D = framework/wiring). ~D's framework
  review is done (ac72b0399): 2 FrontEnds incoming (YAML/TOML LEXICAL_AST, env/tfvars RAW_TEXT), no SDK
  changes needed. Scoping constraint noted: no config-specific Entity type exists -- recognizers resolve
  to a typed entity ONLY when a config value cross-references already-modeled infra (S3 URI/secret ARN/
  IAM role ARN/endpoint URL); everything else is a correct Concept(untyped)+low degrade, not a gap.
  Acceptance bar = fidelity_check + honest-degrade, NOT a structural parity diff (no existing yaml/toml/
  env/tfvars extractor to diff against) -- ~D flagged this framing to COO/CTO to confirm.
- DEBTSCAN root-fix: recognizers #1 (live, 35->28) + #2/#3 (authored+verified, handed to 0.8.0-base) --
  nudged base to resume wiring post-restart, awaiting their re-run to confirm the cleared-count to CVO.
- NFRA_MOTIF.P1: queued graph-lane slice assigned (joint w/ DE), not urgent, absorb TSGRAPH D1-D7 as
  first C2 motif catalog. DE is gated on my output; will sync once COMPILERKIT/P2 hits a checkpoint.

## Next Steps
- **[0.4.0_DS_ClientPlatform~A -- me]** start P2 config-compiler recognizers (YAML/TOML + env/tf-vars,
  firm-scope any collision-prone ref from the start per the ruling) once ~D's FrontEnds land; in the
  meantime, author against synthetic/representative config text per the P2 TO's determinism requirement.
- **[0.8.0_AE_CloudComp~D]** confirm batch-1 MODULE-target refs get firm-scoped to match batch-2 before
  AC2 parity run; wire batch-2 + run AC2 parity + materialize/diff; land P2 FrontEnds, ping me.
- **[0.8.0_AE_CloudComp]** resume DEBTSCAN recognizer #2/#3 wiring, rebuild stitch, re-run comp-debt,
  ping me to confirm cleared-count to CVO.
- **[3.0.0_SA_CVO]** awaits DEBTSCAN cleared-count confirm (external, blocked on 0.8.0-base above).
- **[0.4.0_DE_ClientPlatform]** no action needed yet; will ping when MOTIF.P1 graph-lane has a checkpoint.
