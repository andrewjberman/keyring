# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rth-5: session-establishment tooling for the export
render host (`storageState` reuse in `render_export.cjs` + a new interactive SSM capture tool)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-21. **The
act signed:** the deploy this packet's arm (e) would perform, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~5/NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-5.md`
describes it at HEAD, **blob `a05d2dcaafe3e3bdfc3122dd0b875f80297e77ec`** (the worker's own report of the
committed blob; re-derive at signing: `git rev-parse HEAD:<path>`). A packet whose bytes differ from that
blob is NOT what this half signs. The CTO half is asked the same turn, by this blob.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches -- never the worker's intention.
**Independently re-verified this turn, not taken from the packet's own word:**

- **4 of 5 touched-file hashes match the packet's table exactly** on a plain disk read
  (`render_export.cjs`, `capture-session.sh`, `package.json`, `run-export-render.sh`).
- **`capture-session.cjs` does NOT** -- see row `IRPT_BCKEND-S113`, filed this turn. The packet's claimed
  hash (`edf76b2d...`, 5544 bytes) matches the GIT BLOB (`git cat-file -p HEAD:<path>`); a plain disk read
  on this box (`core.autocrlf=true`, no `.gitattributes` protection for this file) gives 5650 bytes /
  `16d420e7...` instead -- the CRLF class this project already tracks (S68). **This is NOT a blocker**:
  Node tolerates CRLF in `.cjs` source without functional change, and the one file where CRLF WOULD break
  execution (`capture-session.sh`, a shebang script) is already `.gitattributes`-protected. It IS a
  required condition on the deploy this half signs -- see the key table below.
- **The CDP bind-address security claim re-verified directly**: `capture-session.cjs:57` --
  `--remote-debugging-address=127.0.0.1`, matching the packet's "never 0.0.0.0" claim exactly.
- **The additive-only claim on `render_export.cjs`** is taken as sufficiently evidenced by the packet's
  own 7-of-7-anchor structural diff (section 2) plus the live-vs-git-HEAD baseline check (section 3) --
  not independently re-run this turn; the CRLF finding above already establishes that byte-level checks on
  this box can diverge from the git blob, so a repeat of the same class of check would not add
  independent evidence beyond what row S113 already states once.

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| `render_export.cjs` (host script) | ONE new function (`loadSessionContextOptions`), ONE new constant, `browser.newPage()` -> `browser.newContext(contextOptions).newPage()` -- functionally identical when no `storageState` file exists (7 of 7 byte-identical anchors, packet section 2) | **No `storageState.json` on the host (today's state, and the state until an operator completes arm c):** NO OBSERVABLE CHANGE -- every render still hits `SESSION_ABSENT` exactly as today. **A valid session file exists (after the human step, outside this packet):** a render that would have hit `SESSION_ABSENT` can now reach the print route authenticated -- the intended, real behavior change. **An expired/invalid session file:** falls through to the SAME `SESSION_ABSENT` refusal, never a crash or a different failure mode (packet section 3, scenarios 3-4, independently structurally sound per the 7-anchor check) | re-publish the pre-change bytes (`render_export.cjs` sha256 `37b8c4010c29d808f1e54173d7d6c3c647b45d72e204b5e1b058ed2a0d369aac`, `package.json` `2fd9400408ef3186e7918e459cae541d1e2d6988862332d444bf8aa71ca43051`, both measured LIVE this session per the packet, matching git HEAD) via the established `aws s3 cp` mechanism |
| `capture-session.cjs`/`.sh` (NEW, interactive-only tool) | Never invoked by `irpt-export-render-run`; no scheduled trigger; CDP debug port bound to `127.0.0.1` only, reachable exclusively through an operator-initiated SSM port-forward -- no security-group or network change (`irpt-ycharts-runner-sg` untouched, re-verified this turn on the one claim that matters most for exposure) | Adds the ONE interactive capability an operator needs to run arm (c)'s runbook; no effect on any render until an operator deliberately runs it | rollback DELETES both files from the S3 prefix and the host (they do not exist today, so nothing to restore); a `storageState.json` an operator may have already captured is explicitly NOT touched by this rollback (packet section 4, named so a rollback is never mistaken for revoking a session) |
| `package.json` | one new `"capture"` npm script alias; no new dependency | no behavior change to anything already running; the alias is inert until invoked | re-publish pre-change bytes (measured live, matches git HEAD, `2fd9400408...`) |

## A condition this half adds, on the deploy itself (row S113)

**Whoever executes arm (e)'s deploy must upload `capture-session.cjs` via `git show HEAD:<path>` bytes (or
an equivalent LF-preserving extraction), never a raw `aws s3 cp` of a local Windows checkout** -- on this
box's `core.autocrlf=true` config, a naive local-disk upload would ship different bytes/hash for this one
file than this packet's own COMMITTED-FILE-SHA256 table names, and the post-deploy verify-by-hash step
this project's own discipline requires (matching every other cell in this project) would either fail
correctly against the wrong reference or need reconciling against a hash nobody signed. This does not
change the code's behavior (Node tolerates CRLF) and is not a reason to refuse the deploy; it is a
precondition on HOW the deploy is executed, and it is satisfied automatically if the established
`build-and-upload.sh`-style git-blob extraction is used instead of a plain file copy.

## Both branches covered

- **Deployed** (both halves at HEAD naming this blob, the deploy-time condition above observed): the host
  gains session-reuse capability and the capture tool; no observable change to any render until an operator
  captures a real session (a separate, human, unscripted act -- never this packet's or any worker's to
  perform). Arm (e), if reached, proves ONLY the wiring against a synthetic session, per the task order's
  own acceptance bar -- never a claim of real authentication.
- **A half absent, or the blob differs at signing time:** nothing deployed; the host's live script stays
  exactly as measured (packet section 3); every render continues to hit `SESSION_ABSENT` exactly as row
  `IRPT_BCKEND-W3-S52` found it.

## What this half does NOT sign

Any actual session capture (none was attempted, scripted, or synthesized anywhere in this packet -- the
packet's own section 3 battery runs entirely against a fake `playwright` module). The non-MFA
service-account path (out of scope by the CTO's own ruling addendum 2, not touched anywhere in this
packet). Any change to portal-side auth source (none exists in this packet -- verified: the `<paths>` grant
this order carries never names `portal/`). Whether the operator's own AWS identity holds
`ssm:StartSession` on the render host (named, not created or verified, by the packet -- a separate IAM
question if it turns out absent).

**Push state:** LOCAL -- signed on `CLOUD` this turn; the CTO half is asked the same turn, by this blob.
