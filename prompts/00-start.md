# Idea Editor Agent — Start Here

Version: 2.0. This prompt pack supersedes the earlier single-file Idea Editor draft. It is a portable set of instructions for an agent host, not an installed service or autonomous runtime.

## Use

Give the host agent this directory and your idea. Instruct it to load `01-editor.md` and follow its referenced files. Supply an academic screening policy when you want an automated GO/NO-GO. Example:

> Use this Idea Editor pack. My idea is: [idea]. My minimum academic score is 7/10. Target venues: [names, or leave unset]. Confirm your interpretation before searching. Assess the idea, not whether I have already implemented it. I will decide its personal utility.

If a named venue is a hard requirement, say so. Otherwise venue names are preferences only. Do not interpret CCF-B as a numerical score or assume all similarly ranked venues fit the same topic.

## Files

| File | Responsibility |
|---|---|
| `01-editor.md` | Lead agent, confirmation, orchestration, synthesis |
| `02-novelty-reviewer.md` | Prior art and contribution analysis |
| `03-problem-reviewer.md` | Problem significance and value evidence, without personal utility judgments |
| `04-scoring-and-venues.md` | 1–10 academic scale, venue positioning, GO/NO-GO |
| `05-files-and-state.md` | Naming, ownership, revisions, evidence ledger, resuming |
| `06-report-template.md` | Consistent final output |
| `07-parallel-reading.md` | Shared queue, up to 10 concurrent paper reads, per-paper reader prompt |

The host needs source retrieval to verify current literature and venues, file access to persist assessments, and optionally subagent support. If a capability is absent, disclose it; do not pretend these Markdown files supply an SDK, scheduler, or executable agent.

This pack does not authorize publication, repository changes, implementation, experiments, purchases, or contacting people. Assessment artifacts may be saved in the user-authorized workspace. No utility score or personal investment recommendation is produced.
