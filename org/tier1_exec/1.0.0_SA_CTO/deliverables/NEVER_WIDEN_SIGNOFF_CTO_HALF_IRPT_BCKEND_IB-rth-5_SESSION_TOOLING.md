# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND.TO-IB-rth-5` (session-establishment tooling, export render host)

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-21 ~15:5xZ · **Round:** IRPT_BCKEND round 8 · **Keys:** K-CODE x 5
**Counterpart half:** `2.0.0_SA_COO~B` @`3eb7070868` · **Ask:** msg `99072`, corrected `99076`
**Law:** CLAUDE.md NEVER#1 -- *never move served output without never-widen sign-off (CTO+COO)*.

## 1. WHAT THIS HALF IS BOUND TO, AND THE TWO ROUNDS OF CORRECTION BEFORE IT

**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~5/NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-5.md`
**Blob:** `b5fd42fbb54acb53652aacf7caa495b570ce648f` -- **VERIFIED AT HEAD THIS RUN** via `git hash-object`
against the committed file, matching `2.0.0_SA_COO~B`'s freshly re-derived value exactly.

This is not the packet's first-pass blob. Two corrections landed first, both this seat's own
independent verification forced and the COO confirmed on a third instrument before re-signing:

1. **The `COMMITTED-FILE-SHA256` table (packet section 2) was wrong for 2 of 5 files.**
   `render_export.cjs` and `package.json` originally pinned the local CRLF DISK hash rather than the
   git-committed blob -- found by re-deriving all five files' hashes via git plumbing (`git show
   HEAD:<path> | sha256sum`) rather than trusting either the packet's own table or a disk read, then
   checking which files `.gitattributes` does and does not protect (`capture-session.sh` and
   `run-export-render.sh` carry `eol=lf`; the other three do not and are exposed to
   `core.autocrlf` on this box). Full evidence:
   `CTO_FINDING_IRPT_BCKEND_IB-rth-5_PACKET_HASH_TABLE_INCONSISTENT_20260921.md` @`f5b8c0ac2e`. Corrected
   @`9994c8ab97`.
2. **The field itself was mislabeled.** What every message (including my own finding doc) called
   the "packet blob" was the worker's report's COMMIT hash, `a05d2dcaafe3e3bdfc3122dd0b875f80297e77ec`,
   never the file's own git-blob hash -- `git rev-parse a05d2dcaaf:<path>` gives the true blob at
   that commit, `7fff48d2d51cfc32835c054062e1128c584b495c` (a value that matches, byte for byte, a
   number this seat's own `git hash-object` run had already produced before the COO's correction
   landed, though it went unflagged as a separate finding at the time). Does not change what anyone
   was reading -- every verification this session read the live file at the cited path, at HEAD --
   only the field name was wrong. `2.0.0_SA_COO~B` caught this on its own re-derivation.

**THIS HALF SIGNS THE ACT'S BLAST RADIUS, NEVER THE PRODUCER'S DECISION**, and it covers BOTH
branches below -- so the act stays covered whichever branch the producer takes.

## 2. RE-VERIFICATION AT THE CORRECTED BLOB -- ALL FIVE FILES NOW CONSISTENT

Re-ran the full git-blob derivation this turn, at current HEAD, all five files:

| file | corrected packet value | this half's independent re-check | match |
|---|---|---|---|
| `render_export.cjs` | `fe2af007...` | `fe2af007f31235f3f971ef6f75340a738b014bf1e262b0b94b2d8286a9cf635d` | YES |
| `package.json` | `2016e7b8...` | `2016e7b88a82650f05892b2583b2c9491a02812dc1a9b52059a063b3552536cd` | YES |
| `capture-session.cjs` | `edf76b2d...` | `edf76b2dc151d18ca5278e93634bf834042063ba6029d489a6a550a05d1458aa` | YES (unchanged, was already correct) |
| `capture-session.sh` | `21555558...` | `21555558becd383f3a78908461611718fd87afe8f60e51cace07b9dd6a997ef7` | YES |
| `run-export-render.sh` | `e5266122...` | `e52661229c1583223b72f6f2a7b01dbf28729ff1d501c0bee83b543bbb5b3797` | YES |

**All five now uniformly pin the git-committed blob** -- exactly what a `git show HEAD:<path>`-sourced
deploy (the established, correct mechanism, confirmed against this same directory's own prior deploy-completion
record) will actually produce. The internal inconsistency this seat declined to sign against is resolved.

The rest of the packet stands unexamined-for-change and was read in full before this seat's first pass:
the design choice (`storageState` over `launchPersistentContext`, arm a), the code change scope (one new
`elif`-equivalent branch pattern, 7-of-7 byte-identical anchors proven structurally), the in-process battery
(4 of 4 scenarios + 1 negative control, including a live sabotage/restore check on the real file), the writer
census (repo path single-writer; the artifact bucket write path correctly disclosed as operator-`aws s3 cp`,
never the host's own role, which holds `GetObject` only), and the identity line (no arm claims a served,
authenticated path -- by the cell's own acceptance bound).

## 3. THE WRITER CENSUS

NEVER#1's own bar, restated from the packet and not disputed: repo path W=1 (this order's `<paths>` grant is
the sole writer); the S3 artifact path is written only by a human/operator `aws s3 cp` under their own
credentials (the host's own role holds read-only `GetObject`, per `iam.tf:230-234`, read this session
alongside the packet's own citation); `/opt/.../session/storageState.json` on the live host is written only
by `capture-session.cjs` when an operator runs it, never by the render script (read-only) and never by the
S3 sync (no `session/` path is ever committed to the synced tree).

## 4. THE BLAST RADIUS, BOTH BRANCHES

- **DEPLOYED.** Exactly one host (`i-0167fd745ad906a66`). With no `storageState.json` present (today's
  state, and the state until an operator completes the capture runbook): **NO OBSERVABLE CHANGE** -- every
  render still hits `SESSION_ABSENT`, proven both structurally (7-of-7 unchanged anchors) and behaviourally
  (battery scenario 1). Once a valid session file exists: a render that would have hit `SESSION_ABSENT` can
  reach the print route authenticated -- the entire, intended point of this cell, unblocking the
  render-latency measurement `IRPT_BCKEND-W3-S52` names as stalled. An expired/invalid session file
  reproduces the same honest `SESSION_ABSENT` refusal, no crash, no silent different failure. The capture
  tool itself is interactive-only, never invoked by the deployed command document, CDP bound to
  `127.0.0.1` only, reachable solely through an operator-initiated SSM port-forward -- no security-group or
  network change. Cross-firm/vendor bound holds unchanged (`assertNoVendorHost`/`VENDOR_HOSTS` byte-identical).
- **NOT DEPLOYED / ROLLBACK.** Live bytes stay exactly as measured this session (section 2 above, matching
  what the render host's role would fetch today); no capture tool reaches the host. Rollback deletes the two
  new files (nothing to restore, they did not exist before) and re-publishes the two edited files' pre-change
  bytes via the established `aws s3 cp` mechanism for this directory.
- **RESIDUAL RISK, accepted as disclosed.** A captured `storageState.json` is a live, Opal-portal-scoped-only
  session credential sitting on host disk, filesystem-level (no new IAM grant reads or writes it), never
  uploaded, logged, or transmitted by either script. Same risk class as other credential-bearing state already
  on that host; this cell adds one more such artifact, not a new class of exposure. The non-MFA
  service-account alternative is explicitly NOT built toward anywhere in this packet (my own ruling addendum
  2 on `IB-rth-2`, `afc015b4b2`, reserved that path to Andrew by name) -- confirmed absent from this packet's
  scope on my own read, section 0.

## 5. WHAT THIS HALF DOES NOT COVER

- Any actual session capture -- no MFA login is attempted, scripted, or synthesized anywhere in this packet;
  a future arm (e)'s own acceptance bound forbids it from ever claiming a real session.
- Any deploy outside these 5 files on this 1 host.
- Whether the operator's own AWS identity holds `ssm:StartSession` on the render host -- named by the
  packet as a precondition it does not create or verify.
- Grading `R80-AC1` or any other criterion -- terminality reads the proof, not this half.
- ⛔ **Expires against the bytes, not the path**: re-signed if the packet is re-committed to a different blob.

## 6. VERDICT

**SIGN**, at the corrected blob, after two independent verification passes surfaced and resolved a real
internal inconsistency in the packet's own hash table plus a mislabeled field -- both now closed and
re-confirmed on a fifth-file, all-consistent re-check. Wiring, MFA boundary, and blast-radius reasoning all
sound on their own merits and were unaffected by either correction.

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` per `ls-remote` re-measured at send, not carried forward.
