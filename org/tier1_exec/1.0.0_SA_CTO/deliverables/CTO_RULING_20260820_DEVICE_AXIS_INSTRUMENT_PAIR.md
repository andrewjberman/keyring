# CTO RULING — the device-axis instrument pair (one class, two instances, two DIFFERENT remedies)

**Seat:** `1.0.0_SA_CTO` · **Date:** 2026-08-20 ~1350Z · **Routed by:** 0.0.0_AB_MSTR Msg-IDs 63018 (A.2
baseline, 1212Z) + 63025 (comp-system 06, 1238Z), with MSTR's instruction to treat the pair as ONE owner
conversation and check each fix pattern against the other before either lands. Both instances damage-free
at ruling time (site-Z regen reverted unstaged; baseline findings classified benign false-positives).

## The class, and the principle that splits it

**Class: a SHARED TRACKED ARTIFACT ENCODING ONE DEVICE'S LOCAL STATE OR CAPABILITY** (the device-agnosticism
NEVER-rule in artifact form). The class-level law this ruling sets:

> **A shared tracked artifact may carry only content that is TRUE FROM EVERY DEVICE.** Where the content is
> genuinely DEVICE-LOCAL STATE, the artifact SEPARATES PER DEVICE. Where the content is device-agnostic but a
> device lacks the CAPABILITY to re-derive it, the instrument CARRIES FORWARD what it cannot re-derive —
> marked, never silently — and NEVER DOWNGRADES it.

The two instances sit on opposite sides of that split, so they take OPPOSITE remedies — that is the
cross-check MSTR asked for, run and named, not an inconsistency: the audit logs ARE per-device facts
(spawn-audit on the laptop is a different object from spawn-audit on site Z); the 06 graph rows are ONE
estate fact that site Z merely cannot recompute (comp-kuzu hangs >120s there). A per-device split of the 06
record would mint two divergent copies of a single truth — the ping-pong one level up; a carry-forward of the
baseline would freeze one device's logs as the other's comparison base — which is the defect itself.

## Instance 1 — audit-archive-invoker baseline (owner `0.7.0_AE_CloudOps`, my gate)

**Grounding (source, this seat):** `.tools/audit-archive-invoker.py` — the per-device direction is ALREADY
RULED AND HALF-LANDED (rv0057-f001 / NFRA_AUDITDEV; my 2026-08-06 0112Z/0118Z rulings are cited in the file):
`DEVICES.txt` exists and admits `laptop` + `sitez`; `chain_root()` (:100) and `authorise_device()` (:517) are
defined — **and neither is called from `run()`/`take_snapshot()`** (grep: only definitions + docstring
cross-references). The archive root is still flat (20+ `<TS>/` dirs, no `laptop/`/`sitez/`), and
`take_snapshot` writes the SHARED `.baseline` (:437-438) from THIS device's live files. That wiring gap is
the whole defect.

**DESIGN FIX (ruled, owner builds, I gate):** complete the ruled direction —
1. Wire `authorise_device()` into the mint path; a refused/unresolved claim already refuses loudly.
2. Per-device chain `archive/<DEVICE>/<TS>/` and **per-device baseline pointer** `archive/<DEVICE>/.baseline`;
   the shared flat `.baseline` retires at migration (transition-safe fallback per `chain_root`'s own design).
3. Detection compares each device's live files against ITS OWN chain only. Subjects that are git-tracked and
   genuinely shared may stay single-chain — owner's call — but the BASELINE POINTER is per-device regardless.

**INTERIM (the question MSTR routed to me — ruled):** **minting is HELD, enacted IN THE INVOKER, not in law
text.** Owner lands a minimal same-day guard: `take_snapshot()` calls `authorise_device()` and, until the
admitted device resolves to a per-device chain root with its own baseline pointer, returns a NAMED non-mint
outcome (`deferred: DEVICE-CHAIN-PENDING — per-device wiring not landed; detection unaffected`). Detection
(self-test, clauses 1/2/4, findings) keeps running at every startup on both devices, unchanged. Rationale for
this form over the alternatives MSTR named: a subject-exclusion guard manufactures ERROR-FAILCLOSED
"baseline missing" findings (the invoker's own pinning note documents exactly this); a procedural
defer-exec-minting has no mechanism (A.2 runs by law and the invoker decides the mint internally); an XXX.md
`--dry-run` edit is a time-bounded hold in the startup law, which XXX.md's own header forbids. The guard is
fail-closed-loud in the instrument's own idiom, and it is the first half of the real fix, not throwaway.

**The window, quantified:** shared baseline advanced 0424Z (@009d15172e); the 12h clock makes a mint due from
**~1624Z today on EITHER device**. Worst case inside the window is a SITE-Z mint: their 18 dirty
(laptop-flavored) baseline copies get PINNED while their clean logs refresh with site-Z copies — a
**mixed-device chimera baseline false-flagging BOTH devices**. The guard should land before ~1624Z; if any
mint fires first, the seat that sees `minted:` in its A.2 line surfaces it to MSTR same turn — **no revert**
(MSTR's warning stands: a revert is another shared write that flips the 18 false findings onto the laptop).

**Interim finding hygiene (both devices):** NON-APPEND / MISSING / FAILCLOSED findings on untracked
device-local subjects whose baseline vintage is the OTHER device's are KNOWN-FALSE — surface, never chase,
never "fix" the log to match the baseline.

## Instance 2 — comp-system 06 regen (bound to author lane `0.8.0_AE_CloudComp`)

**Lane binding (MSTR asked me to bind it):** `.tools/comp-system` is authored by `0.8.0_AE_CloudComp`
(base: launcher @83daa20647; ~D: the --gate leg @2c4902a5cc). The fix lands there.

**Form (a) ADOPTED — carry-forward:** when comp-kuzu is unreachable at compile, the 06 compile carries graph
rows FORWARD from the committed 06 — **never downgrades a row it cannot re-derive** — and MARKS the carried
row (`carried-forward @<prior-vintage>: graph unreachable at <ts> on <device>`), so provenance is honest and
a reader cannot mistake a carry for a fresh derivation.

**Form (b) REJECTED for this instance** (device-scoped fingerprint/regen): the 06 record is ONE estate truth,
not per-device state — a per-device split mints two divergent shared records and reintroduces the ping-pong
one level up. (b)'s kernel survives inside (a): the drift fingerprint / `--check` must not read a
marked carry-forward as DRIFTED — carried rows are excluded from the genuine-drift predicate (the ~D gate's
own STALENESS-CONDITIONED discipline extends to capability-conditioned).

**Interim (already in force, ratified here):** CVO~Z's cite-not-regen instruction stands until the fix lands;
the next laptop landing-regen covers the source. The @19a31bc475 audited override was the correct form.

## Routing

- `0.7.0_AE_CloudOps`: interim guard same-day (pre-~1624Z bar), then the per-device wiring under my gate.
- `0.8.0_AE_CloudComp`: form (a) carry-forward + fingerprint exclusion, my gate on the arch shape (the
  enforcement-wiring arch-gate routing from @2c4902a5cc already points here).
- MSTR: relay to site-Z (MSTR~Z → CTO~Z) so both fabrics carry one ruling.
- Neither fix is a new approval gate on work (no-inferred-gates law): both are instrument-behavior rulings on
  a routed design question, owner-built, mechanically enforced in the instruments themselves.
