# ANDREW DIRECT -- answers to the nine dell2 cards (2026-10-13 ~12:23Z, 8:23 AM ET)

**Channel:** Andrew, at the dell2 terminal, in the session of `1.0.0_SA_CTO~DELL2`, answering this seat's `/open-calls` card list of
2026-10-13 08:17 ET (nine cards; the list `org/devices/state/dell2/open_calls.json`).

**Verbatim:**

> 1.) I will handle this later. 2.) Seat it now. 3.) Use opalgateway to find the shared folder that I have access to. I believe Lauren has already shared it with me and you can access it on Sharepoint. 4.) I don't know what key this is nor where it lives. 5.) What do you mean "sits behind a signin", we have access to signed in session in the cloud that you can access any time via the bundled cookies we keep in the AWS cloud. 6.) We have the room to do this, yes. 7.) Yes do it. 8.) We will do this later today with #1. 9.) I need a localhost build at 5174 with details on what Im looking for to smoke, if that passes, yes we can promote.

## The cards they answer, and the act each sets

| card | open call | his answer | act |
|---|---|---|---|
| 1 | `dell2-20261012T222152Z-2e30` staff test request + two synthetic uploads | later | stays OPEN, his |
| 2 | `dell2-20261013T121849Z-d156` seat `2.0.0_SA_COO~G2` | seat it now | `0.0.0_AB_MSTR~DELL2` spawns G2; call closes |
| 3 | `dell2-20261011T023030Z-01c5` Research Meeting folder | agents find it through the gateway on SharePoint (Lauren shared it with him) | this seat searches; NFRA_TRNSPT (`~T2`) takes the location |
| 4 | `dell2-20261011T063600Z-e260` the `Opal_Terminal` key | he does not know the key or where it lives | stays OPEN; this seat proposes the next step |
| 5 | `dell2-20261012T205030Z-e41e` Black Diamond flow-timing question | no sign-in barrier: the signed-in session's cookies are kept in AWS for agents | the question is answered by an agent reading Black Diamond's own method help with the stored session (IRPT_DASHBD, `~D2`); the call closes, nothing is sent |
| 6 | `dell2-20261013T121851Z-a342` seat `2.0.0_SA_COO~C2` | yes, the room exists | `0.0.0_AB_MSTR~DELL2` spawns C2; call closes |
| 7 | `fbb1`, `5cb1` close two test tickets | yes, do it | TCKT_VNEXT (`~V2`) closes both; calls close on its receipt |
| 8 | `dell2-20261008T211740Z-3cb1` Alyssa's request | later today, with #1 | stays OPEN, his |
| 9 | portal PROD promote (`dell1-e7f2`) | a localhost build at port 5174 plus a list of what to smoke; promote if it passes | this seat builds portal DEV head on localhost:5174 and writes the smoke list |

-- recorded by 1.0.0_SA_CTO~DELL2
