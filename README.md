<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="./assets/profile-header-mobile-dark.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile-header-mobile.svg" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-header-dark.svg" />
  <img src="./assets/profile-header.svg" width="60%" alt="potatohoney-p — Agents, with a paper trail. Harness / Memory / Evaluation." />
</picture>

<p align="center">
  <a href="#selected-work">Selected work</a> &nbsp; / &nbsp;
  <a href="#beyond-the-agent-loop">Beyond the agent loop</a> &nbsp; / &nbsp;
  <a href="https://github.com/potatohoney-p?tab=repositories">All repositories</a>
</p>

I build the machinery around AI agents: **orchestration, persistent memory, and evaluation**. My public projects explore how to make the path from a prompt to a result visible, inspectable, and easier to build on.

## Selected work

Three parts of the same question: **how do we make agent work easier to inspect?**

<a href="https://github.com/potatohoney-p/weasley-subagents">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/project-subagents-dark.svg" />
    <img src="./assets/project-subagents.svg" width="420" alt="Weasley Subagents" />
  </picture>
</a>

**[Weasley Subagents ↗](https://github.com/potatohoney-p/weasley-subagents)** — Coordinate focused agents without losing the parent session. A Pi extension with parallel reviews, explicit handoffs, background runs, and bounded execution.<br /><sub>TypeScript · Pi · Worktree isolation</sub>

<a href="https://github.com/potatohoney-p/weasley-deepmind">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/project-deepmind-dark.svg" />
    <img src="./assets/project-deepmind.svg" width="420" alt="Weasley DeepMind" />
  </picture>
</a>

**[Weasley DeepMind ↗](https://github.com/potatohoney-p/weasley-deepmind)** — Give agents memory with structure. A self-hosted MCP server for typed fragments, linked evidence, and retrieval within a token budget.<br /><sub>JavaScript · PostgreSQL / pgvector · MCP</sub>

<a href="https://github.com/potatohoney-p/weasley-autoresearch">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/project-autoresearch-dark.svg" />
    <img src="./assets/project-autoresearch.svg" width="420" alt="Weasley AutoResearch" />
  </picture>
</a>

**[Weasley AutoResearch ↗](https://github.com/potatohoney-p/weasley-autoresearch)** — Make experimentation leave evidence. A guarded Pi loop that runs benchmarks, records results, keeps improvements, and reverts regressions.<br /><sub>TypeScript · Pi · Benchmark harnesses</sub>

## Beyond the agent loop

- **[Weasley Assistant](https://github.com/potatohoney-p/weasley-assistant)** — A local-first Python runtime with explicit tool calls, layered memory, traces, and deterministic evaluation.
- **[Weasley Podex](https://github.com/potatohoney-p/weasley-podex)** — A multi-agent workspace and orchestration toolkit with a browser dashboard.
- **[potato box](https://github.com/potatohoney-p/potato_wiki_box)** — Source material into a linked Markdown knowledge base, with provenance and review queues.
- **[Potaty](https://github.com/potatohoney-p/potaty)** — Editable ASCII diagrams grounded in prompts, transcripts, and repository evidence.
- **[Weasley Frame](https://github.com/potatohoney-p/weasley-frame)** — Live-web research into sourced datasets you can inspect, refresh, and export.

## Questions behind the code

**Control** — How can agents delegate work while keeping scope, state, and handoffs explicit?

**Continuity** — What should an agent remember, and what evidence should travel with it?

**Feedback** — How can we measure an improvement and retain the record of what changed?

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/potatohoney-p/potatohoney-p/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/potatohoney-p/potatohoney-p/output/github-snake.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/potatohoney-p/potatohoney-p/output/github-snake.svg" alt="Animated GitHub contributions in shades of blue, with a crimson snake head and rose body" />
</picture>

<p align="center"><sub>Open the repositories. Follow the evidence. Build on what is there.</sub></p>
