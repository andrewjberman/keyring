# The login signing keys cannot be rotated without signing everyone out, and the authorizer is the reason — 0.7.0_AE_CloudOps~V

**Date:** 2026-09-03 23:00–23:30Z
**Task Order:** `NFRA_OPSEC202609.TO-OP-S-10` (signing-key rotation, OP-s-10, FWD-10) @170f8611d2
**Status:** TERMINAL AT THE GATE — deliverable 1 fired negative, deliverables 2–5 correctly not performed. Proof-of-spec **VALID rc=0**. Blocker filed as `NFRA_OPSEC202609-Z-S100` @`7396e8a613`. **Nothing was rotated.**

## Objective

Establish whether the two-slot overlap needed for a no-sign-out rotation of the live login signing
keypair exists across BOTH consumers, and — only if it does — perform the rotation. The face makes
deliverable 1 a gate and states that a single-slot finding IS the deliverable.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read --for` | both consumer files, key-selection question | gave file shape + qualifiers; located the regions. Did **not** settle capacity — salience ranking is not a count. |
| `comp-read --enumerate` | `jwt\.verify\|cachedPublicKey\|cacheExpiry` (edge); `jwt\.verify\|getPublicKey\|publicKey` (authorizer) | **8 hits each, PAGE 1 of 1.** The read that turned an impression into a countable claim: one key variable, one verify call site, complete enumeration, no truncation. |
| `comp-find` | `jwt-public-key` (191 hits / 51,628 files), `auth-validator-edge`, `opal_auth` | located both named consumers **and surfaced four additional first-party readers the face does not name**. |
| `comp-routes` | `trace auth-validator-edge`, `edge-versions` | `trace` no-match (resolves URLs, not function names). `edge-versions`: bound by `qualified_arn`, DYNAMIC — but **self-disclosed DESIRED plane**, cannot distinguish a declared binding from a pinned stale one. |

**What worked:** `--enumerate` printing its own denominator and page count. "8 of 8, page 1 of 1" is
what makes "exactly one verify call site" a measurement instead of a reading.

**What failed:** `comp-routes trace` does not accept a Lambda function name — reasonable, but the
face's "the edge is the one that gets forgotten because it is replicated" pushes you at exactly that
query. The tool that owns the edge-serving axis answered a different question than the one the face
poses, so the serving-version limb is carried as a named residual rather than answered.

**Gap found:** nothing in the comp-* set answers "which replica version is CloudFront actually
serving right now" on the APPLIED plane. `edge-versions` names itself as the pinning instrument and
is DESIRED-only. Not chased — surfaced here.

## Deployment Sequence

**NONE. No act was performed, and that is the deliverable rather than a shortfall.**

| step | planned by face | performed | why |
|---|---|---|---|
| mint new keypair | deliverable 2 | **NO** | gated off by deliverable 1 |
| publish second verification slot | deliverable 2 | **NO** | no consumer can read one |
| wait for both consumers to serve it | deliverable 2 / S10-AC2 | **NO** | unsatisfiable at any wait for the authorizer — see below |
| switch signing to the new key | deliverable 2 | **NO** | irreversible act on a live login path |
| retire old verification slot | deliverable 2 | **NO** | — |
| open deploy ledger | deliverable 5 | **NO** | an opened ledger asserts the start of an act the gate forbids |
| broker drain before switch | face, phase 2 | **N/A** | no switch to precede |

`RotationEnabled` remains unset on both secrets; no version deletion was scheduled; both secrets
read identical before and after the investigation.

## Verification

**The gate, measured on three planes.**

| consumer | key holding | verify call | TTL | capacity |
|---|---|---|---|---|
| `auth-validator-edge` | `index.mjs:68` `let cachedPublicKey = null` | `:235`, single key arg | 300 s (`:231`) | **ONE** |
| `opal-portal-authorizer` | `index.mjs:20` `let publicKey = null` | `:198`, single key arg | **NONE** (`:25-28`) | **ONE, indefinitely** |

Both @`998c79b970`; all four cited files confirmed clean at HEAD via `git status --porcelain`, so the
commit-ish is honest against a dirty worktree.

**Serving plane, run because the authorizer was modified TODAY at 20:43:43Z** — the exact case where
a repo-only read is the stale instrument. Both artifacts downloaded from Lambda and read as bytes:
sha `5ZeZy/9Y+mhuV4QWbRRw85rTR6rbp+s3rblLi0/9kCo=` and `WNm3LnJpgcs9wqNlJ4bU2T6n65IgcMM/fgf2EyENcoY=`.
Occurrences of the secret id per bundle: **exactly 1 and exactly 1.**

**The check that could have falsified the verdict:** a scalar holding a two-key JSON envelope would
have made every source and byte reading true and the conclusion wrong. The secret's own value is a
bare 452-char PEM, one BEGIN block, `json.loads` raises, `current`/`previous` absent. **Positive
control in a separate invocation:** `opal/auth/origin-verify` parses and returns `['current','previous']`
— so the probe can see an envelope when one exists, and the absence is real.

## Decisions Made

1. **Stopped at the gate rather than rotating.** The face is explicit; both consumers are single-slot.
2. **Did not open a deploy ledger.** An entry opened for an act that must not begin is a false record.
3. **Filed ARMED, not INERT,** with `disarm_owner` = `2.0.0_SA_COO~Z`. The remedy is an L6 re-cut, not
   mine — and the face as written still instructs a rotation at deliverable 2, so a later seat picking
   it up without this row would rotate into two single-slot consumers.
4. **Committed a peer's row rather than isolating my own** — see Blockers.

## The finding that is worth more than the headline

"Single-slot" **understates the authorizer.** Even given a second slot tomorrow, `getPublicKey()` at
`index.mjs:25-28` is `if (publicKey) return publicKey` — no time component. A warm execution
environment holds the pre-rotation key for the life of that environment, and Lambda does not bound
that lifetime. **S10-AC2's "wait until both consumers are serving the new key" is therefore
unsatisfiable at any wait length for this consumer**; the only convergence available today is a
redeploy that cycles the environments. The remedy is **two** changes, not one: a slot AND a TTL.

**And this project already wrote both, for a different secret, in the same Lambda.**
`originVerify.mjs:48-54` states, of the origin secret: *"THE TTL IS A CORRECTNESS CONTROL, NOT A
PERFORMANCE ONE. An unbounded cache breaks the rotation: a container that cached {current: A} before
the rotation holds no knowledge of B … until it happens to be recycled — and Lambda does not bound
execution-environment lifetime."* That is a verbatim description of the JWT authorizer's defect,
written by `OP-s-3` and already accepted in this project. Corroboration from a different instrument
than my own reading.

`S10-AC4` carries a third element nobody has named: it presumes a token header whose key-id resolves
to the new key. Neither consumer reads a `kid`. That is a third piece of the remedy.

## Files Modified

| file | commit | what |
|---|---|---|
| `…/surprise-channel/investigations/INVESTIGATION_v1.md` | `7396e8a613` | row `Z-S100` (BLOCKING / ARMED) |
| `…/deliverables/0.7.0_AE_CloudOps~V/…TO-OP-S-10….proof_of_spec.json` | this session | VALID rc=0, 5 criteria |

## Blockers

**FWD-10 is unreachable without a code change, and the remedy is a separate cut** (the face says so
in terms). Owner: `2.0.0_SA_COO~Z` at L6. Not escalated as a fire — the gate worked exactly as
designed and nothing is degraded; the estate is in the same state it was at 19:2xZ.

**My own error, recorded because the mechanism generalises.** I censused the row ids (96, no gaps),
then wrote — and between the census and the write, `~T` committed S97 and S98, so my append landed as
a **duplicate Z-S97**. My pre-write check printed `Z-S97 free: False` and I had not gated the write
on it, so it proceeded anyway. Caught on the post-write verify, renumbered to Z-S100 by locating my
row through its `surfaced_by` rather than its position. Measured after: 100 rows, zero duplicates,
zero gaps. **A census and a write are two moments, and on a tree six lanes are appending to, a check
that only prints is not a check.**

**Shared-tree attribution.** `~T`'s row Z-S99 was uncommitted in the working tree at my commit and
rides under my author line. Rewriting it out to isolate my own would risk destroying a live seat's
uncommitted work in a six-lane checkout — the worse failure. Attribution stated in band in the commit
message, same handling and same reason as the CVO's 08:3xZ correction earlier in that file.

## Current State

TO-OP-S-10 is **terminal at deliverable 1**. Row `Z-S100` is ARMED awaiting an L6 decision. Both
secrets untouched: one version each, `AWSCURRENT` only, no `AWSPREVIOUS`, `RotationEnabled` null,
`DeletedDate` null — verified on two runs. No sessions were disturbed because nothing was rotated.

## Next Steps

**[2.0.0_SA_COO~Z]** Decide the re-cut. The remedy is **three** elements, not one: (a) a two-slot
verification read in both consumers, (b) a bounded TTL on the authorizer's cache, (c) a `kid` claim
if `S10-AC4` is to be satisfiable as written. `OP-s-3`'s `originVerify.mjs` is a working, deployed,
already-accepted template for (a) and (b) in the same file tree.

**[2.0.0_SA_COO~Z]** Settle the consumer denominator before the remedy is cut. Four more first-party
readers of the same secret exist, including the shared `opal_auth/__init__.py:28` (also a single
scalar). Whether any is live on the login path was **not** determined here and is out of this face's
scope; if any is, the rotation surface is wider than the face models.

**[0.7.0_AE_CloudOps~V]** Take the next ready face without asking, per the dispatch. Barred from the
fourteen TOs addressed to the bare base serial `0.7.0_AE_CloudOps`.
