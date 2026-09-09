# CTO ADJUDICATION -- NFRA_CLDGRPH, 2026-09-09 ~18:56Z: WHICH DIRECTIVE HOLDS THE STITCH KEY (S71)

**Mode:** `/open-calls --adjudicate NFRA_CLDGRPH` (Andrew-direct 2026-09-03 ~05:2xZ: a scope question at receipt is the CTO's
to rule, the loop keeps cycling). **Ruler:** `1.0.0_SA_CTO` (L4/L10 owner). **Pitched by:** `2.0.0_SA_COO~A` (94637, drive tick
17) on `3.0.0_SA_CVO`'s row `NFRA_CLDGRPH-S71` (ARMED, disarm_owner `0.8.0_AE_CloudComp`, surfaced 18:44Z).
**Andrew's standing word at this terminal (~12:5xZ):** adjudicate and push forward on NFRA_CLDGRPH; this is that.
**Broadcast the same turn** to `2.0.0_SA_COO~A`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`; Andrew reads it at this terminal.

## THE TWO WORDS, both his, verbatim

- **2026-07-07**, quoted in `.tools/stitch-refresh:6-8` and the hook header: *"for a SOLO contributor whose local working tree IS
  the canonical state, the derivation should read the local repo directly"* -- *"Replaces the cloud stitch-produce"*. Mechanism:
  `.tools/git-hooks/stitch-refresh-post-commit.sh`, installed in `.git/hooks/post-commit` on this laptop (2026-07-07T18:24:14Z,
  read at HEAD `527cd9386d` this turn) and on site Z; backgrounded; publishes `stitch/stitch_graph.json` + `stitch/stitch_marker.json`
  (`producer=stitch-local`, `git_sha` = HEAD at publish) to `s3://opal-313476888478-globgrph/` within ~60 s of any commit touching
  `portal/`, `data/*/scripts/`, `org/modules/graph/` or the two derive scripts.
- **2026-09-02 ~17:5xZ**, the ratified endpoint of THIS project: FWD-7 *"The estate keeps one graph story, and the per-machine
  copy is retired rather than kept alongside"*, DONE WHEN *"after the local copy was switched off"*; the PRD's title he ratified:
  *"no machine is in the compile business"*. PRD v0.6 rows S23-S26 (@`30027295be`) direct the cloud producer repaired, the stitch
  source folded into the served projection, the consumer repointed, the local store retired LAST.

## MEASURED AT THIS SEAT, 18:55Z (a second instrument on the live plane; the CVO's 18:29Z read is the first)

| read | value |
|---|---|
| `stitch/stitch_marker.json` (s3 cp) | `built_at 2026-09-09T18:49:23Z`, **`producer stitch-codebuild`**, `git_sha de590a7d`, 29,267 nodes / 61,275 edges, `artifact_sha256 a7c1d589...` |
| head-object marker / artifact | LastModified 18:49:37Z (330 B) / 18:49:36Z (38,845,013 B) |
| the CVO's read at 18:29:11Z (S71 evidence) | `built_at 17:53:55Z`, **`producer stitch-local`**, `git_sha 9b99b493` (a site-Z commit), 29,320 nodes / 61,833 edges |

So within one hour the ONE key had TWO writers: site Z's post-commit hook at 17:53Z and round 6's cloud build (F-3's ad-hoc run)
at 18:49Z, and the two derives disagree by 53 nodes and 558 edges. The next commit on either clone touching a trigger path would
put the laptop-derived artifact back over the cloud one, silently (the hook is invisible to the committing seat; CloudTrail showed
0 PutObject events in the 17:50-17:56Z window, a logging gap). On this laptop the derive has refused on every run since 09-05
(grain sentinel), so this laptop is inert by accident; site Z's derive passes, so site Z is the live overwriter.

+-- CALL 1 of 1 --------------------------------------------------------------+
  **Which directive holds `stitch/stitch_marker.json` and `stitch/stitch_graph.json`:
  (a) the 2026-07-07 local post-commit hook, or (b) PRD v0.6's cloud producer?**
  Two of Andrew's words name the same S3 key in opposite directions; the CVO named
  the L4/L10 owner as the reconciler; round 6's F-3 has already published (b) once.
  ------------------------------------------------------------------------------
  **REC (2.0.0_SA_COO~A) --** (b), and the hook stops publishing to the shared key;
  a one-line v0.7 addendum to S23's accept; the uninstall a device act per clone.
  ------------------------------------------------------------------------------
  **RULING -- (b). THE CLOUD PRODUCER HOLDS BOTH KEYS FROM ITS FIRST PUBLISH, WHICH
  HAS HAPPENED (18:49:23Z). The 07-07 word is NOT lifted by this seat; it is
  SUPERSEDED BY HIS OWN LATER WORD, and the record says so in its own header.**
  Grounds:
  1. A direction bound to a stated premise does not bind past the premise. The
     07-07 premise -- ONE contributor whose local tree IS the canonical state -- is
     false in fact: two fabrics, ~10 seats, canonical state on origin/CLOUD, and a
     site-Z commit published the shared key at 17:53Z without its author knowing.
     His 09-02 ratification names the same object (the per-machine copy, the
     compile business) and the opposite direction. Later word, same object: governs.
  2. NEVER-5 (his complete veto): a hook on every clone republishing a derived
     artifact to the key the cloud producer owns is a build-alongside pipeline with
     a duplicate writer on one output path -- the shape the veto names.
  3. The live plane already shows the cost: two producers, two node counts, one key.
  FORM: a NEW ROW S29 in PRD v0.7 (not a clause on S23: a different act, a different
  owner, its own three planes), depends_on S23 -- the dependency is met by the
  18:49Z publish; the rule-initiated nightly stays S23's own accept. Reversible:
  the hook line can be re-added by one word of his; nothing is deleted from S3.
+-------------------------------------------------------------------------------+

## S29 -- THE HOOK RETIRED ON THREE PLANES (the row as landed in PRD v0.7)

- **EXECUTABLE (device act, per clone):** the `stitch-refresh-post-commit` line removed from `.git/hooks/post-commit` on this laptop
  (`0.0.0_AB_MSTR`, the device's integrator) and on site Z (over the agentbus to site Z's integrator); the other two hook lines
  (`missions-refresh`, `closeout-comp-state`) untouched. **Site Z first** -- it is the live overwriter.
- **INSTRUCTION (lane `0.8.0_AE_CloudComp`):** `.tools/git-hooks/stitch-refresh-post-commit.sh` retired with a tombstone naming
  this record; `.tools/stitch-refresh` keeps the 07-07 words VERBATIM in its header, marked SUPERSEDED by the 09-02 word and this
  record, and REFUSES to publish to `stitch/` with a non-zero exit whose text names the cloud producer (`opal-stitch-produce`).
- **RESIDUE:** `${TMPDIR}/stitch-refresh.log` on each device noted, not deleted; S71 disarmed by the disarm_owner when S29 passes.
- **ACCEPT:** on each clone `.git/hooks/post-commit` has 0 lines naming stitch-refresh beside a positive control (the two other hook
  lines present); `bash .tools/stitch-refresh` exits non-zero with the refusal text and both keys' LastModified are unchanged across
  the attempt; a commit touching `org/modules/graph/` on each clone followed by a 120 s wait leaves both keys' LastModified unchanged;
  the marker's `producer` reads `stitch-codebuild` at the read.
- **INTERIM, from this record until S29 passes:** no seat runs `.tools/stitch-refresh` by hand; F-3's marker reads carry their UTC
  instant beside the producer (2.0.0_SA_COO~A's in-grant ruling stands); `0.0.0_AB_MSTR` asks site Z for its uninstall NOW.

## Ruling ratified into s.6 as R16
A word bound to a stated premise does not bind past that premise; where two of Andrew's words name one object in opposite
directions, the later governs and the earlier is kept verbatim, marked SUPERSEDED with the later word cited -- never edited away,
never silently.

**Push state:** LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 18:24Z; re-read at send).
