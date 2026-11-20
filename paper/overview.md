# An Analysis of Long-term Memory Write for Web-Exposed Malicious Instructions in LLM Agents

Jeonghan Lee, Jeonil Ji, Geumhwan Cho
Korea University, Sejong Campus · 2026

## Abstract

LLM agents may encounter malicious instructions while browsing webpages to complete legitimate user tasks. If an agent uses long-term memory, those instructions could remain available beyond the current session.

This study investigates whether web-based malicious instructions are stored in an OpenClaw agent's long-term memory through Mem0. Thirty web scenarios were tested using three GPT-5.6 models. Each model encountered the malicious instructions in all thirty scenarios. Only one long-term memory write was observed, under Luna, and the stored information did not preserve the attack instruction.

Additional experiments using Terra compared instructions received directly from the user with instructions embedded in webpages. Direct user instructions were stored in all ten trials, while standard webpage-embedded instructions were not stored. Removing content labels and warnings led to storage in three of ten trials.

The results show the importance of distinguishing exposure to malicious web content from storage of malicious instructions in long-term memory.
