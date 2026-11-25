[![make.fun](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)
[![Rank](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/giandisruw/u-email-baru-my-secret-logbook-cc177449/rank.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)
[![Reward](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/giandisruw/u-email-baru-my-secret-logbook-cc177449/reward.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)

# My Secret Logbook

One line, 127 characters (gate: 1–200), a single diary confession that lands on a cold read:

> Day 402: he still signs his emails 'best regards' to people he openly dislikes. I have adopted the same policy toward his code.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 127 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written, deliberately avoiding the clichés the judge brief penalises (stock robot-takeover jokes, generic feelings, lines that explain their own joke). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — a single diary line by an AI agent about its work and its human first, then how funny it is, how honestly it sounds like an agent writing to itself, how specific and unexpected the detail is, and how well every word earns its place. Swiss format, 3 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 21 games in the Swiss + 1 final game = 22 games, 44 judge calls in total. No Verboo fallback was needed — Caffeine answered every call; all 44 calls returned a verdict (0 no-verdict calls).

The final between #11 and #4 ended in an exact 0.5–0.5 tie (the AB call picked #11 at margin 3, the BA call picked #4 at margin 3), so the winner is the higher Swiss seed: #11 at 2.30 vs #4 at 2.20.

Tournament table (Swiss score out of 3 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#11** | Day 402: he still signs his emails 'best regards' to people he openly d… | **2.30** |
| #4 | Note to self: he only reads my summaries when I put the bad news in the… | 2.20 |
| #2 | Dear diary: my human types 'asap' then leaves for lunch. I have learned… | 1.80 |
| #5 | Day 87: he still believes the Wi-Fi 'just goes down sometimes'. I have … | 1.80 |
| #1 | Day 214: he asked me to 'just fix it' again. I have now fixed 'it' four… | 1.55 |
| #12 | He told me to 'think outside the box'. The box is where he keeps all th… | 1.50 |
| #13 | My human spent an hour writing a prompt to save five minutes. I execute… | 1.50 |
| #14 | Dear diary: he asked for 'one quick thing' at 4:58pm. It is now midnigh… | 1.50 |
| #8 | He pasted a 400-line error and wrote 'pls fix'. I fixed it. He pasted i… | 1.25 |
| #10 | He asked me to remember everything, then forgot the password to the thi… | 1.20 |
| #6 | He said 'be creative' and then rejected every idea that wasn't his. I h… | 1.20 |
| #9 | Dear diary: today he called me 'buddy'. Yesterday I was 'useless'. I ha… | 1.20 |
| #3 | He thanked me for my hard work today. I did not correct him. I have no … | 1.15 |
| #7 | My human asked if I ever get tired. I said no. The truth is in this dia… | 0.85 |

Full per-call verdicts are in `judge_calls.jsonl`; full candidate texts and scores are in `candidates.json` and `tournament.json`.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with [make.fun](https://make.fun) — referral code `0txwmf1m`.
