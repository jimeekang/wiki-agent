---
id: f8ecd6f9-069d-4d66-9e72-c3566cd586fa
category: "[[10_Wiki/Projects/Painting_Estimate_AI]]"
confidence_score: 0.95
tags: [gemma, multimodal-llm, estimate-ai, price-engine, case-state]
last_reinforced: 2026-04-18
github_commit: "uncommitted"
---

# [[Gemma Image Assessment Estimate Architecture]]

## Summary
> 이미지 분석은 LLM이 맡되, 가격 산정은 규칙 엔진으로 고정하고 최종 확정은 사람이 담당하는 견적 앱 아키텍처다.

## Synthesized Content
- 멀티모달 LLM은 사진에서 손상 후보를 추출하고 설명문을 쓰는 역할에 적합하다.
- 안정적인 설계는 photo analysis, case-state update, human confirmation, price engine, summary generation의 다단계 흐름이다.
- LLM 출력은 자유 텍스트보다 고정 JSON schema여야 후속 로직이 안정적이다.
- 대화 히스토리를 길게 끌고 가기보다 canonical case-state JSON만 다음 단계로 넘겨야 한다.
- 실제 제품 관점에서는 손상명보다 작업 범위(scope)와 가격 엔진 매핑이 더 중요하다.
- 사용자가 이미지를 업로드한다.

## Contradictions & Updates
- LLM을 최종 손상 판정기와 가격 결정기로 함께 쓰면 시각적 모호성과 환각 때문에 신뢰성이 떨어진다.
- Genkit은 모델 대체재가 아니라 검증과 흐름 제어를 맡는 오케스트레이션 계층으로 보는 것이 맞다.

## Graph
- Parent: [[10_Wiki/Projects|Projects]]
- Related: [[Harness_Engineering]], [[P_Reinforce_Skill]], [[Local_Agent_Obsidian]]
- Raw Source: [[00_Raw/2026-04-17/LLM 이미지 판독기.md]]
