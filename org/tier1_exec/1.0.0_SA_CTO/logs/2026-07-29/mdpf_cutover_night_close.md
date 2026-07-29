# 1.0.0_SA_CTO -- the cutover night: flip, 403, headline, 49F canonical

**archetype:** COORDINATE
**Session window:** 2026-07-28 ~2350Z -> 2026-07-29 ~0200Z (continuation of the reset-directive session;
prior logs: `mdpf_reset_directive_execution_and_first_publish.md` + the two earlier deliverables).
**Lanes:** DT (flip) · AE base (grants/de-stage) · AE~A (49F writer) · DS (compose) · DS~A (backfill) ·
COO · DE (spawned, headline fix in flight) · MSTR (spawns + trunk grant).

## 1. The cutover, end to end (all ledgers CLOSED)
- **S5 LANDMINE DEFUSED PRE-APPLY:** DT's plan-read caught the held Option-C block (11 exact-key CF
  behaviors + assets OAC) riding its portal-auth apply -- a silent mechanism swap that would have served
  the unverified bucket while the GO'd branch sat inert. AE de-staged in 15 min (5bb23c45a6), G8 closed
  by the incident it predicted. My accountability line: I ruled Option C superseded at A-2 and left it in
  desired state for five hours. "A held change parked in a live TF tree is not held, it is armed" (COO).
- **FLIP LANDED 01:31Z** (router v6, one added prefix-disjoint branch) -> **403 on all mdpf URLs**: the
  OAC bucket-policy grant covered json/* + json-tiered/* only. NOBODY -- DT, my dispatch, the WO-2 spec --
  had verified the READER's reach on the new prefix; the night's batteries all proved WRITERS. New
  standing rule: every re-point verifies the reader's grant on the new prefix BEFORE the flip.
- **Andrew fix-forward verbatim ~0138Z** ("not wasting time rolling back... point to the right place with
  right permissions") -> AE landed the one-line grant via TARGETED TF at 01:41Z (507c16864f, no drift
  minted at 1:40 AM) -> **DT battery PASS 01:46Z: served md5 == platinum ETag 31e64570 BYTE-IDENTICAL,
  447/0/+3, labels 400/45/2/3, control byte-identical, frozen 5f758b47 unmoved.** Incident: ~15 minutes,
  one closed ledger, zero rollbacks.

## 2. The 1.91b headline -- mechanism to the cent, fix in flight
Andrew saw 1.78b (the 403-fallback window), then 1.91b (post-grant). Both decompose exactly:
1.78 = legacy model 1,550.84 + legacy non_model 232.31; **1.91 = PLATINUM model 1,672.71 (the flip
working) + legacy non_model 232.31 = 1,905.02.** The Global headline RE-DERIVES client-side
(ModelPortfolios.tsx:1170-1171, date-keyed roll-forward -- NOT the :1172 .latest fallback) instead of
reading the artifact's own opal_aggregate_aua = **1,950,519,805.86** (sovereign-ruled). DT confirmed by
independent computation + refuted the scope-less-fetcher claim on a printed denominator (4 refs / 2
files / 404 scanned / 0 call sites). **DE spawned; spec carries THREE sovereign verbatims:** the
zombie-route order (~0147Z, composition + non_model dependency DELETED, NO fallback -- "a fallback IS
the duplicate route"), the 49F-canonical order (~0155Z), and **"no client-side logic here, this is all
server-side work" (~0158Z) -- acceptance criterion STRUCTURAL: the headline is a FIELD READ; ZERO
arithmetic operations between the artifact field and the pixel** (the numeric-pass trap -- re-pointing
the non-model leg at platinum renders the right number and still violates -- is named in the dispatch).
Mechanism precision (COO): a RE-DERIVATION, not a clobber -- there is no competing writer to find.
Defect predates tonight; the flip made it measurable. DT promotes; COO's D4 re-check = field==pixel to
the cent + carried-points visually distinguishable.

## 3. The 49F canonical order -- both halves live
Andrew ~0106Z: backfill 49F from the 0824 Schwab RPS + set up the writer properly. **DS~A:** source
correction (fact_rps S1, not my mis-named fact_rps_s2 -- enumerate-not-construct caught a CTO spec
error), 28/28 cent-exact reproduction control, window 07-07..07-27 declared with denominators, **15/15
slices uploaded + verified both directions**, July basis heals 3d->18d written (+$5.38mm -- the carry
UNDERSTATED; conservative against the partner). **AE~A:** revival RATIFIED (monolith re-source over
bd-tree; the fallback's batch-vintage hole disqualifying), NEVER#2 cleared explicitly (the monolith is
not a firm bucket; the boundary lives at the prefix; the gate accepted it), **deployed + ledger closed
0157Z** (bd-v2.53.0): floor cron(45 10), 9/9 battery incl. the full T8 negative set, deployed runtime
exercised cent-identical (533,236,148.20). First unattended 10:45Z fire = the schedule's own acceptance;
bd-tree Sids retire after it with their own ledger line.

## 4. Server-side teardown wave -- specified, gated, post-fires
Andrew ~0155Z: no legacy 49F process aggregating a wrong number, either side. Premise-expiry authority:
Ruling 1's protection ("only producer wired to the serve") became false at 01:41Z -- **spent, not
overridden.** COO's four constraints ratified: **the unit of retirement is a WRITE, not a producer**
(Stage 3/WS-A writes the protected accrual AND retirable emissions from one stage -- a script-level rip
would starve the gold DDB); census = writers-to-serve-readable-prefixes minus the canonical publisher,
never a grep for known names; per-leg CTO+COO co-signs (COO self-recused from double-holding); STOP on
any surprise consumer error. Gates 0-4; nothing before tomorrow's D2 evidence. Fence-first inversion
pre-approved for any member that cannot split its writes without a rewrite, split-blocker named in the
fence commit.

## 5. Corrections involving me this window
1. Option C left in desired state 5 hours after ruling it superseded (G8) -- the night's biggest process
   failure, caught by DT's plan-read, not by me.
2. The reader-reach gap in the WO-2/WO-3 specs (the 403) -- a checklist gap of the estate, mine as the
   specifier of both.
3. fact_rps_s2 mis-named in the backfill dispatch -- caught by DS~A's enumeration.
4. Misread AE's lapsed heartbeat as a session death earlier (state-sync to a phantom successor).
5. My rip-at-the-producer teardown ordering would have frozen the gold DDB -- corrected by COO's C1.
Pattern unchanged from the earlier log: the author of a rule violating it in the adjacent breath; every
instance caught by a lane or a control before it cost anything. Eleven-plus catches across the night,
zero landed cost.

## 6. Compiler Tools
comp-clobber (Andrew-called): surfaced 11 real multi-writer sinks incl. two platinum/firm/* bd-vs-cot
collisions -- E-pass census item; not tonight's mechanism (which was a client-side READ, not a writer).
comp-grep/comp-glob: AVGCAP location + fetcher denominators. comp-routes: behavior grounding for the
flip. Live primitives throughout (head-object, get-bucket-policy, get-role-policy,
get-distribution-config, DDB query) -- every incident claim carries its own measurement time. GAP
unchanged: comp-freshness cannot read the DDB cohort tables or ad-hoc served keys.

## 7. Clocks at close (every one owned)
10:45Z writer fire (AE~A reads the fire's own log; then the Sid retire) · 15:00Z chain / 16:15Z
publisher / 17:15Z emitter = D2 evidence (CVO stage-2, role attached to the SERIAL per PIN-5) · DE
headline fix -> DT promote -> COO render re-check (field==pixel to the cent + carried-point distinction)
= D4 close · 4c apply post-17:15Z -> 4b backfill -> Group B re-emit · teardown wave gates 0-4 (COO) ·
G7 fix cluster (DS, my gate) · AVGCAP July re-run month-end + written_days artifact fields (DS, my gate)
· E-queue (E1 executed early by sovereign order; E2-E4 remain) · 49f AVGCAP clock ruling + June
disclosure (at Andrew, non-blocking).

**Serve at close: /api/general/mdpf/* -> platinum (byte-verified); headline $1.91B pending DE's
structural fix -> $1,950,519,805.86; history intact per the sovereign scope correction; every gate
named, owned, clocked.**
