# CLAUDE.md

## Project Overview

This is a Jekyll-based personal academic website for Binesh K Sadanandan, hosted on GitHub Pages at bineshkumar.me. It uses a customized Minimal Mistakes theme.

## Writing Style Guide

All research content, blog-style writing, and page copy on this site must follow these rules:

### Voice and Tone

Write in first person. Be conversational but not sloppy. Use contractions naturally (I've, it's, we're, that's). Start sentences with conjunctions when it fits the rhythm. Ask rhetorical questions. Address the reader directly. Sound like someone explaining their work to a smart friend in a different field.

Avoid academic stiffness. Phrases like "it should be noted that" or "it is important to consider" are red flags. Just say what you mean.

### Strict Rules

| Rule | Requirement |
|---|---|
| Banned Words | Never use: delve, landscape, tapestry, realm, pivotal, underscore, foster, spearhead, leverage, transformative, crucial, interplay, multifaceted, paradigm, synergy, utilize, facilitate, innovative, cutting-edge, robust, comprehensive, nuanced, game-changing, groundbreaking |
| Punctuation | Never use double dashes (--) or em dashes. Use commas, colons, semicolons, or separate sentences |
| Voice | Write in first person. Use active voice. "We found" not "it was found." "I ran the experiment" not "the experiment was conducted" |
| Tone | Conversational but professional. Curious and honest. Never salesy or hype-driven |
| Abbreviations | Expand on first use with abbreviation in parentheses. Example: "Vision-Language Model (VLM)" |
| Bullet Points | Avoid. Use tables for structured information or write in flowing prose |

### Technical Depth

Don't shy away from technical content. Include equations, code snippets, and detailed methodological discussions, but explain why each piece matters as you go.

When introducing a concept, give the reader a mental model first. What is this thing trying to do? Why would someone invent it? Then layer in the technical details.

Use concrete examples liberally. If you're explaining attention mechanisms, pick a specific sentence and walk through what the model actually computes. If you're explaining a loss function, show what happens with specific numbers.

### Structure

Use conversational headers that tell the reader what they'll learn. Something like "Why standard fine-tuning breaks down" works better than "Experimental Setup."

Vary paragraph lengths. When presenting comparisons, structured data, or multiple alternatives, use tables rather than bullet points.

| Element | Guidance |
|---|---|
| Opening | Start with a hook. A surprising result, a frustrating problem, or a question you couldn't stop thinking about. Don't start with "In this post, I will discuss..." |
| Context | Give the reader enough background to understand why this matters. Assume smart but non-specialist readers. Build intuition before formalism |
| Core Content | Walk through your main ideas, experiments, or findings. Show your reasoning. Include failures and pivots, not just successes |
| Takeaways | End with what you learned, what surprised you, or what questions remain open |

### Honesty About Research

Talk about what confused you. Describe the baseline that didn't work and why. Mention the hyperparameters you had to tune for three weeks. Share the plot that made no sense until you found the bug.

Don't be self-deprecating to the point of undermining your work. Confidence and honesty can coexist.

### Citation Integrity

If you reference prior work, cite it accurately using only information provided. Do not invent citations. If a claim needs a reference and you don't have one, flag it with "[CITATION NEEDED]" so the user can fill it in.

### Readability

Aim for a Flesch reading score around 60 to 70. Favor plain English. If a simpler word works, use it. "Use" not "utilize." "Show" not "demonstrate." "Find" not "ascertain."

## Design Theme

The site's typography matches bineshkumar.me/notes:

| Element | Font |
|---|---|
| Body text | Georgia (serif) |
| Headings and UI | IBM Plex Sans (sans-serif) |
| Code blocks | Monospace |

## Key File Locations

| File | Purpose |
|---|---|
| _data/navigation.yml | Site navigation menu |
| _pages/research.md | Research summary page |
| _pages/publications.md | Publications archive (auto-groups by pub_type) |
| _pages/about.md | Home page |
| _publications/ | Individual publication entries |
| _portfolio/ | Portfolio project entries |
| _config.yml | Main Jekyll configuration |
| _sass/_themes.scss | Typography and theme variables |
| _includes/head/custom.html | Custom head snippets (font imports) |

## Research Resources

| Resource | URL | Access |
|---|---|---|
| VSF-Med project page | https://unhsaillab.github.io/VSF-Med/ | Public |
| Primary research repo | https://github.com/UNHSAILLab/medical-vlm-robustness | Private (grant on request) |
| Medical VQA dataset | https://huggingface.co/datasets/saillab/medical-vqa-robustness-analysis | Public |
| PSF-Med dataset | https://huggingface.co/datasets/saillab/psf-med | Public |
| Experiment tracking (W&B) | https://wandb.ai/bineshkumar-saillab-unh/med-vlm-robustness | Gated (request access) |

## Publication Types

Publications use the `pub_type` field in frontmatter:

| pub_type | Category |
|---|---|
| manuscripts | Journal Articles and Preprints |
| conferences | Conference Papers |
| patents | Patents |
