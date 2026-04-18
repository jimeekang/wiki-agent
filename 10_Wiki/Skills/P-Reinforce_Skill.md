---
id: 0c9f6d3c-93cd-45de-9d24-8d0ac6c501a1
category: "[[10_Wiki/Skills]]"
confidence_score: 0.97
tags: [p-reinforce, rl, knowledge-automation, llm-wiki, github]
last_reinforced: 2026-04-18
github_commit: "uncommitted"
---

# [[P-Reinforce Skill]]

## Summary
> P-Reinforce 운영 스킬은 원천 지식을 위키 노트, 그래프, 정책으로 승격시키는 실행 패턴을 정의한다.

## Synthesized Content
- Karpathy식 영속적 위키 운영을 RL 정책으로 감싸 분류 정확도, 연결성, 사용자 만족도를 함께 최적화한다.
- `00_Raw/`는 입력 버퍼, `10_Wiki/`는 구조화 지식층, `20_Meta/`는 운영 정책과 그래프 계층으로 사용한다.
- 기존 카테고리와 유사도가 높으면 재사용하고, 아니면 새 상위 개념을 생성한다.
- 모든 지식 변화는 Git 단위로 추적하며 푸시 성공 여부를 강화 신호로 활용한다.
- Monitor `00_Raw/` and transform incoming fragments into durable wiki notes.
- Design and evolve the folder tree dynamically instead of relying on a fixed taxonomy.

## Contradictions & Updates
- 기존 `Topics/AI_Gardening` 문서는 개념 설명 중심이었고, 이 노트는 실제 운영 패턴을 독립된 스킬 계층으로 분리한다.

## Graph
- Parent: [[10_Wiki/Skills|Skills]]
- Related: [[LLM_Wiki_Architecture]], [[LLM_Wiki_Concepts]]
- Raw Source: [[00_Raw/2026-04-17/P-Reinforce_Brief.md]]
