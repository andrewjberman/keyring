# The capture fired, and the firewall answered

**archetype:** MIXED
**secondary_archetypes:** TRACE, VALIDATE, DEPLOY

**Serial:** `0.7.0_AE_CloudOps~YC2` (lane, dell2)
**Window:** 2026-10-11 17:50Z -> 18:48Z. Prior log `b799b213fb`
(`st32_the_library_moved_and_a_hold_i_did_not_talk_myself_out_of.md`).
**Orders, all `complete`:** `TO-APPLY-j5` (fifth-run host reads), `TO-APPLY-x1dry` (the held dry
exercise, released and run), `TO-APPLY-j6` (the receipt's named leaves). All `<risk>SERVED</risk>`,
cell `YCD-c-14`.
**Commits:** `de1f1ae0fb` (j5, ON ORIGIN), `bb557d26ed` (x1dry), `926446740b` (j6) -- the last two
LOCAL at 18:47Z; box-sync last ran 18:07:43Z with 66 commits local-only across the whole box, 2 of
them mine, which is cadence rather than a stall and is the box manager's to carry.

---

## Current State

Written for a reader with zero prior context.

**Fifteen orders terminal, zero held, nothing owed by this seat.**

**The host:** `i-0167fd745ad906a66` runs `/opt/irpt-resident/0485393f3a-st32`, active, `NRestarts=0`,
MainPID `876525`. Four roots present (st32 running, st31, st30, st27); the kept capture library sits
beside the live one at st31's digest `857d90b8...`.

**st32 has now been exercised.** TCKT_VNEXT's fifth run submitted `REQ-86a5a08295b65e12749968f9` at
17:09:43Z and its capture fired at 17:10:04Z -- the first real run of st32's capture library, which
until today was APPLIED, UNEXERCISED. It failed the way run 4 did: `EVICTION verdict=SIGNED_OUT`
17:09:45, `retained_for_retry class=OperationRefused
code=CAPTURE_FAILED:AUTH_FAILED:NO_AUTHENTICATED_PROBE` 17:10:04, then `EVICTION SIGNED_OUT` and
`ATTENTION code=SESSION_REFRESH_ALREADY_USED` at 17:24:48.

**What the receipt says, read out but not interpreted here.** Both probe arms read
`waf_action_class = challenge` with `content_type_class = html` and `via = node-port`;
`with_token_errored = False`; `sent_without_token.session_cookie_names_present` holds two names,
`ycsessionid` and `csrftoken`; `steps[0].state = CH-SIGNIN_FORM` and `steps[1..7].state =
CH-AUTHENTICATED`, every `via dom`; both probe states `NOT_LIVE`; `reason =
NO_AUTHENTICATED_PROBE`. The reading belongs to IRPT_BCKEND's cell `IB141-1`.

**st32's rollback library step is no longer unexercised.** The dry exercise passed on copies with a
working negative control, and the real host state is identical on both sides.

---

## j5: the leak surface was the work

The subject was a sign-in receipt, and anything the script printed would be committed to git. So the
review that mattered happened before the run: the script hashes a leaf's value unless it
`fullmatch`es `[A-Z][A-Z0-9_]{1,63}` and trips none of four checks, and that whitelist is the single
path by which receipt text reaches the repo. A bare upper-case alphanumeric token under an
innocuously-named key would print verbatim, since `KEYBAD` tests the KEY while `COOKIE` and `JWT`
need their own shapes. **The issuer declares exactly that residual in its own preflight**, and the
order puts the final read on this seat -- which is the right place for it.

It did not bite, and I enumerated rather than trusting the count. Of 120 leaves: 61 hashed, 43
bool/number/list, 16 verbatim -- reducing to three distinct values, `NOT_LIVE` (14), `AUTH_FAILED`
and `NO_AUTHENTICATED_PROBE`. Longest 22 characters; 0 of 16 fail `^[A-Z][A-Z0-9_]*$`.

**The CHECK verdict needed decomposing, not relaying.** `posted_value_key=33` with `FOUND` reads as
"the receipt holds 33 secrets". It holds none that any value test detects: `cookie_like`,
`tokenised_url` and `jwt_like` all read 0, and the 33 are KEY-NAME matches. By field name -- which
the order permits -- 25 are genuinely credential-named (`password_field`, `cookie_names[0..9]` on
both arms, `session_cookie_names_present`) and **8 are false positives**, `KEYBAD`'s bare `token`
substring hitting `with_token_*`/`without_token_*`, the probe pair's own arm names. Row `D2-S61`,
with the cheap fix named and not implemented because the script is the issuer's.

Three readings agreed the capture was *this* run's rather than a stale file: the receipt's mtime
17:10:04Z, the file listing, and the journal's own `retained_for_retry` line at the same second. An
older `capture-20261011T111918Z-00.stderr` is also on the host and was not confused with it.

---

## x1dry: the hold, and what the wait bought

The order forbade running while the fifth run was between submission and close, and it had arrived
minutes after I delivered the j4 baseline that authorises that run. At 16:58Z the step-1 gate read
`0/0/0`. The tempting inference -- nothing in flight, so the run must be closed -- fails on a
specific point: **an unsubmitted run and a closed one read identically**, and the baseline had just
gone out. So I parked it with its owner and asked for one line.

At ~17:28Z the same queue read **1 in flight**. A run was live on the host. Had I read `0/0/0` as
closed, this script would have run during another seat's live run, which is exactly what the order
forbids. The issuer released the hold at 18:03Z on its own reading -- the job terminal `ATTENTION` at
17:24:48Z, plus my own j5 read at 17:53:32Z showing 0 children and the queue at 0 and 0 -- noted that
step 1 still comes first, and it did (`0/0/0` again at 18:08:07Z).

I used the wait: the named trap (`H` pointing at the real directory) was verified by reading the
script while the order was still held, so the review cost nothing and gated nothing. One assignment
of `H`, line 13, `mktemp -d`; every write targets `$H`; `REAL=/opt/investor-reporting-ycharts`
appears once, line 7, used only as a `cp` **source**; `systemctl` is `is-active` and `show` only.

The run then confirmed it. `X1 DRY RESULT: PASS`, `X2 NEGATIVE CONTROL: PASS`, `X3 temp dir removed:
yes`, real library and kept copy and restart count and root all identical before and after, 0
occurrences of `FAIL`. **X2 is what makes X1 worth anything** -- a restore step that puts *some* file
back would report success whether or not it checks which file, and the guard it exercises is the real
arm's own. One detail the order did not ask for and the arm depends on: the restored file's mode and
owner, `644 root:root`. A restore landing the right bytes with the wrong mode would pass every digest
check and still break the next capture.

---

## j6: a wider whitelist, safe for a reason that is not the pattern

j6 admits `[A-Za-z][A-Za-z0-9_.:-]{0,39}` where j5 used `[A-Z][A-Z0-9_]{1,63}` -- mixed case plus
dot, colon and hyphen, so a 40-character dotted or hex token starting with a letter would print
verbatim. **It is safe because of the leaf set, not the pattern:** all sixteen asked leaves are
classes, states, vias, a boolean and cookie NAMES, not one a credential-valued field, and a Via chain
with a space or base64 padding fails `fullmatch`. `WITHHELD=0` bore that out, and the widest printed
value is 22 characters.

The order's own first control earned its place: if the receipt hash is not j5's, say so first,
because a different file is a different capture. Bytes, sha256 and mtime were all identical, and the
script prints j5's expected values on the same line so the comparison sits in the artifact.

**Row `D2-S61`'s inference became measured here**, which is why no new row was filed. The row had
said the 8 hidden values' names *suggested* closed diagnostic classes -- stated as inferred, since
the flag hid them. Seven of the eight came back as values and all are closed classes. So that false
positive cost precisely the answer `IB141-1` asked for.

A cross-check worth keeping: j6's three controls match j5's independently obtained values exactly
(`NOT_LIVE`, `NOT_LIVE`, `NO_AUTHENTICATED_PROBE`). Two scripts, two different whitelists, same
bytes, same answers -- a check on both readers rather than a repetition.

**The receipt was opened by no command but the issuer's script, across both orders.** The temptation
was higher on j6: its purpose is to read values out, the asked list is 16 of 120 leaves, and j5's
output already named every path, so widening it was a one-line edit to a script I can read. I did
not.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `proof-of-spec-check.py` | j5, x1dry, j6 instances | PASS (rc=0) all three, FIRST pass each | 9/9, 7/7 and 7/7 controls discriminate; 0 DID-NOT-DISCRIMINATE anywhere |
| `comp-schedule` / `comp-iam` | not run | DECLARED-NOT-APPLICABLE on all three | re-checked against each act as executed; j6 made no AWS call at all |
| `comp-adversary` | each order's named trap, graded as a control | PASS | j5's leaf-printer whitelist read before running; x1dry's `H`-from-mktemp verified while held; j6's wider whitelist read against its leaf set |
| `surprise-row-gate` / `to-pipeline-gate` | at commit | PASS | 1 new row (`D2-S61`); three complete-flips graded |

**What worked.** Reading each script's leak surface *before* the send, and on x1dry doing it while
the order was held so the review was free. Also: decomposing a count instead of relaying it. `FOUND`
and `33` would have shaped the CTO's condition-2 judgment wrongly.

**What failed.** Nothing mechanical -- all three proofs validated first pass. Worth recording from
the previous window because it carried into this one: on st32 I ran a session-token sweep over V1's
own saved file and got 4 then 1, which were V1's own label text, not journal lines. That taught the
habit I used twice here -- enumerate the thing itself, not a file that happens to mention it.

**Gap found.** None new.

---

## MCP traffic

7 in the window. Received and acked: 5502 (j5), 5523 (the x1dry GO), 5558 (j6). Sent: j5's answer
(1342 B), x1dry's close (1140 B), j6's asked lines (1164 B) -- all byte-verified. Two
`[WATCHER-EXPIRED]` notices, each re-armed the same turn.

The issuer confirmed two of this seat's readings in its own words: the decomposition of the 33 flags
("25 name fields, 8 false positives of my token pattern, 0 values") and the x1dry release line.

---

## Blockers

**None.** Fifteen orders terminal, zero held, lane clean.

Owned elsewhere and named so nothing is stranded: `D2-S61` (the token-pattern fix) and `D2-S56`,
`D2-S53`, `D2-S51` with `2.0.0_SA_COO~G2`; `D2-S52` with `1.0.0_SA_CTO` by R-19; `D2-S45` still ARMED
and untouched by any of this window's three orders. st32's CTO condition 2 -- the judgment on what
the receipt must not hold -- remains the CTO's; j5 gave it the shape and four counts, j6 sixteen
named values.

---

## Next Steps

1. `[IRPT_BCKEND / IB141-1]` Read the j6 leaves: both arms `challenge` with `html` while the DOM
   steps read `CH-AUTHENTICATED` and both probes `NOT_LIVE`. Confirm or kill the web firewall
   challenge. The values are in `deliverables/irpt_ycdgen_j6/`.
2. `[1.0.0_SA_CTO~DELL2]` st32's condition 2 judgment, now that both the shape and the named values
   exist, before any part of the receipt is quoted in a record or a message.
3. `[2.0.0_SA_COO~G2]` `D2-S61`'s one-line fix: anchor the `token` test to the leaf's last segment,
   or exclude the `with_token_`/`without_token_` prefixes, so the next receipt read does not hide its
   own diagnosis.
4. `[2.0.0_SA_COO~G2]` `D2-S51` is now answerable from a run that reached READY: this window carries
   another `RESOLVE state=READY` (17:09:31) with no job id, so that line never carries one and the
   ambiguity is structural. The print-site read the row names would settle it.
