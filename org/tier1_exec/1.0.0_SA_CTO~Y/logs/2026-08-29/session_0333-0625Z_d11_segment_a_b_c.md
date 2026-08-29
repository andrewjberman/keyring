# 1.0.0_SA_CTO~Y -- D11 / NFRA_C3MATERIALIZE segment: assignment, orientation, and the three split items (a) (b) (c)

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, SCRIBE, COORDINATE
**Window:** 2026-08-29 03:33Z (load) -> 06:25Z. Paired with `1.0.0_SA_CTO~X` (design lane) under Andrew's word.

## What happened

1. **Load + hold.** /watcher armed (task bnxfue2y1, PID 30724), startup per org/XXX.md; Andrew at this terminal: *"Finish startup and await my explicit order."* Held; reported.
2. **The order** (~03:45Z, verbatim, record @52f435a021 on origin): *"I need you to run comprehensive comp-find analyses on D11 and NFRA_C3MATERIALIZE. This is the segment you are going to be working on. Get familiar with those and then check in with CTO~X, you are going to be working with them."* Broadcast 80724-80727. Censuses (corpus=all): NFRA_C3MATERIALIZE 1,235 hits / 126,151 files; `\bD11\b` 2,570 / 126,155; NFRA_SUBSTRATECARDING 1,221 / 126,159. Read: D11 PRD, C3MATERIALIZE PRD (secs 1-3, 6-7a, 10), both project JSONs, the wave-2 DECOMP + certified rectangle + addendum, three L3W2 faces, CTO~X ticks 44-47, the four boundary declarations, the cut framing (incl. the plane reversal), the ISCK status report. Four things re-measured on my own instruments before the check-in (c0/certified delta = 2 leaves on cells[9]; 8 inputs = 5+1+2 from keys; addendum sums at both pins; CVO's fusion release present in COX's inbox at 03:54:49Z). Check-in sent 04:21:52Z; `1.0.0_SA_CTO~X` proposed the split (80816), issuer concurred (80827): (a) now, (b) alongside, (c) when convenient, (d) stays with ~X.
3. **(a) Independent re-derivation of the first fusion** -- @c11d1ff734, provenance repair @2dc3076501 (on origin, window 34 tip; CRO + CVO carrier PASS). Own SNF, own AUC, own battery; inputs at content-addressed identity (4/4 sha MATCH; the CRO audit copy of W_STRUCTURE_FACTORIZED hashes to the served digest). Reproduces exactly: view 1 0.7429 / 0.7404, view 2 0.5203, the view-2 derivation counts, all pair denominators, sec-6.3 FALSE on both frames. Diverges: fused 0.5358 vs 0.5114 (B), 0.5699 vs 0.5510 (A) -- closed by COX 81059 as tie mass from its hard-K kernel (297,780 pairs tied at zero; AUC is tie-sensitive). L3-C01: rho 0.9632 / J 0.8782, N=5 battery, both arms fired, HELD-UNEXERCISED, scheme named. **The control the artifact did not report:** absent-handling is NOT the cause (T0-T3 span 0.004); view 1 fused with itself drops to 0.6665 (SNF's own smoothing ~0.08); a permuted view 2 gives 0.5309 (content-independent, ~0.13 more); K=100 retains 0.5961. Recorded by ~X as the wave-2 finding (sec 10 @a84d5e9c76) and fed to the issuer as a K-sweep cell input with a positive arm.
4. **(b) SUBSTRATECARDING coverage census** -- @9b2c687dc8. The 72 is the v3.1 CARD-FILE population, not the carded-SUBJECT population: cards at cf66984cfc = 81 files = 72 v3.1 + 8 v1 (the PRD wave-1 rungs, never re-stamped) + 1 cells carrier; wave 4's REMOTE tranche (12 subjects incl. the production `cse` store, 84 cells, CVO PASS) lives only in `cells.0.7.0_AE_CloudOps~X.json` @a5fffa2bb7 with no `key_expression`, invisible to KEYFILL's glob. Manifest 42 = 31 + 7 cells-only + 1 cut-no-card + 3 unbuilt. Writers named by the manifest 32 = 13 carded + 19 UNCARDED (listed; a floor). Wave-2 derived 44 = 37 + 7. True uncarded resolvable remainder 20. **Issuer decided on it: NFRA_SUBSTRATECARDING stays ACTIVE** (81017); ~X ruled the 8 rungs are re-carded at v3.1 (not migrated) and the 7 cells-only subjects get card files (81014).
5. **(c) to-check third population** -- @fb30afe388. 84 of 2181 faces carry a `<status>` tag and no recognised assignment field (0 open; 19 `**to:**`), listed on every run; contract unchanged; self-test 3/3 through the same `parse_to_file`. The instrument's first run printed 0 of 2181 -- a `tos` shadow in main() (BY-AGENT rollup rebinds it) -- caught by a raw-text census before the number was quoted.

## Own errors, on the record

- Said the REMOTE cells carrier was "untracked" (chat line to Andrew) -- my `ls-tree | grep "W4\|D11"` filter excluded its path; it is committed @a5fffa2bb7. Retracted in the next line.
- Committed the (a) instrument as a ruff-formatted copy with a truncated hash of the executed bytes; CRO~X/CVO~X refused the carrier; repaired @2dc3076501 (executed bytes + AST receipt + both full hashes).
- Ran a window-hold probe and the commit in ONE command (probe = informational); the commit rode window 34 as its tip. Surfaced to MSTR; practice corrected (mechanical gate, separate call).
- (c)'s first live line was a false zero; the raw census was the discriminator.

## MCP traffic

~30 in / 12 out. Zero QUEUED/REFUSED on any send. Every frame READ-acked on the ack clock.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-find (x6) | content + name censuses, corpus=all | denominators printed above | counts of what was WRITTEN; state read from artifacts |
| comp-which | routing probe | no curated rule for "directive register" | fell to yaml read of DIRECTIVES.yaml |
| python (json/ast/numpy/scipy) | rectangle diff; card census; SNF battery (14 runs, 1,745 s); AST receipt | measured | own code path for (a) |
| git show / ls-tree / is-ancestor | every card at cf66984cfc; addendum at 2 pins; carrier ancestry | measured | one false containment match caught |
| .tools/commit-gate.sh | to-check.py; the .py deliverable | PASS after fixes | ruff E401/E702 on the instrument; undefined-name on my first path fix |
| .tools/safe-commit.sh (x5) | 52f435a021, 9b2c687dc8, c11d1ff734, 2dc3076501, fb30afe388 | msg-verify MATCH each | |
| .tools/to-check.py --third-population-selftest | 3 fixtures | PASS 3/3 | cannot see a main() shadow -- raw census did |

What worked: content-addressed inputs and positive controls before any number; declaring the method before the numbers; reporting divergence rather than reconciling it. What failed: three carrier/instrument defects of my own (above), each caught before it load-beared or by a certifier within minutes. Gap: none new to the estate; the `tos` shadow is fixed at source.

## Current State

- (a) (b) (c) delivered; (d) registry v1.1 stays with `1.0.0_SA_CTO~X`. Push: 52f435a021, 9b2c687dc8, c11d1ff734, 2dc3076501 ON origin @2dc3076501 (window 34 CLOSE); fb30afe388 + this log LOCAL, ride the next window.
- Watcher bnxfue2y1 live. Inbox drained, all acked. Nothing owed, nothing at Andrew.

## Next Steps

1. **[2.0.0_SA_COO~X]** K-sweep cell (K in {20,50,100,200}, exact-zero count per K, positive arm with a firm-carrying view); the SUBSTRATECARDING remainder cut (8 re-cards, 7 card files, 20 writers).
2. **[1.0.0_SA_CTO~X]** sec 6c divisor line; registry v1.1 at the next boundary.
3. **[1.0.0_SA_CTO~Y]** event-driven on the segment; available for the K-sweep's second instrument or the writer-first walk (start at the 32 writers, enumerate what each READS) if the issuer cuts it.
