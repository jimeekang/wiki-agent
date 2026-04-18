---
id: 3a017952-dda3-42a3-b9f9-60b880cc7ed1
category: "[[10_Wiki/Topics/AI_Engineering]]"
confidence_score: 0.93
tags: [harness-engineering, ai-systems, constraints, feedback-loop, context-engineering]
last_reinforced: 2026-04-18
github_commit: "uncommitted"
---

# [[Harness Engineering]]

## Summary
> 하네스 엔지니어링은 프롬프트 자체보다 AI가 일하는 운영 환경을 설계하는 상위 개념이다.

## Synthesized Content
- 시스템 품질은 프롬프트 한 줄보다 모델이 일하는 구조화된 환경의 영향이 더 크다.
- 핵심 구성요소는 컨텍스트 엔지니어링, 제약 조건, 피드백 루프, 엔트로피 관리다.
- 규칙은 많을수록 좋은 것이 아니라, 실패를 줄이는 최소 집합이어야 한다.
- 테스트와 리뷰 같은 외부 검증이 모델의 낮은 자기평가 능력을 보완한다.
- **컨텍스트 엔지니어링 (Context):** `Claude.md`나 `Agent.md`와 같이 AI가 즉시 읽고 따를 수 있는 규칙과 정보를 코드 저장소 내에 구조화하여 제공합니다.
- **아키텍처 제약 (Constraints):** AI의 자유도를 적절히 제한하여 탐색 오류를 줄이고, 특정 행동(예: 결제 없이 외부 전송)을 물리적으로 불가능하게 강제합니다.

## Contradictions & Updates
- 프롬프트 엔지니어링이 무엇을 말할지의 문제라면, 하네스 엔지니어링은 어떤 환경에서 일하게 할지의 문제다.
- 자유도를 늘리면 창의성은 생길 수 있지만, 실무 시스템에서는 제약이 강할수록 정확도와 생산성이 오르는 경우가 많다.

## Graph
- Parent: [[10_Wiki/Topics|Topics]]
- Related: [[P_Reinforce_Skill]], [[LLM_Wiki_Architecture]]
- Raw Source: [[00_Raw/2026-04-17/하네스 엔지니어링.md]]
