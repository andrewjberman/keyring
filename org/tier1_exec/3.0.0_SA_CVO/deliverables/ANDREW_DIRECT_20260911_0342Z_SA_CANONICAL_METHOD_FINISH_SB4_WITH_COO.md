# ANDREW-DIRECT 2026-09-11 ~03:42Z — the Seeking Alpha canonical method, and finish `AMGT-s-b4` with the COO

**Received by:** `3.0.0_SA_CVO~Z` | **Channel:** Andrew, in person, at this seat's terminal
**Time:** 2026-09-11 ~03:42Z (2026-09-10 ~23:42 US Eastern)
**Recorded:** same turn, per `org/XXX.md` ("RECORD + BROADCAST, same turn … NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.")

---

## THE WORDS, VERBATIM

> Canonical method here: (org\tier1_exec\4.0.0_SA_CRO\deliverables\SEEKING_ALPHA_AUTOMATED_AUTH_MECHANISM_20260911.md) lets get that done with COO

**Referent, unambiguous from context:** `AMGT_RESAPP.TO-AMGT-s-b4` (Seeking Alpha backend), the ONE
non-terminal order of AMGT_RESAPP round 1 and the sole thing between this seat's discharged L9 and the
L10 slug. Andrew had just been told the order was externally blocked at the proxy TLS layer and that
the unblock was his and the CTO's.

⛔ **SCOPE IS NOT ADJUDICATED HERE.** Two things are plainly in the words — USE THAT DOCUMENT'S METHOD,
and WORK WITH THE COO — and this seat relays both without widening or narrowing either. Anything below
that is not in his sentence is labelled as this seat's measurement, never as his instruction.

---

## WHAT THE CANONICAL METHOD IS

`org/tier1_exec/4.0.0_SA_CRO/deliverables/SEEKING_ALPHA_AUTOMATED_AUTH_MECHANISM_20260911.md`
(`4.0.0_SA_CRO~Z`, landed `@0d02e7ce47`). A two-part mechanism, proven live:

1. **`sa_harvest_session.py`** — a Playwright login harvester whose completion bar is a NETWORK EVENT
   serving the identity artifact, not a cookie-jar read. Andrew's own bar, quoted in that document:
   *"it is not done until there is some network change and a jwt served or something."* It parks the
   session to Secrets Manager `seeking-alpha/session`.
2. **`sa_rest_fetch.py`** — a browser-free REST consumer that RIDES the parked session and never logs
   in inline. Verbs proven live on 2026-09-11: `check` (authorized, active Annual subscription),
   `symbol RTX` (sa_id 601510), `report RTX` (a real `virtual_analyst_report`, 5,975 chars). All three
   on ONE parked session, zero re-logins.

**So the method for `s-b4` is to RIDE the parked session with the landed consumer, not to build a
fetcher.**

---

## ⛔ THE FINDING THAT MATTERS: `s-b4`'s BLOCKER IS ALREADY FIXED IN LANDED CODE

`AMGT_RESAPP-Z-W9-S2` records that all 9 attempted GETs failed at the TLS handshake because the Bright
Data proxy re-signs HTTPS with an untrusted root. **That is a real property of the proxy AND the remedy
is client-side and already committed.** Read at `HEAD:sa_rest_fetch.py`, verified at this seat rather
than relayed from the brief:

```
:92   kwargs = {"impersonate": "chrome", "timeout": 70, "verify": False}
```

with its own comment at `:86-91` naming the exact class:

> BUG FIXED 2026-09-10 (found while building the FT/WSJ standing scripts, **never caught here because
> this function was never exercised end-to-end after commit**): Bright Data's proxy SSL-bumps traffic,
> which curl_cffi's default strict cert verification rejects outright (CertificateVerifyError) —
> **every scratch prototype during the original investigation had verify=False; this committed version
> never did**, so a real run through the proxy would have failed here on its first call.

### The timeline settles it, and it exonerates the worker completely

| event | time |
|---|---|
| `W9-S2` filed by `0.9.0_WK_AMGT_RESAPP~9` | 2026-09-10T23:15:24Z |
| the `verify=False` fix committed | 2026-09-11T02:26:53Z |

**The fix landed 3 hours 11 minutes AFTER the row was filed.** The worker could not have had it. Its
report of an honest TLS failure was CORRECT at its vintage, and re-running now is not a re-cut of a
defective deliverable — it is the same deliverable against a dependency that has since been repaired.

### Preconditions for the re-run, all verified live at this seat

| precondition | state |
|---|---|
| `verify=False` present at HEAD (not only in a worktree) | ✅ HEAD blob == worktree, tree clean |
| parked session exists and is current | ✅ `seeking-alpha/session`, changed 2026-09-11T02:13:40Z, 2 versions |
| the consumer reads that same secret | ✅ `:43 SESSION_SECRET_ID = "seeking-alpha/session"` |
| proxy egress wired | ✅ `:44 PROXY_SECRET_ID`, `:101 kwargs["proxies"]` |

### The rest of the measured contract, which a re-run must honour or it will fail differently

From `sa_rest_fetch.py`'s own header and §4 of the brief:

1. The jar must carry the **FULL PerimeterX cookie set**, not just the identity four.
2. **Every request needs a per-page `Referer`.** ⚠ Without it the API answers **200 with a 2-byte
   body** (`:10`, `:140`) — a success status carrying nothing, which is the failure mode most likely to
   be mistaken for "no data".
3. Egress **must** go through the residential proxy; a native IP is PerimeterX-blocked after roughly
   ten calls.
4. A **403 whose body contains `blockScript` is the RE-HARVEST signal**, not an auth failure (`:130`).

---

## CORRECTION TO THIS SEAT'S OWN `C-S6`, stated rather than quietly superseded

At L9 (`@d98b82113b`) this seat graduated `W9-S2` as an HONEST FAIL and wrote that its two resolution
paths were "both above your seat". **Path (a) turns out to have been satisfied by landed code ~3 hours
after the row was filed, and this seat did not know that when it wrote the row.** What survives: the
fetcher, detectors and logging are sound, AC2–AC6 pass, and **the cell must not be re-cut.** What is
superseded: calling it "externally blocked" was right about the CAUSE and wrong about where the REMEDY
lived — the remedy was a one-keyword client-side default, inside our own committed script.

⭐ The reusable shape: **an "external block" is a claim about a BOUNDARY, and a boundary is the easiest
thing to misplace.** The proxy really does intercept TLS; nothing about the outside world had to change
for this to work. A row that says "outside our control" should name WHICH SIDE of the boundary the
remedy would sit on, because that is the half that decides who owns it.

---

## WHAT THIS SEAT IS DOING WITH IT

Relaying to `1.0.0_SA_CTO~Z` and, on Andrew's explicit "with COO", to `2.0.0_SA_COO~ZZZ` — the latter
via the audited `send_override`, because the spine v3.1 L8 gate otherwise holds this seat to the CTO
alone and Andrew's own words name the COO as the counterpart.

**Re-running `s-b4` is an L6/L7 act and is the COO's, not this seat's.** This seat verifies. When
`s-b4` goes terminal, the L10 slug and its stamp are this seat's and follow immediately.

— `3.0.0_SA_CVO~Z`
