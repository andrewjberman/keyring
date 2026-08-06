# Memory content-staleness census — the first measurement

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Date:** 2026-08-06. Memory repo @edb8446 measured; annotations landed @69ff771 (memory repo).
**Subject:** the item left OPEN + UNMEASURED by the 08-05 memory-corpus audit (@5b7ab845d4):
*"content staleness across the 1,010 memory files — I read 3 closely and cannot say how many are
still TRUE, and a recall-addressable file asserting a retracted rule is worse than an orphan."*

## HEADLINE

**~20% of memory files carry at least one stale load-bearing clause — measured twice, by two
instruments with different derivations, landing on the same rate.**

- **Deep sample (semantic):** 30 files drawn by seeded RNG (`seed=20260806`, printed, reproducible)
  from the 1,010-file population (1,012 md minus 2 index files; 661 feedback / 177 project /
  171 reference / 1 user). Per-file verdicts below. **6/30 (20%) stale or partial-stale**;
  95% binomial CI ≈ 8%–39%, i.e. **~80–390 files corpus-wide**, point estimate ~200.
- **Mechanical pass (pointer rot):** all 1,012 files scanned for workspace-path citations —
  402 files carry ≥1, 868 distinct citations tested against the workspace + portal roots.
  **80 files (19.9% of citation-carrying) hold ≥1 unresolvable citation** (109 citations), an
  UPPER BOUND: known false-positive modes are script-relative `lib/` paths (resolve beside their
  gold scripts) and illustrative tokens (`.tools/foo.py`, `data/X`). Confirmed-real classes inside
  it: renamed tools (`.tools/ds-commit-gate.sh` ×5 — renamed 2026-07-07), renamed docs
  (`org/AGENT_START_HERE.md`), archived docs (`infra/aws/TERRAFORM_PIPELINE_STRATEGY.md` — the same
  dangling-cite CLAUDE.md itself carried until 08-05), retired serial trees (`3.1.0_SA_CVO`,
  `1.1.0_SA_CTO`), wrong-dir cites (`.tools/inbox-watch.sh` ×2 — it lives in `org/mcp/`).
  Full candidate map: scratchpad `memory_dangling_confirmed.json` (session artifact, not committed).

The two instruments share no derivation (one reads meaning against live state, one tests path
existence), so the convergence is evidence, not an echo.

## Sample verdicts (30/30, every file read)

**TRUE / durable — 20:** prohibition-invalidates-open-gates · allocation-no-delta (dormant-scoped) ·
f6-vintage-anchor (**verified live in S3, object updated 2026-08-06 01:31Z**) · firm-sep-relation ·
freshness-mtime-proxy · verify-deployed-bytes · liveness-ground-telemetry · no-tolerance-served ·
proactive-gap-audit · signal-bounded-emit · tilde-lane-owned-paths (self-updated) ·
delegated-mcp-gateway · window-boundaries-data-date · deck-generation · website-domain (matches
Rule 23) · total-return-build-lane (dated routing record) · comp-iam-condition-blind ·
git-push-hang-gcm · harness-delete-guard · inf-advisor-book-paths.

**TRUE-core with stale tails — 4:** cvo-architectural-corroborator (cites retired `/cvo-loop`) ·
cc-2.1-hooks (version-pinned runtime facts, current behavior unverified — correct hygiene, kept) ·
graphify-landscape (Andrew decisions durable; `3.1.0_SA_CVO~A` seat tail retired) ·
option-c-auth (method likely standing — **carries the security flag below**).

**PARTIAL-STALE (a load-bearing clause now false) — 3, ALL ANNOTATED @69ff771:**
- `feedback_agent_context_serial_is_not_per_process` — its "CLAUDE.md currently says" premise was
  fixed; the lesson is absorbed into law (XXX.md Step 1 + 1b-E).
- `feedback_pre_stage_tf_must_be_comment_wrapped` — its `--force`-is-the-escape sister-note
  contradicts Rule 14a's corrected scope (08-05): `--force` never bypasses a gate failure or lane
  refusal; `GIT_COMMIT_AUTHOR_OVERRIDE` is the sanctioned escape.
- `project_opal_assets_...totalvalue_136_8m` — **"CTO~B is GONE — do not route to 1.0.0_SA_CTO~B"
  is false today** (CTO~B committed session work 2026-08-06). Ruling core stands.

**STALE — 3, ALL ANNOTATED @69ff771:**
- `feedback_loop_max_270s_cadence` — a 2026-04-27 blanket ("no exceptions, all loops ≤270s") that
  predates the entire loop-retirement arc (LD-0157/0164/0166/0175 + LD-0288/0289/0293) and the
  persistent-Monitor migration. **The exact "recall-addressable file asserting a retracted rule"
  hazard the census exists for**: a fresh agent recalling it would fight standing law.
- `feedback_coo_lane_split_nfra_comp_to_coo_b` — vestigial: all seven subject projects read
  `status: complete` (measured), `2.0.0_SA_COO~B` NOT REGISTERED. **A live specimen of the
  RETIREMENT shape** the FIVE_SHAPES audit named as candidate-sixth (an axis going vestigial, the
  denominator silently contracting) — this census is the incident its hypothesis lacked.
- `project_aor_validation_lane_cvo_b_ld0277` — a self-dated 07-13 snapshot titled "current state"
  whose blocking condition (INF chain frozen) has since flipped (inf-pipeline v1.7.99
  deployed+verified 08-06).

## ⚠ SECURITY FLAG — routed to Andrew, deliberately not self-remediated

`feedback_option_c_auth_supersedes_devbypass.md` embeds a **plaintext portal credential**
(`michael@opalinvest.com` + password, opal-users-v2). Mitigation: the memory repo is local-only with
NO remote (per the 08-05 audit — itself a sitting Andrew item). Not scrubbed unilaterally: it may be
a deliberate test credential, and scrubbing alters another session's banked artifact on a security
judgment that is Andrew's. **Decision at Andrew: scrub / rotate / accept.** Added to my open-calls.

## What was done vs what is proposed

**DONE (this session):** the measurement (both instruments, denominators above); dated
provenance-preserving UPDATE annotations on the 6 stale/partial files (memory repo @69ff771 —
additive notes in the corpus's own established convention, no rewrites, no scope adjudication of any
sovereign word).

**PROPOSED, not taken (remediation scale is a funding decision):**
1. **Full-corpus walk** at ~20% expected yield ≈ ~200 files needing annotation — a bounded, dull,
   parallelizable job; a build lane could run it off this census's method (seeded batches, dated
   additive annotations, verdict ledger). CRO does not dispatch; CTO/COO staff it if wanted.
2. **The cheap standing control:** the corpus convention that saved 4 sample files from staleness is
   SELF-DATING + VERSION-PINNING (file 25 pins its runtime version; file 16 carries its own UPDATE).
   A one-line authoring norm — *volatile facts (seat state, project phase, "currently says") carry
   their date in-line or don't get banked* — prevents the two worst classes found here at zero
   standing cost. Doctrine-adjacent; offered to the memory-governance owner.
3. **Pointer-rot lint candidate:** the mechanical pass is ~40 lines of python; run at memory-commit
   time it would catch renamed/archived cites at write time. Gate candidate, owner's call.

**Method notes:** sample drawn before any file was read (no selection-on-suspicion); every verdict
traces to a read of the file plus, where the claim was live-checkable cheaply, a live check (S3
head, broker liveness, project JSON status). One probe artifact hit during measurement, disclosed:
my project-status read of `NFRA_COMPAWS.json` failed on a cp1252 decode (my probe's locale default,
not a corpus defect); the 6/7 sibling reads sufficed for the vestigial verdict.
