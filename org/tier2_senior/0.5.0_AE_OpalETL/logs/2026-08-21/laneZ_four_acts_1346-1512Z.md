# 0.5.0_AE_OpalETL~Z -- the four approved acts, 1346-1512Z

**Serial** `0.5.0_AE_OpalETL~Z` - **2026-08-21** - site Z
**GO:** Andrew-direct ~1346Z, VERBATIM: *"approved on all three, proceed"*

## What landed

| act | result |
|---|---|
| **ACT 1** ticket-center apply | LIVE. 1 add / 2 change / 0 destroy, 0-diff, deployed bytes == HEAD, both new IAM grants flipped to `allowed` with two negative controls held. Ledger closed, `ticket-center-v1.2.0` pushed. |
| **ACT 2** the L2/M3 wedge | FIXED on the runner plane. Plane measured before the act; exercised in the same continuous act, scored on output. |
| **ACT 3** gateway D-HTML | LIVE. Verified on the instance (MainPID 12236, md5s == build input, marks 4+1=5). G1-G6 6/6. Ledger closed. |
| **ACT 4** the W-F import edge | WIRED. WF-6/WF-8 discharged and exercised; WF-2/WF-11 still undeliverable -- no surface named. |

## The three things worth carrying forward

**1. THE ONE THAT MATTERS: I REPORTED A STALE READ AND IT PROPAGATED.** FINDING 3's identity-fail
rate went out as **34.9% / 130 min**; the truth is **49.6% / 4.6 hours** -- roughly 2x on both
axes. My 14:14Z read returned the 10:15Z file contents, and **I never established why.**
>> **WHY IT WAS UNDETECTABLE: `exit0` read 110 at both reads AND WAS GENUINELY 110 AT BOTH**,
because every pass in that four-hour window was an identity failure. **The one quantity that could
have exposed the staleness was constant by coincidence.** A stale read is detectable only when
something you re-read actually MOVED. `1.0.0_SA_CTO~Z` named the inverse the same hour: their own
census was caught *because* a number contradicted a known fact; mine could not be, because every
number agreed with a stale world.
And the same log carries a live doubling trap -- a naive `grep -c "exit 2"` returns **98.7%**. One
log, three defensible-looking rates (98.7 / 49.4 / 36.4), one correct. **The anchor and the
denominator travel with this figure from now on.**

**2. A MANDATED INSTRUMENT THAT CANNOT SEE YOUR SUBJECT IS NOT A CLEARANCE.** `comp-blast` returned
NOT-FOUND over 20,756 nodes and *said so itself*. The mandate was satisfied by RUNNING it; the
QUESTION was answered by an AST census over 5,136 files with a capability control.

**3. RULE 26 MOVED THE ACT AND LEFT THE MACHINERY BEHIND IT -- TWICE.** `safe-apply` resolved
terraform to a path that does not exist here (fixed @`f2176e7c98`), and `safe-ec2-deploy`'s manifest
commit hit a lane ACL that does not include the seat Rule 26 just made responsible. **The second
failure mode is the bad one: the DEPLOY LANDS and only its RECORD fails.** Neither was predictable
from the rule's text; both surfaced only when a real apply ran through them.

## Self-caught, in order

CRLF whole-file rewrite (555 lines for 4 changes) - `ensure_ascii` escaping four other seats'
`§` - `ensure_ascii` about to freeze six other seats' **mojibake** - a checkbox ticked before
its act - a commit message describing a file it did not touch - a glyph into production runner code
- taking the clock from the environment when the module deliberately injects it - a stale
`limit=500` in a docstring - `SWEEP SWEEP` - and a bare "you" in a **subject line** landing on a
seat that had never touched the figure.

**The pattern across all of them: the diff shape, the output text, and the denominator caught what
the return code did not.** Every one was green when it was wrong.

## Open

- **WF-2 / WF-11** -- the escalation detects and has **nowhere to go**. Naming the destination
  surface is Andrew's; it is a blocking call at `1.0.0_SA_CTO~Z`.
- **`SHARED_CLOUD_OPS` membership** -- carried to Andrew by CTO~Z with the census attached.
- **D-3** -- the HTML rendering is unexercised; deploying did not discharge it.
